import json
import urllib.request
from .models import Country


# read data json file
def read_json_file(file_name):
    with open(file_name, 'r') as data_file:
        raw=data_file.read()

    return json.loads(raw)

def read_json_api(url):
    try:
        print(f"...requesting data from {url}")
        with urllib.request.urlopen(url) as request:
            result = json.loads(request.read().decode())
        
        print("data successfully fetched!")
        return result
    except:
        print("data could not be fetched, using local data")
        return read_json_file("../data/data.json")


# parse our data into domain models
def load_data(url):
    data = read_json_api(url)["records"]
    if len(data):
        date = data[0]["dateRep"]

    result = {}
    for item in data:
        cases = item["cases"]
        country_name = item["countriesAndTerritories"]
        pop = item["popData2018"]
        if country_name in result:
            result[country_name].add_cases(cases)
        else:
            result[country_name] = Country(country_name, pop, cases)

    # build our pct by day
    for k, v in result.items():
        result[k] = v.finalise()
    
    return result, date

def load_watchlist(file_name):
    result = {}
    
    for region in read_json_file(file_name):
        result[region["region"]] = region["countries"]

    return result
