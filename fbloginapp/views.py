from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from . models import *

# Create your views here.
def login(request):
    return render(request,'login.html')

def adlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('pswd')
    if freg.objects.filter(email=email,password=password).exists():
        data=freg.objects.filter(email=email,password=password).values('fname','lname','date','month','year','gender','id').first()
        request.session['fname']=data['fname']
        request.session['lname']=data['lname']
        request.session['date']=data['date']
        request.session['month']=data['month']
        request.session['year']=data['year']
        request.session['gender']=data['gender']
        request.session['email']=email
        request.session['password']= password
        request.session['id']=data['id']
        return redirect('login') 
    else:
        return render(request,'login.html',{'msg':"Sorry... Invalid username or password"})  

def Flogout(request):
    del request.session['email']
    del request.session['password']
    del request.session['fname']
    del request.session['lname']
    del request.session['date']
    del request.session['month']
    del request.session['year']
    del request.session['gender']
    del request.session['id']
    return redirect('login') 

def index(request):
    return render(request,'index.html')

def wdisplay(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('pswd')
        email = request.POST.get('email')
        date = request.POST.get('date')
        month = request.POST.get('month')
        year = request.POST.get('year')
        gender = request.POST.get('gender')
        data = freg(fname=fname,lname=lname,password=password,email=email,date=date,month=month,year=year,gender=gender)
        data.save()
        return redirect('login')                   

def tem(request):
    return render(request,'template.html')