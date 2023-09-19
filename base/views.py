from django.shortcuts import render,redirect
from .models import Room,Subject,Message
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# rooms = [
#     {'id' : 1,'name' : 'Let`s Get on with C'},
#     {'id' : 2,'name' : 'Code in Java'},
#     {'id' : 3,'name' : 'Django it is'}
# ]

def loginUser(request):
    page = 'Login'
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        print(username,password)
        try:
            user = User.objects.get(username = username)     
        except:
            print("User not found")

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print("Bad Credentials")

    context = {"page" : page}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    print(q)
    rooms= Room.objects.filter(
        Q(subject__name__icontains = q) |
        Q(name__icontains = q) |
        Q(desc__icontains = q)
        )
    
    room_count = rooms.count()
    subject = Subject.objects.all()
    comments = Message.objects.filter(Q(room__subject__name__icontains = q))
    context = {'rooms' : rooms,'subjects' : subject,'room_count' : room_count,'comments' : comments}
    return render(request,'base/home.html',context)

def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('/')
        else:
            print("Bad Credentials")
    context = {"form" : form}
    return render(request,'base/login_register.html',context)

def Rooms(request,pk):
    room = Room.objects.get(id =pk)
    if request.method == 'POST':
        comment = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('/pages/'+str(room.id))
    
    comments = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    context = {'room' : room,'comments' : comments,"participants" : participants}
    return render(request,'base/rooms.html',context)


def Profile(request,pk):
    user = User.objects.get(id = pk)
    rooms = user.room_set.all()
    comments = user.message_set.all()
    subject = Subject.objects.all()
    context = {'user' : user,"rooms" : rooms,"comments" : comments,"subjects" : subject}
    return render(request,'base/profile.html',context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
            return redirect('/')
    context = {"form" : form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='/login')
def editRoom(request,pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='/login')
def deleteRoom(request,pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('/')
    
    return render(request,'base/delete_temp.html',{'obj' : room})

@login_required(login_url='/login')
def deleteMessage(request,pk):
    comment = Message.objects.get(id = pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('/pages/'+str(comment.room.id))
    
    return render(request,'base/delete_temp.html',{'obj' : comment})
