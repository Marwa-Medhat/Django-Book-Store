from django import forms
from .models import Book ,Category ,Isbin
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
   
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) in range(10,50) :  
             return title
        else :
            raise ValidationError("title must be betwen  10 and 50 chars")
        
    def clean(self):
        super(BookForm,self).clean()
        # Categories=self.cleaned_data.get('Categories')
        # for category in Categories:
        #     if len (category.name) < 3:
        #          raise forms.ValidationError("category must be greater than 3 chars")
        return self.cleaned_data


  
class categoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__' # Or a list of the fields that you want to include in your form


    def clean(self):
        super(categoryForm,self).clean()
        Categories=self.cleaned_data.get('name')
        if len(Categories) <= 2:  
               raise forms.ValidationError("category must be greater than 2 chars")
        return self.cleaned_data



class uuidForm(forms.ModelForm):
    class Meta:
        model = Isbin
        fields = '__all__' 


              
   