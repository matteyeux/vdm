import requests 
import json
from django.shortcuts import render

URL = 'http://127.0.0.1:5000/reservations/'

def vdm_report_page(request):
    return render(request, 'order_report.html', {})

def vdm_booking_list_page(request):
    bookings_data = requests.get(URL).text
    bookings = json.loads(bookings_data)
    price = 0.0
    for booking in bookings:
    	for spectator in booking['Reservation']:
    		price += spectator['prix']
    	price = float("{:.2f}".format(price))	
    	total_price = {'total_prix': f'{price:.2f}' + " €"}
    	booking.update(total_price)
    	price = 0.0
    return render(request, 'booking_list.html', {
    	'bookings': bookings,
    	})

def get_booking_list(request):
    bookings_data = requests.get(URL).text
    bookings = json.loads(bookings_data)
    price = 0.0
    for booking in bookings:
    	for spectator in booking['Reservation']:
    		price += spectator['prix']
    	price = float("'%.2f".format(price))	
    	total_price = {'total_prix': price}
    	booking.update(total_price)
    	price = 0.0
    return render(request, 'get_booking_list.html', {
    	'bookings': bookings,
    	})