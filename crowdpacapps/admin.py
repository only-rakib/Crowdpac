from django.contrib import admin

# Register your models here.
from . models import Endorsement_list
from . models import Donar_list

admin.site.register(Endorsement_list)
admin.site.register(Donar_list)
