from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from RoomManager.models import Room


# Create your views here.
def home(request):
    return render(request, 'home.html')


def main(request):
    return render(request, 'main.html')


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
    return render(request,'rooms.html', {'rooms': rooms_lst})