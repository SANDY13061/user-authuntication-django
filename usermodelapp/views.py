from django.shortcuts import render,redirect
from usermodelapp.forms import userForm,userform3,userForm2
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from usermodelapp.models import userData


# Create your views here.
def userView(request):
    registered=False
    if request.method == 'POST':
        form1=userForm(request.POST)
        form2=userForm2(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            profile=form2.save(commit=False)
            profile.user=user
            profile.save()
            registered=True

    else:
        form1=userForm()
        form2=userForm2()
    return render(request,'registration.html',{'form':form1,'form2':form2,'registered':registered})

def user_login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if request.method == 'POST':
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('mainpage')

            else:
                return HttpResponse('user is inactive')
        else:
            return HttpResponse('entered username or password is incorrect')
    return render(request,'login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def mainpage(request):
    return render(request,'mainpage.html')

@login_required(login_url='login')
def user_update(request):
    if request.method =='POST':
        form=userform3(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    
    form=userform3(instance=request.user)

    return render(request,'user_update.html',{'form':form})

@login_required(login_url='login')
def dashboard(request):
    data=userData.objects.get(user=request.user)
    return render(request,'dashboard.html',{'form':data})



    
