import requests 
import json
from django.shortcuts import render

URL = 'http://127.0.0.1:5000/reservations/'

def vdm_report_page(request):
    return render(request, 'order_report.html', {})

def vdm_list_booking_page(request):
    bookings_data = requests.get(URL).text
    bookings = json.loads(bookings_data)
    print(type(bookings))
    return render(request, 'list_booking.html', {
    	'bookings': bookings,
    	})