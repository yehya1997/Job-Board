from django.contrib import admin

# Register your models here.
from .models import job , catagorys

admin.site.register(job)

admin.site.register(catagorys)