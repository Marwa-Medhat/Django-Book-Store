from django.contrib import admin
from .models import Book ,Category,Tag, Isbin 
from .forms import BookForm ,categoryForm

# ,Metric 

# Register your models here.
class BookAdmin (admin.ModelAdmin):
    form=BookForm
    list_display=("title","author","content")
    list_filter=(("Categories"),)
    # search_fields=(("title"),)
class categoryAdmin (admin.ModelAdmin):
    form=categoryForm
    

class BookInline (admin.StackedInline):
    model=Book
    max_num=3
    extra=1

class TagAdmin (admin.ModelAdmin):
    inlines=[BookInline]





admin.site.register (Book,BookAdmin)
admin.site.register (Category,categoryAdmin)
admin.site.register (Tag,TagAdmin)
admin.site.register (Isbin)