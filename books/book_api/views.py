from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from book_api.models import Book
from book_api.serializer import BookSerializer
# Create your views here.

""" Normal Style - we need to follow three below steps to get JSON object
so that Serializer are used here """
def normal_book_list(request):
    books = Book.objects.all()        #Get querySet
    books_list = list(books.values()) #convert querySet into list
    return JsonResponse({
        "books" : books_list          #convert that list into to json 
    })


#Actual API
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True) # as it return many value so set many as true
    return Response(serializer.data) #Send the JSON data

@api_view(['POST'])
def create_book(request):
    print('data',request.data) # ----> it is request.data not request.body
    serializer = BookSerializer(data=request.data) # ---> it reaches def create(self,data): in serializers.py
    if serializer.is_valid(): # ----> is_valid() fn is used only if serializers has data=request.data
        serializer.save()  
        return Response(serializer.data) #send data in JSON
    return Response(serializer.errors) #send error happen in JSON


@api_view(['GET','PUT','DELETE'])
def alterBookWithId(request,id):
   
    try:
        book = Book.objects.get(pk=id) #Get the row based on selectedId
    except:
        content = {"error":"Book Id not found"}
        return Response(content,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book) #Dont add many=True as it return one data
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookSerializer(book,data=request.data) 
        # book is a instance(Target Row) and 
        # request.data contains data to be update
        # THen this statement went to def create(self,instance,new_data): as it has three parameter in serializers.py file
        if serializer.is_valid():     
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book.delete() # selected book based on ID is deleted
        content = {'message': 'Data is deleted'}
        return Response(content,status=status.HTTP_200_OK)