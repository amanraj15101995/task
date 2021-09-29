from django.shortcuts import render,HttpResponseRedirect,redirect
from mainApp.models import AccountUser
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
# Create your views here.
def home(request):
   
    if (request.method=="POST"):
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        user=auth.authenticate(username=uname,password=pwd)
        if (user is not None):
            request.session.set_expiry(60)
            auth.login(request,user)
            
            return render(request,'profile.html')
        else:
            messages.error(request,"Invalid User Name or Password")
    return render(request,'index.html')

def signup(request):
    if (request.method=="POST"):
        obj = AccountUser()
        obj.username=request.POST.get('username')
        obj.Email=request.POST.get('email')
        pwd=request.POST.get('pwd')  
        cpwd=request.POST.get('cpwd') 
        obj.address=request.POST.get('address') 
        if pwd == cpwd:
            user = User.objects.create_user(username=obj.username,password=pwd)
            obj.save()
            messages.add_message(request, messages.INFO, 'Data inserted successfully.')
        else:
            messages.error(request,"Password and comfirm Password not match")
           
        return render(request,'signup.html')    
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def showDetail(request):
    users = User.objects.all()
    Accounts=AccountUser.objects.all()
    print(users)
    print( Accounts)
    return render(request,'profile.html',{'user_detail':users,
                                          'Account':Accounts})

def update(request,id):
   
    user=AccountUser.objects.get(id=id)
    if (request.method=="POST"):
        #user.username=request.POST.get('username')
        user.Email = request.POST.get('Email')
        user.address = request.POST.get('address')
        user.save()
        return HttpResponseRedirect('/detail/')
    return render(request,'update.html',{"user":user})

def destroy(request, id):  
    Account = AccountUser.objects.get(id=id)  
    Account.delete()  
    return redirect("/detail/")  
