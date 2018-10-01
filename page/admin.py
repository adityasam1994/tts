from django.contrib import admin
from .models import Memory
# Register your models here.

class MemoryAdmin(admin.ModelAdmin):
    list_display=["query","reply"]
   

admin.site.register(Memory,MemoryAdmin)