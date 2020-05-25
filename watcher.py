#!/usr/bin/env python3
"""Watcher tool used to upload to our API."""

import os 
import sys
from datetime import datetime


def send_json():
    # send post request
    # check error
    # move to other dir according to error


def main():
    for json in os.listdir("jsons"):
        json_date = json.split('_')[0]
        now = datetime.now()
        current_date = now.strftime("%Y%m%d%H%M%S")
        
        if int(current_date) - 100000000 > int(json_date):
            print("post request")

if __name__ == '__main__':
    sys.exit(main())
