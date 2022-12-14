from book_api.models import Book
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # ---> Autogenerated
    title = serializers.CharField()
    author = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    quantity = serializers.IntegerField()
    published_date = serializers.DateField()
    
    
    '''
    We Can add validate function to validate the value of incoming column before creation of it
    ex:
      def validate(self,data):

        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('Name already used')
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email already used')

        def create(self,validate_data):
            return Book.objects.create(**data)
                or

            user=User.objects.create(username=validated_data['username],email=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return validated_data

    '''

    def create(self,data): #Needed to create row
        return Book.objects.create(**data)
    
    def update(self,instance,new_data): #Needed to update row, fn's data is received by new_data
        # newdata's title get from new_data and save in that instance(selected book row to update)
        print('instance',instance)
        print('data',new_data)
        instance.title = new_data.get('title',instance.title)
        instance.author = new_data.get('author',instance.author)
        instance.number_of_pages = new_data.get('number_of_pages',instance.number_of_pages)
        instance.quantity = new_data.get('quantity',instance.quantity)
        instance.published_date = new_data.get('published_date',instance.published_date)
        instance.save() # save and return
        return instance
    

