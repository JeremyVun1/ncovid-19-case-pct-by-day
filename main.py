import json
from lib.logic import load_data, load_watchlist
from lib.plotter import plot_case_pct

ecdc_api = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
data = load_data(ecdc_api) # ECDC data

watchlist = load_watchlist('data/watchlist.json')

comparison_countries = ["China"] # baseline countries to compare to in all plots

# graph cases as a percentage of population by day since the first reported case
# for each of our regions - see watchlist.json
plot_case_pct(data, watchlist, comparison_countries)