from django.shortcuts import render,redirect
from .models import Signup,Login,Book
from django.http import HttpResponse
# Create your views here.
def view(request):
    return render(request,'index.html')
# def signuptosignin(request):
#     return redirect(Login)
def signintosignup(request):
    return redirect(view)
def signup(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        phone_number=request.POST['Phone Number']
        username=request.POST['Username']
        password=request.POST['Password']
        data=Signup.objects.create(name=name,email=email,phone_no=phone_number,username=username)
        data.save()
        data1=Login.objects.create(username=username,password=password,type=1)
        data1.save()
        return render(request,'login.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        try:
            data=Login.objects.get(username=username)
            if data.password==password:
                request.session['id']=username
                if data.type==1:
                   return redirect(bookstore)
                else:
                    return redirect(librarian)
            else:
                return HttpResponse("password error")
        except Exception:
            return HttpResponse("username error")
    else:
        return render(request,'login.html')

def signout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(signin)


def bookstore(request):
    data=Book.objects.all()
    return render(request,'bookstore.html',{'data':data})



def changepasswordview(request):
    return render(request,'changepasswordview.html')

def changepassword(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        new = request.POST['New']
        try:
            data1 = Login.objects.get(username=username)
            if data1.password == password:
                data1.password = new
                data1.save()
                return render(request, 'login.html')
            else:
                 return HttpResponse("password error")
        except Exception:
          return HttpResponse("username error")
    else:
        return redirect(changepasswordview)





def addbook(request):
    if request.method=='POST':
        BOOK_NAME=request.POST['Book_name']
        AUTHOR=request.POST['Author']
        GENRE=request.POST['Genre']
        data=Book.objects.create(book_name=BOOK_NAME,author=AUTHOR,genre=GENRE)
        data.save()
        return redirect(librarian)
    else:
        return render(request, 'addbook.html')





def librarianlogin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        try:
            data=Librarian.objects.get(username=username)
            if data.password==password:
                request.session['id']=username
                return redirect(librarian)
            else:
                return HttpResponse("password error")
        except Exception:
            return HttpResponse("username error")
    else:
        return render(request,'librarianlogin.html')



def librarian(request):
    data=Book.objects.all()
    return render(request,'librarian.html',{'data':data})

def editbook(request,id):
    data=Book.objects.get(id=id)

    if request.method=='POST':
        newbookname=request.POST['New_Book_name']
        newauthor=request.POST['New_Author']
        newgenre=request.POST['New_Genre']
        try:
            data=Book.objects.get(id=id)
            if data.id==id:
                data.book_name=newbookname
                data.author=newauthor
                data.genre=newgenre
                data.save()
                return redirect(librarian)
            else:
                return HttpResponse("BOOK NOT FOUND")
        except Exception:
            return HttpResponse("BOOK NOT FOUND")
    else:
        return render(request,'editbook.html',{'data':data})

def deletebook(request,id):
    data=Book.objects.get(id=id)
    data.delete()
    return redirect(librarian)







def editprofileview(request):
     return render(request,'editprofileview.html')


def editprofile(request):
    if request.method == 'POST':
        username = request.POST['Username']
        new_name = request.POST['New_name']
        new_email = request.POST['New_e-mail']
        new_phone = request.POST['New_phone_no']
        print(username)
        try:
            data2 = Signup.objects.get(username=username)
            print(data2.username)
            if data2.username == username:
                data2.name = new_name
                data2.email = new_email
                data2.phone_no = new_phone

                data2.save()
                return redirect(bookstore)
            else:
                 return HttpResponse("username error")
        except Exception:
            return HttpResponse("username error")
    else:
        return redirect(editprofileview)


def historyuser(request):
    return render(request,'historyuser.html')
def historylibrarian(request):
    return render(request,'history librarian.html')


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(librarianlogin)