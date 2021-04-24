from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver

from .models import Book,ISBN,User 

@receiver(post_save, sender = Book)
def after_book_addition(sender,instance,created,*args, **kwargs):
    if created:
        isbn_instance = ISBN.objects.create(author_title=instance.user.username,
            book_name=instance.book_name
        )

        instance.isbn = isbn_instance 
        instance.save()