from django.contrib import admin
from django.http import HttpRequest
from .models import Category, Request
# Register your models here.

admin.site.register(Category)
admin.site.register(Request)

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('category_name', 'timestamp')
   def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance,'category_created_by'):
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


class RequestAdmin(admin.ModelAdmin):
   exclude = ('username', 'timestamp')
   list_display = ('name', 'username', 'timestamp')
   prepopulated_fields = ('username', 'timestamp')
   def save_model(self, request, obj, form, change):
       if not change:
           obj.username = request.user
       obj.save()
