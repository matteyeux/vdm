import requests 
import json
# from django.http import JsonResponse
from bson import ObjectId
from datetime import datetime


def first_date_bookings():
    bookings_first_tmp = requests.get('http://127.0.0.1:5000/firstDate/').text
    bookings_first = json.loads(bookings_first_tmp)
    bookings_first_id = bookings_first[0]['_id']['$oid']
    first_datetime = ObjectId(bookings_first_id).generation_time
    first_date = datetime.strftime(first_datetime, "%d/%m/%Y")
    return first_date


def last_date_bookings():
    bookings_last_tmp = requests.get('http://127.0.0.1:5000/lastDate/').text
    bookings_last = json.loads(bookings_last_tmp)
    bookings_last_id = bookings_last[0]['_id']['$oid']
    last_datetime = ObjectId(bookings_last_id).generation_time
    last_date = datetime.strftime(last_datetime, "%d/%m/%Y")
    return last_date