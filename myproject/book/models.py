from django.db import models
from datetime import date
 
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=20,
        choices=[
            ('fiction', 'Fiction'),
            ('nonfiction', 'Non-Fiction')
        ],
        default='fiction'
    )
    published_date = models.DateField(default=date.today)
    page_number = models.IntegerField()
    
    def __str__(self):
        return self.title
 