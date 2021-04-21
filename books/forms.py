from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__' # Or a list of the fields that you want to include in your form
