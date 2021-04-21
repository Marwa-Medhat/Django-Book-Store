from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from django import forms
from .models import Book
from .forms import BookForm

def index (request):
    # return render(request,"books/index.html")
    books=Book.objects.all()
    return render(request,"books/index.html",{"books": books})




def create (request):
    # return render(request,"books/create.html")
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"books/create.html",{"form":form})


def edit (request,id):
    # return render(request,"books/edit.html")
    book=Book.objects.get(pk=id)
    form = BookForm(request.POST or None , instance=book)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"books/edit.html",{"form":form , "book": book})

# return HttpResponse ("hello from books store !")


def delete (request,id):
    # return render(request,"books/edit.html")
    book=Book.objects.get(pk=id)
    book.delete()
    return redirect("index")

def showbook(request,id):
    # return render(request,"books/edit.html")
    book=Book.objects.get(pk=id)
    return render(request,"books/showbook.html",{"book": book})    
   