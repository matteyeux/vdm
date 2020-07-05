import requests 
import json
from django.shortcuts import render

URL = 'http://127.0.0.1:5000/bookingList/'

def vdm_report_page(request):
	return render(request, 'order_report.html', {})

def vdm_booking_list_page(request):
	bookings_kpi = requests.get('http://127.0.0.1:5000/kpiBookingList/').text
	kpi_list = json.loads(bookings_kpi)
	total_amount = 0
	nb_resa = 0
	nb_spectateur = 0
	for elem in kpi_list:
		total_amount += elem['TotalPrice']
		nb_resa += 1
		nb_spectateur += elem['NbSpectateur']

	kpi = {
		'total_amount': total_amount,
		'nb_resa': nb_resa,
		'nb_spectateur': nb_spectateur
	}
	return render(request, 'booking_list.html', {
		'kpi': kpi
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