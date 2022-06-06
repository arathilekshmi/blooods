from django.contrib import auth, messages
from django.contrib.auth.models import User

from .forms import DonorRegistration
from  .models import District,Center,Registrations
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def demo(request):
    return render(request,"index.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        passwrd=request.POST['passw']
        user=auth.authenticate(username=username,password=passwrd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login/')
    return render(request,'login.html')
def register(request):
    if request.method =='POST':
        username=request.POST["username"]
        passwd=request.POST["passw"]
        cpass=request.POST["passwr"]
        if passwd==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('/login/')
            else:
                user = User.objects.create_user(username=username,password=passwd)
                user.save();
                return redirect('/login/')
                print("create user")
        else:

            messages.info(request,"password not match")
            return redirect('/')
    return render(request,"reg.html")
def donor_registration(request):
    form = DonorRegistration()
    if request.method == 'POST':
        form = DonorRegistration(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"donor_list.html",{'form': form})
    return render(request, 'donar.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')


def load_center(request):
    district_id = request.GET.get('district_id')
    center = Center.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'center': center})
