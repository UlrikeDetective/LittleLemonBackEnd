from django.shortcuts import render
from .models import Menu, Booking
from django.core import serializers
from datetime import datetime
from .forms import BookingForm
from rest_framework import generics
from .serializers import MenuSerializer

# Page views
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def bookings(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(booking_date__date=date)
    booking_json = serializers.serialize('json', bookings)
    return render(request, "bookings.html", {"bookings": booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book.html', {'form': form})

def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = None
    return render(request, 'menu_item.html', {"menu_item": menu_item})

# REST API views
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
