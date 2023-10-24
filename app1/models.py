from django.db import models
from datetime import date

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.IntegerField()


    def __str__(self):
        return self.username


# class Login(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     type = models.IntegerField()
#
#     def __str__(self):
#         return self.username
class Book(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    image=models.ImageField()
    def __str__(self):
        return self.book_name


class Issue(models.Model):
    username=models.ForeignKey(Signup,on_delete=models.CASCADE)
    book_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date=models.DateField(default=date.today,blank=False)
    def __str__(self):
        return self.username.username +" "+ "Rented" + " "+self.book_name.book_name

