from django.contrib import admin
from . models import *

# Register your models here.

class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(cat,categadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(products,prodadmin)
    
