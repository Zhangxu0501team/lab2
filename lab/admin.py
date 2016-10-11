#coding:utf-8
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book,Author

class BookAdmin(admin.ModelAdmin):
    list_display = ("Price","Title","ISBN")#按顺序显示

admin.site.register(Book,BookAdmin)
admin.site.register(Author)