from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


@login_required(login_url='login')
def home_pg(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'basic/home.html',context)


# def Topic(request, pk):
#     topic = Topic.objects.all()
#     context = {'topic' : topic}
#     return render(request,'basic/home.html' ,context)



@login_required(login_url='login')
def room_pg(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()
    context = {'room' : room, 'messages': messages}
    return render(request,'basic/room.html' ,context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {'form': form}
    return render(request, 'basic/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
        return redirect('home')
      
    
    context = {'form':form}
    return render(request, 'basic/room_form.html',context)


@login_required(login_url='login')
def basic(request):
    return render(request,'basic/base.html')


def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You Have Successfully Logged In.."))
            return redirect('home')

        else:
            messages.success(request, ("Please Try Again..."))
            return render(request, 'basic/login.html')

    else:
        return render(request, 'basic/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Successfully Logged Out .."))
    return redirect('login')


@login_required(login_url='login')
def user_account(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'account/account.html',context)


def reg_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            

    context = {'form': form}
    return render(request,'account/user_reg.html',context)
