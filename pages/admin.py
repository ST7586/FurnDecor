from django.contrib import admin

# Register your models here.
from .models import ContactQuery

admin.site.register(ContactQuery)