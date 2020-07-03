#!/usr/bin/env python3
"""Watcher tool used to upload to our API."""

import os
import sys
import requests
import json
from datetime import datetime

URL = "http://127.0.0.1:5000/reservation"


def send_json(json_file: str):
    with open("jsons/"+json_file) as js:
        json_data = json.load(js)

    headers = {'Content-type': 'application/json'}
    query_data = json.dumps(json_data)
    query = requests.post(URL, data=query_data, headers=headers)
    print(query.status_code)
    print(query.text)
    # check error
    # move to other dir according to error


def main():
    for json_file in os.listdir("jsons"):
        json_date = json_file.split('_')[0]
        now = datetime.now()
        current_date = now.strftime("%Y%m%d%H%M%S")

        if int(current_date) - 10 > int(json_date):
            print("sending {}".format(json_file))
            send_json(json_file)


if __name__ == '__main__':
    sys.exit(main())
