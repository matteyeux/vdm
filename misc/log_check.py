#!/usr/bin/env python3
import sys
import os
import smtplib, ssl
import configparser


def send_mail():
    config_path = os.getenv("HOME") + "/" + "vdm.conf"
    config = configparser.ConfigParser()
    config.read(config_path)

    sender_email = config['credentials']['mail']
    password = config['credentials']['password']
    receiver_email = "hauteb_m@etna-alternance.net"
    port = 465
    smtp_server = "smtp.gmail.com"
    message = """\
    Subject : VDM Report

    \n""" + open("mail.txt").read()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print(message)


def is_line_bad(line: str) -> bool:
    matches = ["POST", "GET", "PATCH", "PUT"]
    if any(x in line for x in matches):
        if int(line.split()[-2]) >= 400:
            return True
    return False


def main():
    # read file line by line
    with open("../api/vdm_error.log", "r") as log:
        lines = log.readlines()
        for line in lines:
            if is_line_bad(line) is True:
                open("mail.txt", 'a+').write(line)
        send_mail()


if __name__ == '__main__':
    sys.exit(main())
