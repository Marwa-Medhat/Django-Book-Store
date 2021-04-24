from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django import forms
from .models import Book
from .forms import BookForm, categoryForm, uuidForm
from django.contrib.auth.decorators import login_required, permission_required


# @login_required(login_url="/login")
@login_required()
def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {"books": books})


@login_required()
def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "books/create.html", {"form": form})


@login_required()
def createcategory(request):
    form = categoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "books/category.html", {"form": form})


def createuuid(request):
    form = uuidForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "books/uuid.html", {"form": form})


@login_required()
def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "books/edit.html", {"form": form, "book": book})


@login_required()
@permission_required(["books.view_book", "books.delete_book"], raise_exception=True)
def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect("index")


@login_required()
def showbook(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "books/showbook.html", {"book": book})
