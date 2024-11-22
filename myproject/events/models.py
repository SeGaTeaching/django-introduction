from django.db import models

# Create your models here.
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('conference', 'Conference')
    ]
    
    title = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    max_participants = models.PositiveIntegerField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    
    def __str__(self) -> str:
        return self.title
