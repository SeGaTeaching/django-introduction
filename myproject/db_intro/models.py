from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    user_email = models.EmailField(default='user@example.com')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    

# ForeignKey (Many-to-one Relationship)
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} von {self.author}'


# ManytoMany Relationship
class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'Course: {self.title} Students: {self.students}'
    
# Zwischen Modell für ManytoMany Relationships erstellen
class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateField()
    
    def __str__(self):
        return f'{self.student.name}'


# OnetoOne Relationship
class User(models.Model):
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, default='info@hiphop.net')
    
    def __str__(self) -> str:
        return self.user.username
