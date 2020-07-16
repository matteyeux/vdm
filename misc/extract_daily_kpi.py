"""Convert KPI daily report to CSV."""

import csv, json, sys
import requests
from datetime import date

response = requests.get("http://localhost:5000/extractKPIDaily/")
data = json.loads(response.text)

filename = str(date.today()) + "_extractKPIDaily.csv"
with open(filename, 'w') as f:
    output = csv.writer(f)
    output.writerow(data[0].keys())

    for row in data:
        output.writerow(row.values())
print("[i] report saved to {}".format(filename))
