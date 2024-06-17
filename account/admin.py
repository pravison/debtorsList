from django.contrib import admin
from . models import Profile, CustomersEmail, CustomersMessages

# Register your models here.
admin.site.register(Profile)
admin.site.register(CustomersEmail)
admin.site.register(CustomersMessages)
