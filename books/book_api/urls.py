
from django.contrib import admin
from django.urls import path
from book_api.views import alterBookWithId, book_list, create_book, normal_book_list
urlpatterns = [
  path('noserial/list/',normal_book_list),
  path('list/',book_list),
  path('create/',create_book),
  path('<int:id>/',alterBookWithId)
]
