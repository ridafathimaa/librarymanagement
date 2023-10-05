from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=50)
    username=models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.IntegerField()

    def __str__(self):
        return self.username
class Book(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    def __str__(self):
        return self.book_name


