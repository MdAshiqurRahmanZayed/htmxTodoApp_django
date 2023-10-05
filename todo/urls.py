from django.urls import path
from todo.views import *
urlpatterns = [
    path('', todos,name='todos'),
    path('add-todo/', add_todo, name='add_todo'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('edit/<int:pk>/', edit_todo, name='edit_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),

]
