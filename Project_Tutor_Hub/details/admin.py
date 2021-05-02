'''
This program will create visual database pages in Admin panel.
'''
from django.contrib import admin
from .models import Ad_Student, Ad_Tutor


admin.site.register(Ad_Student)
admin.site.register(Ad_Tutor)
