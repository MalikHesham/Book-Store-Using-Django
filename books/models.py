from django.db import models
from django.contrib.auth.models import User
import uuid

class Tag(models.Model):
    name = models.CharField(max_length=25)
    
class BookCategory(models.Model):
    class Meta:
        verbose_name_plural = "Book Categories"

    categoryName = models.CharField(max_length=50)
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.categoryName
    
class Metric(models.Model):
    liked = models.IntegerField(null=True,blank=True)
    rating = models.DecimalField(null=True, blank=True , max_digits=2 , decimal_places=1)

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name="book", null=True,blank=True )
    category = models.ManyToManyField(BookCategory)
    metrics = models.ForeignKey(Metric, on_delete = models.CASCADE , null=True , blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ISBN(models.Model):
    isbn_number = models.UUIDField(primary_key=True, default = uuid.uuid4,editable = False)
    author_title = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    book_name= models.OneToOneField(Book, on_delete=models.CASCADE, null=True, blank=True)
    

