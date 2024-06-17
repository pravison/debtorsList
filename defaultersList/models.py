from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Defaulter(models.Model):
    customer_name = models.CharField(max_length=350)
    national_id = models.CharField(max_length=50)
    customer_location = models.CharField(max_length=50)
    bussiness_type =  models.CharField(max_length=50, help_text='type of business cutomer runs')
    number_of_loans_taken =  models.IntegerField(default= 1)
    amount_in_default =  models.IntegerField(default= 0)
    date_defaulted = models.DateField()
    company_defaulted = models.CharField(max_length=200)
    cleared = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING , blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.customer_name
