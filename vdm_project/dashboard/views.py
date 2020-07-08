import requests 
import json
from django.shortcuts import render

from . import numFormat

# URL = 'http://127.0.0.1:5000/bookingList/'

def vdm_report_page(request):
	return render(request, 'order_report.html', {})

def vdm_booking_list_page(request):
	# bookings_kpi = requests.get('http://127.0.0.1:5000/kpiBookingList/').text
	# kpi_list = json.loads(bookings_kpi)
	# total_amount = 0
	# nb_resa = 0
	# nb_spectateur = 0
	# for elem in kpi_list:
	# 	total_amount += elem['TotalPrice']
	# 	nb_resa += 1
	# 	nb_spectateur += elem['NbSpectateur']

	# kpi = {
	# 	'total_amount': total_amount,
	# 	'nb_resa': nb_resa,
	# 	'nb_spectateur': nb_spectateur
	# }
	return render(request, 'booking_list.html', {})

# def get_booking_list(request):
# 	bookings_data = requests.get(URL).text
# 	bookings = json.loads(bookings_data)
# 	price = 0.0
# 	for booking in bookings:
# 		for spectator in booking['Reservation']:
# 			price += spectator['prix']
# 		price = float("'%.2f".format(price))	
# 		total_price = {'total_prix': price}
# 		booking.update(total_price)
# 		price = 0.0
# 	return render(request, 'get_booking_list.html', {
# 		'bookings': bookings,
# 		})

def dashboard360(request):
	# Request Chart CA per Days
	bookings_CAdays = requests.get('http://127.0.0.1:5000/caDays/').text
	CAdays_list = json.loads(bookings_CAdays)
	CAdays = [
		['Jour', 'CA', {"role": "annotation"}]
		]
	for i in reversed(range(len(CAdays_list))):
		date = CAdays_list[i]['_id']
		CA = CAdays_list[i]['CA']
		CA_anno = numFormat.formatNumberMoney(CA)
		CAday = [date, CA, CA_anno]
		CAdays.append(CAday)

	# Request Chart CA per Rooms and per Days
	bookings_CARoomdays = requests.get('http://127.0.0.1:5000/caRoomDays/').text
	CARoomdays_list = json.loads(bookings_CARoomdays)
	CARoomdays = [
		[
			'Jour',
			'Interminable attente chez le medecin', {"role": "annotation"}, 
			'Diner de famille insoutenable', {"role": "annotation"},
			'En plein dans la Friendzone', {"role": "annotation"},
			'Mon compte en banque en fin du mois', {"role": "annotation"},
			'Soutenance finale', {"role": "annotation"},
			'Plus de PQ dans les toilettes', {"role": "annotation"},
			'Impot sur le revenu', {"role": "annotation"},
			'Greve de la SNCF', {"role": "annotation"},
			'Mariage sans alcool', {"role": "annotation"},
		]
	]
	for i in reversed(range(len(CARoomdays_list))):
		date = CARoomdays_list[i]['_id']
		for elem in CARoomdays_list[i]['Rooms']:
			if elem['Room'] == 'Interminable attente chez le medecin':
				CARoom1 = elem['CA']
				CARoom1_anno = numFormat.formatNumberMoney(CARoom1)
			elif elem['Room'] == 'Diner de famille insoutenable':
				CARoom2 = elem['CA']
				CARoom2_anno = numFormat.formatNumberMoney(CARoom2)
			elif elem['Room'] == 'En plein dans la Friendzone':
				CARoom3 = elem['CA']
				CARoom3_anno = numFormat.formatNumberMoney(CARoom3)
			elif elem['Room'] == 'Mon compte en banque en fin du mois':
				CARoom4 = elem['CA']
				CARoom4_anno = numFormat.formatNumberMoney(CARoom4)
			elif elem['Room'] == 'Soutenance finale':
				CARoom5 = elem['CA']
				CARoom5_anno = numFormat.formatNumberMoney(CARoom5)
			elif elem['Room'] == 'Plus de PQ dans les toilettes':
				CARoom6 = elem['CA']
				CARoom6_anno = numFormat.formatNumberMoney(CARoom6)
			elif elem['Room'] == 'Impot sur le revenu':
				CARoom7 = elem['CA']
				CARoom7_anno = numFormat.formatNumberMoney(CARoom7)
			elif elem['Room'] == 'Greve de la SNCF':
				CARoom8 = elem['CA']
				CARoom8_anno = numFormat.formatNumberMoney(CARoom8)
			elif elem['Room'] == 'Mariage sans alcool':
				CARoom9 = elem['CA']
				CARoom9_anno = numFormat.formatNumberMoney(CARoom9)
		CARoomday = [
			date, 
			CARoom1, CARoom1_anno,
			CARoom2, CARoom2_anno,
			CARoom3, CARoom3_anno,
			CARoom4, CARoom4_anno,
			CARoom5, CARoom5_anno,
			CARoom6, CARoom6_anno,
			CARoom7, CARoom7_anno,
			CARoom8, CARoom8_anno,
			CARoom9, CARoom9_anno,
			]
		CARoomdays.append(CARoomday)

	return render(request, 'chart/dashboard360.html', {
		'CAdays': CAdays,
		'CARoomdays': CARoomdays
		})
