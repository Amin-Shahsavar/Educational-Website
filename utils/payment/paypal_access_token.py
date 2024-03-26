from django.utils import timezone

import requests
from datetime import timedelta, datetime
from decouple import config


def get_paypal_accsess_token():
    client_id = config('PAYPAL_CLIENT_ID')
    client_secret = config("PAYPAL_CLIENT_SECRET")
    url = config('PAYPAL_ACSESS_TOKEN_URL')
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US",
    }
    data = {
        "grant_type": "client_credentials"
    }
    auth = (client_id, client_secret)

    try:
        response = requests.post(url, headers=headers, data=data, auth=auth)
        response.raise_for_status()
        access_token = response.json()["access_token"]
        return access_token
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print("Error:", str(e))
        return None

def calculate_remaining_time(created_at):
    remaining_time = created_at + timedelta(minutes=10) - datetime.now(timezone.utc)
    remaining_time = remaining_time - timedelta(microseconds=remaining_time.microseconds)
    formatted_time = (datetime.min + remaining_time).strftime("%M:%S")
    return formatted_time
