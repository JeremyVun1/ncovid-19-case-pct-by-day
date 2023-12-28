import json
import requests
import configparser
from datetime import datetime, timedelta
from .models import Country


# read data json file
def read_json_file(file_name):
    print(f"...loading data from {file_name}")
    with open(file_name, 'r') as data_file:
        raw=data_file.read()

    return json.loads(raw)

def read_json_api(url):
    try:
        print(f"...requesting data from {url}")
        response = requests.get(url)
        result = response.json()
        
        print("data successfully fetched!")
        return result
    except Exception as e:
        print(e)
        print("data could not be fetched")
        return read_json_file("data/data.json")

def write_data(data, filename="data/data.json"):
    with open(filename, 'w') as file:
        json.dump(data, file)


# parse our data into domain models
def load_data(url, cached_date, trim_start=True, metric="cases"):
    cached_date = datetime.strptime(cached_date, "%d/%m/%Y").date()
    curr_date = (datetime.now() - timedelta(hours=10)).date()

    if cached_date < curr_date:
        data = read_json_api(url)["records"]
        write_data({"records": data})
        set_config("config", "cached_date", data[0]["dateRep"])
    else:
        data = read_json_file("data/data.json")
        data = data["records"]

    # get the date of the data
    if len(data):
        date = data[0]["dateRep"]
    
    start_date = datetime.strptime(date, "%d/%m/%Y").date()

    result = {}
    for item in data:
        cases = item[metric]
        country_name = item["countriesAndTerritories"]
        pop = item["popData2019"]

        item_date = datetime.strptime(item["dateRep"], "%d/%m/%Y").date()

        if country_name in result:
            result[country_name].add_cases(cases, item_date)
        else:
            result[country_name] = Country(country_name, pop, cases, item_date)
        
        start_date = item_date if item_date < start_date else start_date

    # build our pct by day
    for k, v in result.items():
        result[k] = v.finalise(start_date=start_date, trim_start=trim_start)
    
    return result, curr_date, start_date


def load_watchlist(file_name):
    result = {}
    
    for region in read_json_file(file_name):
        result[region["region"]] = region["countries"]

    return result


def load_config(filename, scope="config"):
    config = configparser.ConfigParser()
    config.read(filename)
    if scope in config:
        return config[scope]
    else:
        config[scope] = {
            "cached_date": "01/01/1901",
            "fps": 8,
            "metric": "cases"
        }
        with open(filename, 'w') as configfile:
            config.write(configfile)


def set_config(scope, config_prop, value, filename='config.ini'):
    with open(filename, 'r') as configfile:
        config = configparser.ConfigParser()
        config.read_file(configfile)
    
    with open(filename, 'w') as configfile:
        config[scope][config_prop] = value
        config.write(configfile)