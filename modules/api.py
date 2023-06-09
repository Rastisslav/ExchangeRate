import requests
from string import Template
import os
from dotenv import load_dotenv


def Api(firstCur, secondCur, year, month, day):

    load_dotenv()

    # ziskam api kluc ktory treba na pripojenie
    API_KEY = os.getenv('API_KEY')
    # dnesny exchangerate
    api_url_template_now = Template(
        'https://v6.exchangerate-api.com/v6/ \
         $key/pair/$firstCur/$secondCur')
    #vcerajsi exchangerate
    api_url_template_yesterday = Template(
        'https://v6.exchangerate-api.com/v6/ \
         $key/history/$firstCur/$year/$month/$day')

    api_url_now = api_url_template_now.substitute(
        key=API_KEY, firstCur=firstCur, secondCur=secondCur)
    api_url_yesterday = api_url_template_yesterday.substitute(
        key=API_KEY,
        firstCur=firstCur,
        secondCur=secondCur,
        year=year,
        month=month,
        day=day)

    response_now = requests.get(api_url_now)
    response_yesterday = requests.get(api_url_yesterday)

    # porovna ktory z nich je vacsi a posle naspat
    if round(response_now.json()['conversion_rate'], 2) >= round(
            response_yesterday.json()['conversion_rates'][str(secondCur)], 2):
        return round(response_now.json()['conversion_rate'], 2), True
    else:
        return round(response_now.json()['conversion_rate'], 2), False
