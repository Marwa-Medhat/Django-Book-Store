from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Tag (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category (models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Isbin (models.Model):
    book_title = models.CharField(max_length=255, null=True, blank=True)
    author_title = models.CharField(max_length=50)
    booknumber = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self. author_title} author_title | {self.  booknumber} booknumber "


class Book (models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=2048)
    Categories = models.ManyToManyField(Category)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="books")
    isbin = models.OneToOneField(
        Isbin, on_delete=models.CASCADE, null=True, blank=True)
    # isbin=models.OneToOneField(Isbin,on_delete=models.CASCADE,default=default)
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
