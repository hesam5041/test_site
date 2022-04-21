from django.contrib import admin
from .models import Work_Samples

# Register your models here.

class Work(admin.ModelAdmin):
    list_display = ("title" , "status")
    list_filter = (["status"])
    search_fields = ("title" ,)
    ordering = ["status"]


admin.site.register(Work_Samples , Work)
