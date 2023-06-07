import requests
from string import Template

def Api(firstCur, secondCur):
    api_key = "c6cfabe071361a4c3117e84f"
    api_url_template = Template('https://v6.exchangerate-api.com/v6/$key/pair/$firstCur/$secondCur')
    api_url = api_url_template.substitute(key = api_key, firstCur = firstCur, secondCur = secondCur)
    response = requests.get(api_url)
    #response.json
    return response.json()['conversion_rate']
    
#https://v6.exchangerate-api.com/v6/c6cfabe071361a4c3117e84f/pair/USD/EUR