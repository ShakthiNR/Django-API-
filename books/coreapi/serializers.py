
from dataclasses import fields
from rest_framework import serializers
from coreapi.models import Color, Person

"""
1. Serializers are used to convert querySet into JSON objects
2. PeopleSerializers which inherit from ModelSerializer
    a. In class Meta 
           model = ***      --> Tells which modal to serialize(Person Model)
           fields = __all__ --> Tells all fields from Model needs to be serialized 
                            --> we can customize it by using fields = ['name','age'] -->(only name,age are serialized)
                            --> or exclude = ['name'] ---- > exclude name and other fields(age,dob) should be serialized
           depth = 1        --> Depth was used to expand foreign key, 
             |
             |--> expand the foreign key with all data {id:1,name:"red"}

            Note: Instead of using depth, use ColorSerializer as ModelSerializer with color_name as fields  
                  to expand the foreign key. Then we have use color = ColorSerializer() to serialize the foreign key
    b. we can create custom Method to add column with data.
        use get_ as prefix name to define function

3. validate the incoming data from view use def validate function
    a.  data['age'] < 18 --> from data(sent from views),check the age column is <18
"""


class LoginSerializer(serializers.Serializer): #=> Serialize is for validation  #--> 3rd
    email = serializers.EmailField()
    password =serializers.CharField()
   #to know more about serializers.Serializer see book_api folder

class ColorSerializer(serializers.ModelSerializer): #--> 2nd
    class Meta:
        model = Color
        fields =['color_name'] 

class PeopleSerializer(serializers.ModelSerializer): #--> 1st
    
   # color = ColorSerializer() #=> to serialize foreign key, it add color as column with value
  #  colorInfo = serializers.SerializerMethodField() #=> Custom function
  
    class Meta:
        model = Person  
        fields = "__all__"   
'''
    def get_colorInfo(self,obj): #=> as SerializerMethodField Name is colorInfo use get_ as prefix
        color_obj = Color.objects.get(id=obj.color.id)
        return {'colorName':color_obj.color_name,'hex_code':"#000"}


    def validate(self,data): #=> validate the column name

        specialChar = '!@#$%^&*()~`?><:"'
        if any(c in specialChar for c in data['name']):
            raise serializers.ValidationError({"error":"Name should not contain special characters"})

        if data['age'] < 18: # from data(sent from views),check the age column
            raise serializers.ValidationError({"error":"Age should be greater than 18 yrs"})

        return data
'''