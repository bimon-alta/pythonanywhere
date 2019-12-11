from django.contrib import admin
from .models import Mentor,Mentee,Blog

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Blog)