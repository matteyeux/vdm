#!/usr/bin/env python3
"""Watcher tool used to upload to our API."""

import os
import sys
import requests
import json
from datetime import datetime
from pathlib import Path

URL = "http://127.0.0.1:5000/reservation"
BOOKING_DIR = "../generate_booking/jsons/"


def send_json(json_file: str):
    with open(BOOKING_DIR + json_file) as js:
        json_data = json.load(js)

    headers = {'Content-type': 'application/json'}
    query_data = json.dumps(json_data)
    query = requests.post(URL, data=query_data, headers=headers)
    if query.status_code == 201:
        os.rename(BOOKING_DIR + json_file, "processed/" + json_file)
    else:
        os.rename(BOOKING_DIR + json_file, "failed/" + json_file)


def main():
    Path("processed").mkdir(parents=True, exist_ok=True)
    Path("failed").mkdir(parents=True, exist_ok=True)
    for json_file in os.listdir(BOOKING_DIR):
        json_date = json_file.split('_')[0]
        now = datetime.now()
        current_date = now.strftime("%Y%m%d%H%M%S")

        if int(current_date) - 10 > int(json_date):
            print("sending {}".format(json_file))
            send_json(json_file)


if __name__ == '__main__':
    sys.exit(main())
