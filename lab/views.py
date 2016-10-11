#coding:utf-8
from django.shortcuts import render
from django.template import  loader,Context
from django.http import HttpResponse
from django.shortcuts import  render_to_response
from lab.models import Author,Book
from django.core.mail import send_mail
import json
# Create your views here.
def mybook(request):
    return render_to_response('mybook.html')

def addNewAuthor(request):
    name = request.GET['name']
    age = request.GET['age']
    age=int(age)
    country=request.GET['country']

    a1=Author()
    a1.Age=int(age)
    a1.Country=country
    a1.Name=name

    a1.save()
    print "添加新作者成功"
    return render_to_response('mybook.html')

def addNewBook(request):


    isbn=request.GET['isbn']
    title=request.GET['title']
    publisher=request.GET['publisher']
    publishdate=request.GET['publishdate']
    price=request.GET['price']
    authorname=request.GET['authorname']

    author=Author.objects.filter(Name=authorname)
    print author
    if(len(author)==0):
        return HttpResponse("作者不存在,请先录入作者")
    b1=Book()
    b1.ISBN=isbn
    b1.Title=title
    b1.Publisher=publisher
    b1.PublishDate=publishdate
    b1.Price=float(price)
    b1.author=author[0]
    b1.save()

    print '添加书籍成功'
    return render_to_response('mybook.html')

def search(request):
    authorname=request.GET['authorname']
    a1=Author.objects.get(Name=authorname)
    books=list(Book.objects.filter(author=a1))
    di={"name":"zhangxu","age":18}
    li=["zhangxu","huoshoukang","12"]
    return render_to_response("books.html",{"books":books,"author":a1,"di":json.dumps(di),"li":json.dumps(li)})


def getDetails(req):
    isbn=req.GET["isbn"]
    book=Book.objects.get(ISBN=isbn)
    author=book.author

    isbn=book.ISBN
    price=str(book.Price)
    publisher=book.Publisher
    publishdate=str(book.PublishDate)
    title=book.Title

    name=author.Name
    age=str(author.Age)
    country=(author.Country)

    reponse = u"书籍信息" + "</br>"

    reponse+=u"标题："+title+"</br>"
    reponse += u"ISBN：" + isbn + "</br>"
    reponse += u"出版社：" + publisher + "</br>"
    reponse += u"出版日期：" + publishdate + "</br>"
    reponse += u"价格：" + price + "</br>"
    reponse += "---------------------------------------</br>"

    reponse += u"作者信息：" + "</br>"

    reponse += u"作者姓名：" + name + "</br>"
    reponse += u"作者年龄：" + age + "</br>"
    reponse += u"作者国籍：" + country + "</br>"
    reponse += "---------------------------------------</br>"
    return HttpResponse(reponse)
def delete(req):
    isbn=req.GET["isbn"]
    Book.objects.get(ISBN=isbn).delete()
    return HttpResponse()
def getUpdate(req):
    isbn=req.GET["isbn"]
    return render_to_response("upDateBook.html", {"isbn": isbn})

def update(req):
    publisher=req.GET["publisher"]
    date=req.GET["publisher"]
    price=req.GET["price"]
    authorname=req.GET["authorname"]
    isbn=req.GET["isbn"]

    book=Book.objects.get(ISBN=isbn)
    author=Author.objects.get(Name=authorname)

    book.PublishDate=date
    book.Price=float(price)
    book.author=author
    book.Publisher=publisher
    return render_to_response("mybook.html")
