import requests
from requests.auth import HTTPBasicAuth
import json
from keys import MpesaAccessToken,LipanaMpesaPpassword


def register_urls():
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode, #####in live production use Business_short_code
               "ResponseType": "Completed",
               "ConfirmationURL": "https://d3aabc302d08.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://d3aabc302d08.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)

    print(response.text)

#register_urls()


def simulate_c2b_transaction():
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
    "ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"1",
    "Msisdn":"254708374149",
    "BillRefNumber":"12345678"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
simulate_c2b_transaction()