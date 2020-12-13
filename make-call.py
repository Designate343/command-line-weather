import requests
import json

BASE_URL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/"

def getApiKey():
    file_name = "config.json"
    with open(file_name) as f:
        data = json.load(f)
        return data["API_KEY"]

def makeCall(locationId):
    res = requests.get(BASE_URL + str(locationId) + "?res=3hourly&key=" + getApiKey())
    resJson = res.json()
    forecastPeriod = resJson['SiteRep']['DV']["Location"]['Period']
    for day in forecastPeriod:
        print (day['value'])
        hours = day['Rep']
        temperatures = []
        rainChance = []
        for hour in hours:
            temperatures.append( hour['T'])
            rainChance.append(hour['Pp'])
        print ('Temperatures:', temperatures)
        print ('Chance of rain:', rainChance)



makeCall(3529)