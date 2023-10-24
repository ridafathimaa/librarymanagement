"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view),
    # path('a',views.signuptosignin),
    path('signintosignup',views.signintosignup),
    path('signup',views.signup),
    path('signin',views.signin),
    path('signout',views.signout),
    path('bookstore',views.bookstore),
    path('getbook',views.getbook),
    path('changepasswordview',views.changepasswordview),
    path('changepassword',views.changepassword),
    path('librarian',views.librarian,name='librarian'),
    path('addbook',views.addbook),
    path('editbook/<int:id>',views.editbook ,name='editbook'),
    path('deletebook/<int:id>',views.deletebook),
    path('editprofileview',views.editprofileview),
    path('editprofile',views.editprofile),
    path('historyuser',views.historyuser),
    path('returnbook/<int:id>',views.returnbook,name='returnbook'),
    path('historylibrarian',views.historylibrarian),
    path('logout',views.logout)

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)