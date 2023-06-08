import requests
from string import Template
import os

def Api(firstCur, secondCur, year, month, day):

    api_key = "c6cfabe071361a4c3117e84f"
    #api_key = os.getenv('API_KEY')
    #print(api_key)
    api_url_template_now = Template('https://v6.exchangerate-api.com/v6/$key/pair/$firstCur/$secondCur')
    api_url_template_yesterday = Template('https://v6.exchangerate-api.com/v6/$key/history/$firstCur/$year/$month/$day')
    
    api_url_now = api_url_template_now.substitute(key = api_key, firstCur = firstCur, secondCur = secondCur)
    api_url_yesterday = api_url_template_yesterday.substitute(key = api_key, firstCur = firstCur, secondCur = secondCur, year = year, month = month, day = day)
    
    response_now = requests.get(api_url_now)
    response_yesterday = requests.get(api_url_yesterday)

    #print(response_yesterday.json()['conversion_rates'][str(secondCur)])
    
    if round(response_now.json()['conversion_rate'],2) >= round(response_yesterday.json()['conversion_rates'][str(secondCur)],2):
        return round(response_now.json()['conversion_rate'],2), True
    else:
        return round(response_now.json()['conversion_rate'],2), False
    
    # print(secondCur," ", type(response_yesterday.json()['conversion_rates'].get(secondCur)))
    # print(response_yesterday.json()['conversion_rates'].get(str(secondCur)))
    # return round(response_yesterday.json()['conversion_rates'][str(secondCur)],2), True
