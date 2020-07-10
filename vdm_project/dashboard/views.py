import requests 
import json
from django.shortcuts import render
from django.http import JsonResponse

from . import numFormat


def homepage(request):
	return render(request, 'homepage/homepage.html', {})

def booking_list(request):
	return render(request, 'bookingList/booking_list.html', {})

def dashboard360(request):
	return render(request, 'chart/dashboard360.html', {})


############################################################################
######################      Chart to Dashboard 360      ####################
############################################################################
# Request Chart CA per Days
def get_CA_days(request, *args, **kwargs):
	bookings_CAdays = requests.get('http://127.0.0.1:5000/caDays/').text
	CAdays_list = json.loads(bookings_CAdays)
	CAdays = [
		['Jour', 'CA', {"role": "annotation"}, "Prix Moyen des réservations", {"role": "annotation"}]
		]
	for i in reversed(range(len(CAdays_list))):
		date = CAdays_list[i]['_id']
		CA = CAdays_list[i]['CA']
		CA_anno = numFormat.formatNumberMoney(CA)
		PM = CAdays_list[i]['CA']/CAdays_list[i]['Nb_Booking']
		PM_anno = numFormat.formatNumberMoney(PM)
		CAday = [date, CA, CA_anno, PM, PM_anno]
		CAdays.append(CAday)
	return JsonResponse(CAdays, safe=False) # http response

# Request Chart Number of bookings per days
def get_Nb_Bookings(request, *args, **kwargs):
	bookings_NbBooks = requests.get('http://127.0.0.1:5000/nbBookingDays/').text
	NbBooks_list = json.loads(bookings_NbBooks)
	NbBooks = [
		['Jour', 'Nombre de réservation', {"role": "annotation"}, 'Nombre de spectateurs par réservations', {"role": "annotation"}]
		]
	for i in reversed(range(len(NbBooks_list))):
		date = NbBooks_list[i]['_id']
		Nb_books = NbBooks_list[i]['Nb_Booking']
		Nb_books_anno = numFormat.formatNumberInt(Nb_books)
		M_spec = NbBooks_list[i]['Nb_Spec']/NbBooks_list[i]['Nb_Booking']
		M_spec_anno = numFormat.formatNumberFloat(M_spec)
		NbBook = [date, Nb_books, Nb_books_anno, M_spec, M_spec_anno]
		NbBooks.append(NbBook)
	return JsonResponse(NbBooks, safe=False) # http response

# Request Chart Number of spectators per days
def get_Nb_Spectators(request, *args, **kwargs):
	bookings_NbSpects = requests.get('http://127.0.0.1:5000/nbSpectDays/').text
	NbSpects_list = json.loads(bookings_NbSpects)
	NbSpects = [
		['Jour', 'Nombre de spectateurs', {"role": "annotation"}, 'Prix Moyen par spectateurs', {"role": "annotation"}]
		]
	for i in reversed(range(len(NbSpects_list))):
		date = NbSpects_list[i]['_id']
		Nb_Spects = NbSpects_list[i]['Nb_Spec']
		Nb_Spects_anno = numFormat.formatNumberInt(Nb_Spects)
		PM_Spects = NbSpects_list[i]['CA']/NbSpects_list[i]['Nb_Spec']
		PM_Spects_anno = numFormat.formatNumberMoney(PM_Spects)
		NbSpect = [date, Nb_Spects, Nb_Spects_anno, PM_Spects, PM_Spects_anno]
		NbSpects.append(NbSpect)
	return JsonResponse(NbSpects, safe=False) # http response 


############################################################################
######################      xxxxxxxxxxxxxxxxxxxxxx      ####################
############################################################################
# Request Chart CA per Rooms and per Days
def get_CA_Rooms_Days(request, *args, **kwargs):
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
	for i in range(len(CARoomdays_list)):
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
		date = CARoomdays_list[i]['_id']
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
	return JsonResponse(CARoomdays, safe=False) # http response


# Request Chart CA per Days
def get_CA_Rooms(request, *args, **kwargs):
	bookings_CArooms = requests.get('http://127.0.0.1:5000/cadRoom/').text
	CArooms_list = json.loads(bookings_CArooms)
	CArooms = [
		['Salle', 'CA', {"role": "annotation"}]
		]
	for i in reversed(range(len(CArooms_list))):
		room = CArooms_list[i]['_id']['Rooms']
		CA = CArooms_list[i]['CA']
		CA_anno = numFormat.formatNumberMoney(CA)
		CAroom = [room, CA, CA_anno]
		CArooms.append(CAroom)
	return JsonResponse(CArooms, safe=False) # http response


# Request Chart CA per Days
def get_Spect_Rooms(request, *args, **kwargs):
	bookings_Spectrooms = requests.get('http://127.0.0.1:5000/cadRoom/').text
	Spectrooms_list = json.loads(bookings_Spectrooms)
	Spectrooms = [
		['Salle', 'Nombre de Spectateurs', {"role": "annotation"}]
		]
	for i in reversed(range(len(Spectrooms_list))):
		room = Spectrooms_list[i]['_id']['Rooms']
		Spect = Spectrooms_list[i]['Nb_Spec']
		Spect_anno = numFormat.formatNumberMoney(Spect)
		Spectroom = [room, Spect, Spect_anno]
		Spectrooms.append(Spectroom)
	return JsonResponse(Spectrooms, safe=False) # http response


# Request Chart CA per thems and per Days
def get_CA_Themes_Days(request, *args, **kwargs):
	bookings_CAThemedays = requests.get('http://127.0.0.1:5000/caThemeDays/').text
	CAThemedays_list = json.loads(bookings_CAThemedays)
	CAThemedays = [
		[
			'Jour',
			'Braquage', {"role": "annotation"},
			'Stress', {"role": "annotation"},
			'Rapidité', {"role": "annotation"},
			'Mythologique', {"role": "annotation"},
			'Stratégie', {"role": "annotation"},
			'Psychologique', {"role": "annotation"},
			'Santé', {"role": "annotation"},
			'Amour', {"role": "annotation"},
			'Horreur', {"role": "annotation"},
		]
	]
	# CATheme1, CATheme2, CATheme3, CATheme4, CATheme5, CATheme6, CATheme7, CATheme8, CATheme9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
	# CATheme1_anno, CATheme2_anno, CATheme3_anno, CATheme4_anno, CATheme5_anno = "0", "0", "0", "0", "0"
	# CATheme6_anno, CATheme7_anno, CATheme8_anno, CATheme9_anno = "0", "0", "0", "0"
	print(type(CAThemedays_list))
	for i in range(len(CAThemedays_list)):
		CATheme1 = 0
		CATheme1_anno = "0"
		CATheme2 = 0
		CATheme2_anno = "0"
		CATheme3 = 0
		CATheme3_anno = "0"
		CATheme4 = 0
		CATheme4_anno = "0"
		CATheme5 = 0
		CATheme5_anno = "0"
		CATheme6 = 0
		CATheme6_anno = "0"
		CATheme7 = 0
		CATheme7_anno = "0"
		CATheme8 = 0
		CATheme8_anno = "0"
		CATheme9 = 0
		CATheme9_anno = "0"
		date = CAThemedays_list[i]['_id']
		print("here")
		for elem in CAThemedays_list[i]['Themes']:
			if elem['First_theme'] == 'Braquage' or elem['Second_theme'] == 'Braquage':
				print("###################### Braquage ###################")
				CATheme1 += elem['CA']
				CATheme1_anno = numFormat.formatNumberMoney(CATheme1)
			if elem['First_theme'] == 'Stress' or elem['Second_theme'] == 'Stress':
				CATheme2 += elem['CA']
				CATheme2_anno = numFormat.formatNumberMoney(CATheme2)
			if elem['First_theme'] == 'Rapidité' or elem['Second_theme'] == 'Rapidité':
				CATheme3 += elem['CA']
				CATheme3_anno = numFormat.formatNumberMoney(CATheme3)
			if elem['First_theme'] == 'Mythologique' or elem['Second_theme'] == 'Mythologique':
				CATheme4 += elem['CA']
				CATheme4_anno = numFormat.formatNumberMoney(CATheme4)
			if elem['First_theme'] == 'Stratégie' or elem['Second_theme'] == 'Stratégie':
				CATheme5 += elem['CA']
				CATheme5_anno = numFormat.formatNumberMoney(CATheme5)
			if elem['First_theme'] == 'Psychologique' or elem['Second_theme'] == 'Psychologique':
				CATheme6 += elem['CA']
				CATheme6_anno = numFormat.formatNumberMoney(CATheme6)
			if elem['First_theme'] == 'Santé' or elem['Second_theme'] == 'Santé':
				CATheme7 += elem['CA']
				CATheme7_anno = numFormat.formatNumberMoney(CATheme7)
			if elem['First_theme'] == 'Amour' or elem['Second_theme'] == 'Amour':
				CATheme8 += elem['CA']
				CATheme8_anno = numFormat.formatNumberMoney(CATheme8)
			if elem['First_theme'] == 'Horreur' or elem['Second_theme'] == 'Horreur':
				CATheme9 += elem['CA']
				CATheme9_anno = numFormat.formatNumberMoney(CATheme9)
		CAThemeday = [
			date, 
			CATheme1, CATheme1_anno,
			CATheme2, CATheme2_anno,
			CATheme3, CATheme3_anno,
			CATheme4, CATheme4_anno,
			CATheme5, CATheme5_anno,
			CATheme6, CATheme6_anno,
			CATheme7, CATheme7_anno,
			CATheme8, CATheme8_anno,
			CATheme9, CATheme9_anno,
			]
		CAThemedays.append(CAThemeday)
	return JsonResponse(CAThemedays, safe=False) # http response


# Request Chart CA per Themes
def get_CA_Themes(request, *args, **kwargs):
	bookings_CAthemesF = requests.get('http://127.0.0.1:5000/cadThemeFirst/').text
	bookings_CAthemesS = requests.get('http://127.0.0.1:5000/cadThemeSecond/').text
	CAthemesF_list = json.loads(bookings_CAthemesF)
	CAthemesS_list = json.loads(bookings_CAthemesS)
	CAthemes = [
		['Thèmes', 'CA', {"role": "annotation"}]
		]

	for elem in CAthemesF_list:
		theme = elem['_id']['ThemeF']
		CA = elem['CA']
		CA_anno = numFormat.formatNumberMoney(CA)
		CAtheme = [theme, CA, CA_anno]
		CAthemes.append(CAtheme)

	for elem in CAthemesS_list:
		for i in range(len(CAthemes)):
			if elem['_id']['ThemeS'] == CAthemes[i][0]:
				CAthemes[i][1] = CAthemes[i][1] + elem['CA']
				CAthemes[i][2] = numFormat.formatNumberMoney(CAthemes[i][1])
	return JsonResponse(CAthemes, safe=False) # http response


# Request Chart CA per Themes
def get_Spect_Themes(request, *args, **kwargs):
	bookings_SpectthemesF = requests.get('http://127.0.0.1:5000/cadThemeFirst/').text
	bookings_SpectthemesS = requests.get('http://127.0.0.1:5000/cadThemeSecond/').text
	SpectthemesF_list = json.loads(bookings_SpectthemesF)
	SpectthemesS_list = json.loads(bookings_SpectthemesS)
	Spectthemes = [
		['Thèmes', 'Nombre de Spectateurs', {"role": "annotation"}]
		]

	for elem in SpectthemesF_list:
		theme = elem['_id']['ThemeF']
		Spect = elem['Nb_Spec']
		Spect_anno = numFormat.formatNumberMoney(Spect)
		Specttheme = [theme, Spect, Spect_anno]
		Spectthemes.append(Specttheme)

	for elem in SpectthemesS_list:
		for i in range(len(Spectthemes)):
			if elem['_id']['ThemeS'] == Spectthemes[i][0]:
				Spectthemes[i][1] = Spectthemes[i][1] + elem['Nb_Spec']
				Spectthemes[i][2] = numFormat.formatNumberMoney(Spectthemes[i][1])
	return JsonResponse(Spectthemes, safe=False) # http response


# Request Chart Points per Themes
def get_Points_Themes(request, *args, **kwargs):
	bookings_pointThemesF = requests.get('http://127.0.0.1:5000/ptRoomThemesF/').text
	bookings_pointThemesS = requests.get('http://127.0.0.1:5000/ptRoomThemesS/').text
	pointThemesF_list = json.loads(bookings_pointThemesF)
	pointThemesS_list = json.loads(bookings_pointThemesS)
	pointThemes = [
		['Salles', 'Thèmes', 'Points' , {"role": "annotation"}]
		]

	for elem in pointThemesF_list:
		room = elem['_id']['Salle']
		theme = elem['_id']['ThemeF']
		point = elem['Nb_Spec']*3
		point_anno = numFormat.formatNumberInt(point)
		pointTheme = [room, theme, point, point_anno]
		pointThemes.append(pointTheme)

	for elem in pointThemesS_list:
		room = elem['_id']['Salle']
		theme = elem['_id']['ThemeS']
		point = elem['Nb_Spec']
		point_anno = numFormat.formatNumberInt(point)
		pointTheme = [room, theme, point, point_anno]
		pointThemes.append(pointTheme)

	return JsonResponse(pointThemes, safe=False) # http response


