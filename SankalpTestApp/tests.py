from django.contrib import admin
from django.urls import path,include
from . import views as v

urlpatterns = [
    path('',v.index),
    path('POST/client',v.addClient.as_view()),
    path('GET/client',v.listClient.as_view()),
    path('PUT-PATCH/client/:<int:pk>',v.editClient.as_view()),
    path('DELETE/clients/:<int:pk>',v.deleteClient.as_view()),
    path('GET-POST/projects',v.createListProject.as_view()),
    path('editDeleteProject/:<int:pk>',v.editDeleteProject.as_view()),
    path('listProject/:<int:id>',v.getProject),
]

