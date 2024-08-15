from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import Group, User


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer


 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_list': 'account',
        'Search by age': '/?age=age_name',
        'Search by location': '/?location=location_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)

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
    room_messages = room.message_set.all().order_by('-created')

    if request.method =='POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        return redirect('room', pk=room.id)


    context = {'room' : room, 'room_messages': room_messages}
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

@login_required(login_url='login')
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
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method =='POST':
        room.delete()
        return redirect('home')
    return render(request,'account/delete.html',{'obj':room})


@login_required(login_url='login')
def basic(request):
    return render(request,'basic/base.html')



def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You Have Successfully Logged In.."))
            return redirect('home')

        else:
            messages.error(request, ("User Does not Exists ..."))
            return render(request, 'account/login_reg.html')

    context = {'page':page}
    return render(request, 'account/login_reg.html',context)


def reg_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured ,kindly check your registration..!')
            

    context = {'form': form,}
    return render(request,'account/login_reg.html',context)


def logout_user(request):
    
    logout(request)
    messages.success(request, ("You Have Successfully Logged Out .."))
    return redirect('login')


@login_required(login_url='login')
def user_account(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    prof = Profile.objects.all()
    context = {'prof':prof,'user':user,'rooms':rooms}
    return render(request,'account/account.html',context)




