from django.contrib import admin
from .models import Signup,Login,Book

# Register your models here.
admin.site.register(Signup)
admin.site.register(Login)
admin.site.register(Book)
