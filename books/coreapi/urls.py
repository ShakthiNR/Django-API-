from django.contrib import admin
from django.urls import path,include


from coreapi.views import createDetails, deleteDetail, getDetails, login, personAPI, updateDetails

urlpatterns = [
   path('getdetails/',getDetails),
   path('createdetails/',createDetails),
   path('updatedetails/<int:pk>/',updateDetails),
   path('deletedetails/<int:pk>/',deleteDetail),
   path('login/',login),
   path('persondetails-api-class/<int:pk>',personAPI.as_view()) #=> it is classBased

]