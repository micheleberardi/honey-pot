#!/usr/bin/env python3

import sys
import argparse
from socket import socket, AF_INET, SOCK_STREAM
import requests
import datetime

VERSION = '0.1a'
welcome = b"Ubuntu 18.04.1 LTS\nserver login: "

datenow = datetime.datetime.now()
def slack_msg_error(msg):
    result_dict = ("*HONEY POT 🍯 PORT 23* \n" + "*MSG* " + str(msg) + "\n DATE: " + str(datenow))
    slack_report = {"attachments": [{"fallback": "*HONEY POT 🍯 PORT 22*", "color": "#ECB22E", "text": result_dict}]}
    webhook = 'https://hooks.slack.com/services/<TOKEN>'
    response = requests.post(webhook, json=slack_report, headers={'Content-Type': 'application/json'})
    if response.ok:
        json_data = response.text
        result = json_data
        return result
    else:

        return response.text


def send_email(src_address):
    """ Todo: send an email if we're scanned / probed on this port """
    pass


def honeypot(address, port=23):
    print("Starting honeypot on port {}".format(port))
    """ create a single Threaded telnet listen port """
    try:

        ski = socket(AF_INET, SOCK_STREAM)
        ski.bind((address, port))
        ski.listen()
        conn, addr = ski.accept()
        print('honeypot has been visited by ' + str(addr))
        data = 'honeypot has been visited by ' + str(addr)
        slack_msg_error(data)
        send_email(addr[0])
        conn.sendall(welcome)
        while True:
            data = conn.recv(1024)
            #slack_msg_error(data)
            print(data)
            #slack_msg_error(msg=data)
            if data == b'\r\n':
                slack_msg_error(data)
                #print(data)
                #ski.close()
                #sys.exit()
            elif data == b'':
                print(data)
                ski.close()
                sys.exit()
            else:
                print(data)
                slack_msg_error(data)
                #ski.close()
                #sys.exit()
    except Exception as e:
        print(e)
        ski.close()
        sys.exit()
        print(e)
        print("honeypot failed")
        ski.close()
        sys.exit()


if __name__ == '__main__':

    honeypot('0.0.0.0')
