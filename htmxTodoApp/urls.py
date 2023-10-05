from django.contrib import admin
from django.urls import path,include
# from app.views import create_contact, ContactList,delete_contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todo.urls') ),

]
