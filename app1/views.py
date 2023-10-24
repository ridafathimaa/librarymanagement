from django.shortcuts import render,redirect
from .models import Signup,Book,Issue
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
        data=Signup.objects.create(name=name,email=email,phone_no=phone_number,username=username,password=password,type=1)
        data.save()
        # data1=Login.objects.create(username=username)
        # data1.save()
        return render(request,'login.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        try:
            data=Signup.objects.get(username=username)
            if data.password==password:
                request.session['id']=data.id
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
    if 'id' in request.session:
        userid=request.session['id']
        user=Signup.objects.get(id=userid)
        data=Book.objects.all()
        return render(request,'bookstore.html',{'data':data,'user':user})
    else:
        return redirect(signin)

def getbook(request):
    if 'id' in request.session:
        userid=request.session['id']
        user = Signup.objects.get(id=userid)
        if request.method == 'POST':
            BOOKID=request.POST['Book_id']
            currentbook=Book.objects.get(id=BOOKID)
            if Issue.objects.filter( book_name=currentbook).exists():
                return HttpResponse ('404 NOT FOUND')
            else:
                data=Issue.objects.create(username=user,book_name=currentbook)
                data.save()
                return HttpResponse('RENTED SUCESSFULLY')






def changepasswordview(request):
    if 'id' in request.session:
        user=request.session['id']
        return render(request,'changepasswordview.html')
    else:
        return redirect(signin)

def changepassword(request):
    if 'id' in request.session:
        user=request.session['id']
        if request.method == "POST":
            # username = request.POST['Username']
            password = request.POST['Password']
            new = request.POST['New']
            try:
                data1 = Signup.objects.get(id=user)
                if data1.password == password:
                    data1.password = new
                    data1.save()
                    return redirect(bookstore)
                else:
                     return HttpResponse("password error")
            except Exception:
              return HttpResponse("username error")
    else:
        return redirect(signin)





def addbook(request):
    if 'id' in request.session:
        user=request.session['id']
        if request.method=='POST':
            BOOK_NAME=request.POST['Book_name']
            AUTHOR=request.POST['Author']
            GENRE=request.POST['Genre']
            IMAGE=request.FILES['Image']
            data=Book.objects.create(book_name=BOOK_NAME,author=AUTHOR,genre=GENRE,image=IMAGE)
            data.save()
            return redirect(librarian)
        else:
            return render(request, 'addbook.html')
    else:
        return redirect(signin)









def librarian(request):
    if 'id' in request.session:
        userid=request.session['id']
        data=Book.objects.all()
        return render(request,'librarian.html',{'data':data})
    else:
        return redirect(signin)
def editbook(request,id):
    data=Book.objects.get(id=id)

    if request.method=='POST':
        newbookname=request.POST['New_Book_name']
        newauthor=request.POST['New_Author']
        newgenre=request.POST['New_Genre']
        newimage=request.POST['New_Image']
        try:
            data=Book.objects.get(id=id)
            if data.id==id:
                data.book_name=newbookname
                data.author=newauthor
                data.genre=newgenre
                data.image=newimage
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
    if 'id' in request.session:
        user=request.session['id']
        return render(request,'editprofileview.html')
    else:
        return redirect(signin)

def editprofile(request):
    if 'id' in request.session:
        user = request.session['id']
        if request.method == 'POST':
            # username = request.POST['Username']
            new_name = request.POST['New_name']
            new_email = request.POST['New_e-mail']
            new_phone = request.POST['New_phone_no']
            # print(username)
            try:
                data2 = Signup.objects.get(id=user)
                # print(data2.username)
                # if data2.username == username:
                data2.name = new_name
                data2.email = new_email
                data2.phone_no = new_phone

                data2.save()
                return redirect(bookstore)
            # else:
            #      return HttpResponse("username error")
            except Exception:
              return HttpResponse("username error")

        else:
         return HttpResponse("username error")
    else:
        return redirect(editprofileview)


def historyuser(request):
    if 'id' in request.session:
      user = request.session['id']
      data=Issue.objects.all()
      return render(request,'historyuser.html',{'data':data})
    else:
        return redirect(signin)

def returnbook(request,id):
    data=Issue.objects.get(id=id)
    data.delete()
    return redirect(historyuser)

def historylibrarian(request):
    if 'id' in request.session:
        user=request.session['id']
        data = Issue.objects.all()
        return render(request,'history librarian.html', {'data': data})
    else:
        return redirect(signin)


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(signin)