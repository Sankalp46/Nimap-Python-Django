from django.db import models 
from django.contrib.auth.models import User
# Create your models here.     

class Client(models.Model):
    client_name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(s):
        return s.client_name
    
    class Meta:
        db_table = 'Client'

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    
    class Meta:
        db_table = 'Project'

    def __str__(self):
        return self.project_name
