#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 使用MySQL建立一个“图书数据库“BookDB,包含两张表: –
# Book {ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price} –
# Author {AuthorID (PK), Name, Age, Country}


class Author(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Country=models.CharField(max_length=30)
    def __unicode__(self):
        return self.Name

class Book(models.Model):
    ISBN=models.CharField(max_length=30)
    Title=models.CharField(max_length=30)
    Publisher=models.CharField(max_length=30)
    PublishDate=models.DateField()
    Price=models.FloatField()
    author=models.ForeignKey(Author)
    def __unicode__(self):
        return self.Title