import requests 
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from bson import ObjectId
from datetime import datetime

from . import numFormat, utilities


@login_required
def homepage(request):
    return render(request, 'homepage/homepage.html', {})


@login_required
def booking_list(request):
    """Render to display all 'Réservations'"""
    bookings_data = requests.get('http://127.0.0.1:5000/bookingList/').text
    bookings = json.loads(bookings_data)
    counter = 0
    for booking in bookings:
        num = {'Compteur': counter}
        price = booking['TotalPrice']
        price = float("{:.2f}".format(price))   
        total_price = {'TotalPrice': f'{price:.2f}' + " €"}
        booking_id = booking['_id']['$oid']
        new_booking_id = {'oid': booking_id}
        booking.update(total_price)
        booking.update(num)
        booking.update(new_booking_id)
        counter += 1
    # bookings = {k: v for k, v in sorted(bookings, key=lambda x: x['Compteur'])}

    first_date = utilities.first_date_bookings()
    last_date = utilities.last_date_bookings()
    return render(request, 'bookingList/booking_list.html', {
            'bookings': bookings,
            'first_date': first_date,
            'last_date': last_date
        })


@login_required
def booking_list_day(request):
    """Render to display daily 'Réservations'"""
    return render(request, 'bookingList/booking_list_day.html', {})


@login_required
def booking_detail(request, bookingId):
    """Render to display detail 'Réservation'"""
    booking_detail_tmp = requests.get('http://127.0.0.1:5000/bookingDetail/?bookingId='+bookingId).text
    booking_detail = json.loads(booking_detail_tmp)
    booking_datetime = ObjectId(bookingId).generation_time
    booking_date = datetime.strftime(booking_datetime, "%d/%m/%Y")
    return render(request, 'bookingList/booking_detail.html', {
            'booking_detail': booking_detail,
            'booking_date': booking_date
        })


@login_required
def dashboard360(request):
    """Render to display 'Dashboard360'"""
    first_date = utilities.first_date_bookings()
    last_date = utilities.last_date_bookings()
    return render(request, 'chart/dashboard360.html', {
            'first_date': first_date,
            'last_date': last_date
        })


@login_required
def get_CA_days(request, *args, **kwargs):
    """Request Chart CA per Days"""
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
    return JsonResponse(CAdays, safe=False)

 
@login_required
def get_Nb_Bookings(request, *args, **kwargs):
    """Request Chart Number of bookings per days"""
    bookings_NbBooks = requests.get('http://127.0.0.1:5000/nbBookingDays/').text
    NbBooks_list = json.loads(bookings_NbBooks)
    NbBooks = [
            [
                'Jour', 
                'Nombre de réservation', 
                {"role": "annotation"}, 
                'Nombre de spectateurs par réservations', 
                {"role": "annotation"}
            ]
        ]
    for i in reversed(range(len(NbBooks_list))):
        date = NbBooks_list[i]['_id']
        Nb_books = NbBooks_list[i]['Nb_Booking']
        Nb_books_anno = numFormat.formatNumberInt(Nb_books)
        M_spec = NbBooks_list[i]['Nb_Spec']/NbBooks_list[i]['Nb_Booking']
        M_spec_anno = numFormat.formatNumberFloat(M_spec)
        NbBook = [date, Nb_books, Nb_books_anno, M_spec, M_spec_anno]
        NbBooks.append(NbBook)
    return JsonResponse(NbBooks, safe=False)


@login_required
def get_Nb_Spectators(request, *args, **kwargs):
    """Request Chart Number of spectators per days"""
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
    return JsonResponse(NbSpects, safe=False) 


@login_required
def dashboard_rooms(request):
    """Render to display 'Détails Salles'"""
    first_date = utilities.first_date_bookings()
    last_date = utilities.last_date_bookings()
    return render(request, 'chart/dashboard_rooms.html', {
            'first_date': first_date,
            'last_date': last_date
        })


@login_required
def get_CA_Rooms_Days(request, *args, **kwargs):
    """Request Chart CA per Rooms and per Days"""
    bookings_CARoomdays = requests.get('http://127.0.0.1:5000/caRoomDays/').text
    CARoomdays_list = json.loads(bookings_CARoomdays)
    CARoomdays = [
        [
            'Jour',
            'Plus de PQ dans les toilettes',
            'Mariage sans alcool',
            'Interminable attente chez le medecin', 
            'Impot sur le revenu',
            'En plein dans la Friendzone',
            'Mon compte en banque en fin du mois',
            'Greve de la SNCF',
            'Diner de famille insoutenable',
            'Soutenance finale',
        ]
    ]
    for i in range(len(CARoomdays_list)):
        for elem in CARoomdays_list[i]['Rooms']:
            if elem['Room'] == 'Plus de PQ dans les toilettes':
                CARoom1 = elem['CA']
            elif elem['Room'] == 'Mariage sans alcool':
                CARoom2 = elem['CA']
            elif elem['Room'] == 'Interminable attente chez le medecin':
                CARoom3 = elem['CA']
            elif elem['Room'] == 'Impot sur le revenu':
                CARoom4 = elem['CA']
            elif elem['Room'] == 'En plein dans la Friendzone':
                CARoom5 = elem['CA']
            elif elem['Room'] == 'Mon compte en banque en fin du mois':
                CARoom6 = elem['CA']
            elif elem['Room'] == 'Greve de la SNCF':
                CARoom7 = elem['CA']
            elif elem['Room'] == 'Diner de famille insoutenable':
                CARoom8 = elem['CA']
            elif elem['Room'] == 'Soutenance finale':
                CARoom9 = elem['CA']
        date = CARoomdays_list[i]['_id']
        CARoomday = [
            date, 
            CARoom1,
            CARoom2,
            CARoom3,
            CARoom4,
            CARoom5,
            CARoom6,
            CARoom7,
            CARoom8,
            CARoom9,
            ]
        CARoomdays.append(CARoomday)
    return JsonResponse(CARoomdays, safe=False)


@login_required
def get_CA_Rooms(request, *args, **kwargs):
    """Request Chart CA per Days"""
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
    return JsonResponse(CArooms, safe=False)


@login_required
def get_Spect_Rooms(request, *args, **kwargs):
    """Request Chart CA per Days"""
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
    return JsonResponse(Spectrooms, safe=False)


@login_required
def dashboard_themes(request):
    """Render to display 'Détails Thèmes'"""
    bookings_pointThemesF = requests.get('http://127.0.0.1:5000/ptRoomThemesF/').text
    bookings_pointThemesS = requests.get('http://127.0.0.1:5000/ptRoomThemesS/').text
    pointThemesF_list = json.loads(bookings_pointThemesF)
    pointThemesS_list = json.loads(bookings_pointThemesS)
    pointThemes = []

    for elem in pointThemesF_list:
        theme = elem['_id']['ThemeF']
        point = elem['Nb_Spec']*3
        pointTheme = [theme, point]
        pointThemes.append(pointTheme)

    for elem in pointThemesS_list:
        for i in range(len(pointThemes)):
            if elem['_id']['ThemeS'] == pointThemes[i][0]:
                pointThemes[i][1] = pointThemes[i][1] + elem['Nb_Spec']
    sort_pointTheme = sorted(pointThemes, key=lambda theme: theme[1], reverse = True) 

    first_date = utilities.first_date_bookings()
    last_date = utilities.last_date_bookings()
    return render(request, 'chart/dashboard_themes.html', {
            'pointThemes': sort_pointTheme,
            'first_date': first_date,
            'last_date': last_date
        })


@login_required
def get_CA_Themes_Days(request, *args, **kwargs):
    """Request Chart CA per thems and per Days"""
    bookings_CAThemedays = requests.get('http://127.0.0.1:5000/caThemeDays/').text
    CAThemedays_list = json.loads(bookings_CAThemedays)
    CAThemedays = [
        [
            'Jour',
            'Braquage',
            'Stress',
            'Rapidité',
            'Mythologique',
            'Stratégie',
            'Psychologique',
            'Santé',
            'Amour',
            'Horreur',
        ]
    ]
    print(type(CAThemedays_list))
    for i in range(len(CAThemedays_list)):
        CATheme1 = 0
        CATheme2 = 0
        CATheme3 = 0
        CATheme4 = 0
        CATheme5 = 0
        CATheme6 = 0
        CATheme7 = 0
        CATheme8 = 0
        CATheme9 = 0
        date = CAThemedays_list[i]['_id']
        print("here")
        for elem in CAThemedays_list[i]['Themes']:
            if elem['First_theme'] == 'Braquage' or elem['Second_theme'] == 'Braquage':
                CATheme1 += elem['CA']
            if elem['First_theme'] == 'Stress' or elem['Second_theme'] == 'Stress':
                CATheme2 += elem['CA']
            if elem['First_theme'] == 'Rapidité' or elem['Second_theme'] == 'Rapidité':
                CATheme3 += elem['CA']
            if elem['First_theme'] == 'Mythologique' or elem['Second_theme'] == 'Mythologique':
                CATheme4 += elem['CA']
            if elem['First_theme'] == 'Stratégie' or elem['Second_theme'] == 'Stratégie':
                CATheme5 += elem['CA']
            if elem['First_theme'] == 'Psychologique' or elem['Second_theme'] == 'Psychologique':
                CATheme6 += elem['CA']
            if elem['First_theme'] == 'Santé' or elem['Second_theme'] == 'Santé':
                CATheme7 += elem['CA']
            if elem['First_theme'] == 'Amour' or elem['Second_theme'] == 'Amour':
                CATheme8 += elem['CA']
            if elem['First_theme'] == 'Horreur' or elem['Second_theme'] == 'Horreur':
                CATheme9 += elem['CA']
        CAThemeday = [
            date, 
            CATheme1,
            CATheme2,
            CATheme3,
            CATheme4,
            CATheme5,
            CATheme6,
            CATheme7,
            CATheme8,
            CATheme9,
            ]
        CAThemedays.append(CAThemeday)
    return JsonResponse(CAThemedays, safe=False)


@login_required
def get_CA_Themes(request, *args, **kwargs):
    """Request Chart CA per Themes"""
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
    return JsonResponse(CAthemes, safe=False)


@login_required
def get_Spect_Themes(request, *args, **kwargs):
    """Request Chart spectator per Themes"""
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
    return JsonResponse(Spectthemes, safe=False)


@login_required
def get_Points_Themes(request, *args, **kwargs):
    """Request Chart Points per Themes"""
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

    return JsonResponse(pointThemes, safe=False)


@login_required
def dashboard_client(request):
    """Render to display 'Détails Clients'"""
    first_date = utilities.first_date_bookings()
    last_date = utilities.last_date_bookings()
    return render(request, 'chart/dashboard_client.html', {
            'first_date': first_date,
            'last_date': last_date
        })


@login_required
def get_Cust_Split_Sex_Daily(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_splitSex = requests.get('http://127.0.0.1:5000/customer/civilities/daily').text
    splitSex_list = json.loads(bookings_splitSex)
    NbCustSplitSex = [
        ['Jour', 'Nombre d\'Hommes', {"role": "annotation"}, 'Nombre de Femmes', {"role": "annotation"}]
        ]

    for elem in splitSex_list:
        if elem['_id']['Civilite'] == "Monsieur":
            date = elem['_id']['date']
            nb_man = elem['total']
            for elem_n in splitSex_list:
                if date == elem_n['_id']['date'] and elem_n['_id']['Civilite'] == "Madame":
                    nb_woman = elem_n['total']
            NbCustSplitSex_tmp = [date, nb_man, nb_man, nb_woman, nb_woman]
            NbCustSplitSex.append(NbCustSplitSex_tmp)

    return JsonResponse(NbCustSplitSex, safe=False)


@login_required
def get_Cust_Split_Sex(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_splitSex = requests.get('http://127.0.0.1:5000/customer/civilities').text
    splitSex_list = json.loads(bookings_splitSex)
    NbCustSplitSex = [
        ['Civilité', 'Nombre', {"role": "annotation"}]
        ]

    for elem in splitSex_list:
        if elem['_id'] == "Monsieur":
            civilite = "Hommes"
        if elem['_id'] == "Madame":
            civilite = "Femmes"
        nb = elem['total']
        NbCustSplitSex_tmp = [civilite, nb, nb]
        NbCustSplitSex.append(NbCustSplitSex_tmp)

    return JsonResponse(NbCustSplitSex, safe=False)


@login_required
def get_Cust_Split_VR_Daily(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_splitVR = requests.get('http://127.0.0.1:5000/customer/version/daily').text
    splitVR_list = json.loads(bookings_splitVR)
    NbCustSplitVR = [
        ['Jour', 'Réservation Jeu avec VR', {"role": "annotation"}, 'Réservation Jeu sans VR', {"role": "annotation"}]
        ]

    for elem in splitVR_list:
        if elem['_id']['VR'] == "Oui":
            date = elem['_id']['date']
            nb_yes = elem['total']
            for elem_n in splitVR_list:
                if date == elem_n['_id']['date'] and elem_n['_id']['VR'] == "Non":
                    nb_no = elem_n['total']
            NbCustSplitVR_tmp = [date, nb_yes, nb_yes, nb_no, nb_no]
            NbCustSplitVR.append(NbCustSplitVR_tmp)

    return JsonResponse(NbCustSplitVR, safe=False)


@login_required
def get_Cust_Split_VR(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_splitVR = requests.get('http://127.0.0.1:5000/customer/version').text
    splitVR_list = json.loads(bookings_splitVR)
    NbCustSplitVR = [
        ['VR', 'Nombre', {"role": "annotation"}]
        ]

    for elem in splitVR_list:
        if elem['_id'] == "Oui":
            vr = "Réservation avec VR"
        if elem['_id'] == "Non":
            vr = "Réservation sans VR"
        nb = elem['total']
        NbCustSplitVR_tmp = [vr, nb, nb]
        NbCustSplitVR.append(NbCustSplitVR_tmp)

    return JsonResponse(NbCustSplitVR, safe=False)


@login_required
def get_Cust_Bookings_Hours(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_H_tmp = requests.get('http://127.0.0.1:5000/customer/bookings/hours').text
    bookings_Hours_list = json.loads(bookings_H_tmp)
    bookings_Hours = [
        ['Heures', 'Nombre de réservations', {"role": "annotation"}]
        ]

    for elem in bookings_Hours_list:
        hours = elem['_id']['hours'] + ":00"
        nb = elem['total']
        bookings_Hours_tmp = [hours, nb, nb]
        bookings_Hours.append(bookings_Hours_tmp)

    return JsonResponse(bookings_Hours, safe=False)


@login_required
def get_Cust_Game_Hours(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    Game_H_tmp = requests.get('http://127.0.0.1:5000/customer/game/hours').text
    Game_Hours_list = json.loads(Game_H_tmp)
    Game_Hours = [
        ['Heures', 'Nombre de réservations', {"role": "annotation"}]
        ]

    for elem in Game_Hours_list:
        hours = elem['_id']
        nb = elem['total']
        Game_Hours_tmp = [hours, nb, nb]
        Game_Hours.append(Game_Hours_tmp)

    return JsonResponse(Game_Hours, safe=False)


@login_required
def get_Cust_Split_Age(request, *args, **kwargs):
    """Request Chart Customer SPlit Age"""
    Split_A_tmp = requests.get('http://127.0.0.1:5000/customer/age').text
    Split_Age_list = json.loads(Split_A_tmp)
    Split_Age = [
        ['Age', 'Nombre d\'Acheteur', {"role": "annotation"}]
        ]
    print(Split_Age_list)
    for key, elem in Split_Age_list[0].items():
        if key != "_id":
            Age = key
            nb = elem
            Split_Age_tmp = [Age, nb, nb]
            Split_Age.append(Split_Age_tmp)

    return JsonResponse(Split_Age, safe=False)


@login_required
def get_Spect_Split_Sex_Daily(request, *args, **kwargs):
    """Request Spectator Split Sex Daily"""
    bookings_splitSex = requests.get('http://127.0.0.1:5000/spectator/civilities/daily').text
    splitSex_list = json.loads(bookings_splitSex)
    NbCustSplitSex = [
        ['Jour', 'Nombre d\'Hommes', {"role": "annotation"}, 'Nombre de Femmes', {"role": "annotation"}]
        ]

    nb_man = 0
    nb_woman = 0
    counter = 1
    current_date = None
    for elem in splitSex_list:
        if current_date == None:
            current_date = elem['date']
        if elem['date'] != current_date or counter == len(splitSex_list):
            NbCustSplitSex_tmp = [current_date, nb_man, nb_man, nb_woman, nb_woman]
            NbCustSplitSex.append(NbCustSplitSex_tmp)
            nb_man = 0
            nb_woman = 0
        current_date = elem['date']
        for resa in elem['Reservation']:
            if resa['Spectateur']['Civilite'] == "Monsieur": 
                nb_man += 1
            elif resa['Spectateur']['Civilite'] == "Madame":
                nb_woman += 1
        counter += 1

    return JsonResponse(NbCustSplitSex, safe=False)


@login_required
def get_Spect_Split_Sex(request, *args, **kwargs):
    """Request Chart Spectator Split Sex"""
    bookings_splitSex = requests.get('http://127.0.0.1:5000/spectator/civilities').text
    splitSex_list = json.loads(bookings_splitSex)
    NbCustSplitSex = [
        ['Civilité', 'Nombre', {"role": "annotation"}]
        ]

    nb_man = 0
    nb_woman = 0
    for elem in splitSex_list:
        for resa in elem['Reservation']:
            if resa['Spectateur']['Civilite'] == "Monsieur":
                man = "Hommes"
                nb_man += 1
            elif resa['Spectateur']['Civilite'] == "Madame":
                woman = "Femmes"
                nb_woman += 1
    NbCustSplitSex_tmp = [man, nb_man, nb_man]
    NbCustSplitSex.append(NbCustSplitSex_tmp)
    NbCustSplitSex_tmp = [woman, nb_woman, nb_woman]
    NbCustSplitSex.append(NbCustSplitSex_tmp)

    return JsonResponse(NbCustSplitSex, safe=False)


@login_required
def get_Spect_Split_VR_Daily(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_splitVR = requests.get('http://127.0.0.1:5000/spectator/version/daily').text
    splitVR_list = json.loads(bookings_splitVR)
    NbCustSplitVR = [
        ['Jour', 'Réservation Jeu avec VR', {"role": "annotation"}, 'Réservation Jeu sans VR', {"role": "annotation"}]
        ]

    for elem in splitVR_list:
        if elem['_id']['VR'] == "Oui":
            date = elem['_id']['date']
            nb_yes = elem['total']
            for elem_n in splitVR_list:
                if date == elem_n['_id']['date'] and elem_n['_id']['VR'] == "Non":
                    nb_no = elem_n['total']
            NbCustSplitVR_tmp = [date, nb_yes, nb_yes, nb_no, nb_no]
            NbCustSplitVR.append(NbCustSplitVR_tmp)

    return JsonResponse(NbCustSplitVR, safe=False)


@login_required
def get_Spect_Split_VR(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_splitVR = requests.get('http://127.0.0.1:5000/spectator/version').text
    splitVR_list = json.loads(bookings_splitVR)
    NbCustSplitVR = [
        ['VR', 'Nombre', {"role": "annotation"}]
        ]

    for elem in splitVR_list:
        if elem['_id'] == "Oui":
            vr = "Réservation avec VR"
        if elem['_id'] == "Non":
            vr = "Réservation sans VR"
        nb = elem['total']
        NbCustSplitVR_tmp = [vr, nb, nb]
        NbCustSplitVR.append(NbCustSplitVR_tmp)

    return JsonResponse(NbCustSplitVR, safe=False)


@login_required
def get_Spect_Bookings_Hours(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    bookings_H_tmp = requests.get('http://127.0.0.1:5000/spectator/bookings/hours').text
    bookings_Hours_list = json.loads(bookings_H_tmp)
    bookings_Hours = [
        ['Heures', 'Nombre de réservations', {"role": "annotation"}]
        ]

    for elem in bookings_Hours_list:
        hours = elem['_id']['hours'] + ":00"
        nb = elem['total']
        bookings_Hours_tmp = [hours, nb, nb]
        bookings_Hours.append(bookings_Hours_tmp)

    return JsonResponse(bookings_Hours, safe=False)


@login_required
def get_Spect_Game_Hours(request, *args, **kwargs):
    """Request Chart Points per Themes"""
    Game_H_tmp = requests.get('http://127.0.0.1:5000/spectator/game/hours').text
    Game_Hours_list = json.loads(Game_H_tmp)
    Game_Hours = [
        ['Heures', 'Nombre de réservations', {"role": "annotation"}]
        ]

    for elem in Game_Hours_list:
        hours = elem['_id']
        nb = elem['total']
        Game_Hours_tmp = [hours, nb, nb]
        Game_Hours.append(Game_Hours_tmp)

    return JsonResponse(Game_Hours, safe=False)


@login_required
def get_Spect_Split_Age(request, *args, **kwargs):
    """Request Chart Split Spectator Age"""
    Split_A_tmp = requests.get('http://127.0.0.1:5000/spectator/age').text
    Split_Age_list = json.loads(Split_A_tmp)
    Split_Age = [
        ['Age', 'Nombre de Spectateurs', {"role": "annotation"}]
        ]

    nb_0_18 = 0
    nb_18_25 = 0
    nb_25_39 = 0
    nb_40_54 = 0
    nb_55 = 0
    for elem in Split_Age_list:
        for resa in elem['Reservation']:
            if resa['Spectateur']['Age'] < 18:
                Spect_0_18 = "[0-18["
                nb_0_18 += 1
            if resa['Spectateur']['Age'] >= 18 and resa['Spectateur']['Age'] < 25:
                Spect_18_25 = "[18-25["
                nb_18_25 += 1
            if resa['Spectateur']['Age'] >= 25 and resa['Spectateur']['Age'] < 39:
                Spect_25_39 = "[25-39["
                nb_25_39 += 1
            if resa['Spectateur']['Age'] >= 40 and resa['Spectateur']['Age'] <= 54:
                Spect_40_54 = "[40-54]"
                nb_40_54 += 1
            if resa['Spectateur']['Age'] >= 55:
                Spect_55 = "[55 et plus"
                nb_55 += 1

    Split_Age_tmp = [Spect_0_18, nb_0_18, nb_0_18]
    Split_Age.append(Split_Age_tmp)
    Split_Age_tmp = [Spect_18_25, nb_18_25, nb_18_25]
    Split_Age.append(Split_Age_tmp)
    Split_Age_tmp = [Spect_25_39, nb_25_39, nb_25_39]
    Split_Age.append(Split_Age_tmp)
    Split_Age_tmp = [Spect_40_54, nb_40_54, nb_40_54]
    Split_Age.append(Split_Age_tmp)
    Split_Age_tmp = [Spect_55, nb_55, nb_55]
    Split_Age.append(Split_Age_tmp)

    return JsonResponse(Split_Age, safe=False)


@login_required
def data_extrator(request):
    """Render to display 'data extractor'"""
    return render(request, 'data/data_extractor.html', {})
# customer/bookings/hours