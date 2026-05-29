# Requisitos: pip install django
# Import: from django.contrib import admin
from django.contrib import admin

from .models import Topic, Entry


admin.site.register(Topic)
admin.site.register(Entry)