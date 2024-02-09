from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from RoomManager.models import Room
from RoomManager.models import RoomManager
from datetime import date, datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class MainView(View):
    def get(self, request):
        searched_room_name = request.GET.get('room_name', '')
        searched_room_capacity = request.GET.get('room_capacity')
        searched_projector_YES = request.GET.get('checkbox')
        searched_projector_NO = request.GET.get('checkbox2')
        rooms_lst = Room.objects.all()
        rooms_lst = rooms_lst.filter(room_name__icontains=searched_room_name)
        if searched_room_capacity:
            rooms_lst = rooms_lst.filter(room_capacity__gte=searched_room_capacity)
        if searched_projector_YES:
            rooms_lst = rooms_lst.filter(projector=searched_projector_YES)
        if searched_projector_NO:
            rooms_lst = rooms_lst.filter(projector=searched_projector_NO)
        if len(rooms_lst) == 0:
            ero = 'NO ROOMS FOUND'
            return render(request, 'main.html', {'rooms': rooms_lst, "ero": ero})
        return render(request, 'main.html', {'rooms': rooms_lst})


class AddRoom(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        if len(request.POST.get('name')) > 0:
            name = request.POST.get('name')
            rooms_lst = Room.objects.all()
            if not rooms_lst.filter(room_name=name):
                if request.POST.get('capacity') and int(request.POST.get('capacity')) > 0:
                    capacity = request.POST.get('capacity')
                    if request.POST.get('projector'):
                        projector = True
                    else:
                        projector = False
                    Room.objects.create(room_name=name, room_capacity=capacity, projector=projector)
                    return redirect('main')
                else:
                    ero = "Wrong room size"
                    return render(request, 'add_room.html', {'ero': ero})
            else:
                ero = 'Name in use'
                return render(request, 'add_room.html', {'ero': ero})
        else:
            ero = 'Wrong room name'
            return render(request, 'add_room.html', {'ero': ero})


def rooms(request):
    rooms_lst = Room.objects.all()
    today = date.today()

    return render(request, 'rooms.html', {'rooms': rooms_lst, 'today': today})


def room_details(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'room_details.html', {'room': room})


class RoomEdit(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, 'room_edit.html', {"room": room})

    def post(self, request, id):
        room = Room.objects.get(id=id)
        room_name = request.POST.get('room_name')
        if room_name == '':
            ero = "Room name cannot be empty"
            return render(request, 'room_edit.html', {'ero': ero, "room": room})
        room_capacity = request.POST.get('room_capacity')
        if room_capacity <= '0':
            ero = "Room capacity cannot be less then 1"
            return render(request, 'room_edit.html', {'ero': ero, "room": room})
        if request.POST.get('checkbox'):
            checkbox = True
        else:
            checkbox = False
        room.room_name = room_name
        room.room_capacity = int(room_capacity)
        room.projector = checkbox
        room.save()
        return redirect('rooms')


class RoomDelete(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, 'room_delete.html', {'room': room})

    def post(self, request, id):
        room = Room.objects.get(id=id)
        if request.POST.get("YES") == "YES":
            room.delete()
            return redirect('rooms')
        elif request.POST.get("NO") == "NO":
            return redirect('rooms')


class RoomReserve(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        today = date.today()
        return render(request, 'room_reserve.html', {'room': room, 'today': today})

    def post(self, request, id, ):
        today = date.today()
        room = Room.objects.get(id=id)
        if request.POST.get('commentary'):
            new_commentary = request.POST.get('commentary')
        else:
            new_commentary = '...'
        date_user = request.POST.get('date')
        if date_user >= str(today):
            date_format = datetime.strptime(date_user, "%Y-%m-%d").date()
            if date_format in [x.date for x in room.roommanager_set.all()]:
                ero = 'Date already taken'
                return render(request, 'room_reserve.html', {'room': room, 'ero': ero})
            RoomManager.objects.create(date=date_user, commentary=new_commentary, room_id_id=room.id)
            ero = F"You Booked {room.room_name} room at {date_user}"
            return render(request, 'room_reserve.html', {'room': room, 'ero': ero})
        else:
            ero = 'Date is from the past'
            return render(request, 'room_reserve.html', {'room': room, 'ero': ero})
