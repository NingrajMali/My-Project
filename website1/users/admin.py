from django.contrib import admin
from users.models import *

class logadd(admin.ModelAdmin):
    list_display=('first_Name','Last_Name','Mobile_No','Password','Confirm_Password')

admin.site.register(signup,logadd)

# Register your models here.
