from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from coreapi.models import Person
from coreapi.serializers import LoginSerializer, PeopleSerializer


# 1. api_view - decorator to create API
@api_view(['GET'])
def getDetails(request):

    if request.method =='GET': # or  if request.GET:
        obj = Person.objects.all()
        serializer = PeopleSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def createDetails(request):
    if request.method=='POST':
        data = request.data 
        serializer = PeopleSerializer(data=data) #create row
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','PATCH'])
def updateDetails(request,pk):
    try:
        obj = Person.objects.get(pk=pk)
    except:
        return Response({'error':'Entered Id not found in dB'},status=status.HTTP_404_NOT_FOUND)
    
    # Put - need to send all column (name,age,dob) in table to update
    # Patch - can be sent nly needed column(either age/dob/name) to update (PartialUpdate)
    if request.method =='PUT':
        data = request.data
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method =='PATCH':
        data = request.data
        serializer = PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteDetail(request,pk):
    obj = Person.objects.get(pk=pk)
    obj.delete()
    return Response({"message":"Item Deleted"},status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request): #-----> for validation use Serializer instead of ModelSerializer
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data=serializer.validated_data  # Get the validatedData from serializer
        return Response({'msg':"success"})

    return Response(serializer.errors)


# 2. classBasedView :
'''
1. class - Encapsulate the all the method (no need to use request.method)
2. classLevel handles all 5 methods easily. It Reduces the steps
3. then in urls.py add personAPI.as_view() 
'''
from rest_framework.views import APIView  
class personAPI(APIView): 
    def get(self,request,pk): 
        obj = Person.objects.all()
        serializer = PeopleSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request,pk):
        data = request.data 
        serializer = PeopleSerializer(data=data) #create row
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



    def put(self,request,pk):
        obj = Person.objects.get(pk=pk)
        data = request.data
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    def patch(self,request,pk):
        obj = Person.objects.get(pk=pk)
        data = request.data
        serializer = PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk):
        obj = Person.objects.get(pk=pk)
        obj.delete()
        return Response({"message":"Item Deleted"})



# 3. ModelViewSet - used to perform all CRUD in two line of code.
"""
   | -> By default it can do POST/PUT/DELETE/GET methods
   | -> It can also be restricted by explicitly saying http_method_names=['GET','POST']
   | -> need to use router in urls.py
   | -> can do actions for methods like after 'POST' method call action SENDMAIL(to send mail)
***********************************************
class PeopleViewSet(views.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.object.all()   
***********************************************
"""

# 4. Authentication - creating Token and check the token for restricted route
"""
user= authenticate(username=serializer.data['username'],password=serializer['password']) 
            |--> validate credentials
token, _ = Token.objects.get_or_create(user=user) 
                              |--> create token after login

       1. check username,pass
       2. If correct create token for them
       3. else throw error message

In restricted route        
whenever router routes   - check for token using permission authentication in setting.py
                            and in views.py  (add at top of Class api)
                                permission_classes =  [IsAuthenticated] 
                                authentication_classes = [TokenAuthentication]
                                         -> throw error if token not matched or not included 

*********************************************************************************************************************************************

"""

# 5. Pagination -see video