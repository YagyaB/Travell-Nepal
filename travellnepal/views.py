from django.shortcuts import render
from .models import Destination

# Create your views here.

def index1(request):
     return render(request, "index1.html" )


def index2(request):

    dests = Destination.objects.all()
    
    """
    dest1 = Destination()
    dest1.name = 'Dhangadhi'
    dest1.desc = 'City of Cricket'
    dest1.img = 'image/destination_1.jpg'
    dest1.price = '800'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Lumbani'
    dest2.desc = 'Birthplace of lord Budha'
    dest2.img = 'image/destination_2.jpg'
    dest2.price = '900'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Kathmandu'
    dest3.desc = 'Capital city of Nepal'
    dest3.img = 'image/destination_3.jpg'
    dest3.price = '1000'
    dest3.offer = False
    
    dests = [dest1, dest2, dest3]
    """

    return render(request, 'index2.html', {'dests': dests})

