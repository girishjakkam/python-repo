from django.contrib import admin

# Register your models here.
from .models import items ,subitems
admin.site.register(items)
admin.site.register(subitems)