from django.shortcuts import render
from rest_framework import generics
from .serializer import ClientSerializer,ProjectSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import viewsets

# Register a client
# Register a client
class addClient(generics.CreateAPIView):
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

#List a clients
class listClient(generics.ListAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

#Edit client info
class editClient(generics.RetrieveUpdateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

#Delete client Info
class deleteClient(generics.DestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

#Add new projects for a client and assign one or multiple users to those projects.
class createListProject(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

#Update or Delete project and its user or clients
class editDeleteProject(generics.RetrieveUpdateDestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    
#Index Page
def index(request):
    return render(request,'index.html')

# List of all projects assigned to the  user
from rest_framework import status

@api_view(['GET'])
def getProject(request, id):
    try:
        projects = Project.objects.filter(users=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

class Anonymous(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer