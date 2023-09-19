from django.contrib import admin

# Register your models here.
from .models import Room,Message,Subject

admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Message)