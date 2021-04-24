# #  signal for create isbn objects then assign it to create book

# from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
# from django.dispatch import receiver
# from .models import Book, Isbin, User

# # after save ..sender is book
# # created when book save


# @receiver(post_save, sender=Book)
# def after_book_creation(sender, instance, created, *args, **kwargs):
#     # when create book makes isbin related to it
#     if created:
#         isbn_instance = Isbin.objects.create(
#             author_title=instance.author.username, book_title=instance.title)
#         instance.isbin = isbn_instance
#         instance.save()
#     else:
#         print("updating")
