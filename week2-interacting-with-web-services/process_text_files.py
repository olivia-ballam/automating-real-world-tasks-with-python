#! /usr/bin/env python3

import os
import requests

def send_feedback_request(text_file, ip_address):


    # open and read text file 
    with open(text_file, 'r') as f:
        title = f.readline().strip()
        name = f.readline().strip()
        date = f.readline().strip()
        review = f.read().strip()

        # text file realine dictionary
        feedback = {"title": title, "name": name, "date": date, "feedback": review}

        try:
            response = requests.post(f"http://{ip_address}/feedback/", data=feedback)
        except Exception as e:
            print(f"ERROR: {e} unable to connect to server")


if __name__ == "__main__":

    path = "/data/feedback"
    text_files = os.listdir(path)

    ip_adress = "35.188.67.234"

    for text in text_files:

        send_feedback_request(text, ip_adress)

