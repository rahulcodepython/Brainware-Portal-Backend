from django.contrib import admin
from .models import Marks

# Register your models here.


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'grade')
    search_fields = ('id',)
