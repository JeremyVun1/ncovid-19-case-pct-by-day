**Usage**
> pipenv install

**Static chart**
> python main.py

**Show Animated chart**
> python main.py -a

**Render video out.avi**
> python main.py -o

Modify data/watchlist.json to change the countries that get plotted. Add additional regions and countries if you want.

Configuration in config.ini. Monitor either "cases" or "deaths".

This script pulls the latest ECDC ncovid-19 data to plot a country's reported ncovid-19 cases as a percentage of the country's population and graphs the reported velocity at which the virus is spreading through said country's population. Plots are normalised to start at the date of a country's first reported case unless you run the animated chart.

https://opendata.ecdc.europa.eu/covid19/casedistribution/json/

![alt text](https://raw.githubusercontent.com/elodea/ncovid-19-case-pct-by-day/master/img/screen.png)

![alt text](https://raw.githubusercontent.com/elodea/ncovid-19-case-pct-by-day/master/img/deaths.png)
