from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete= models.CASCADE)
    point = models.IntegerField(default=1)
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
     
class CustomersEmail(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
    
class CustomersMessages(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.subject