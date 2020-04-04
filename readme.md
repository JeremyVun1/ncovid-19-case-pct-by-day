**Usage**
> pipenv install

**Static chart**
> python main.py

**Animated chart**
> python main.py -a

Modify data/watchlist.json to change the countries that get plotted. Add additional regions and countries if you want.

Configuration in config.ini. Monitor either "cases" or "deaths".

This script pulls the latest ECDC ncovid-19 data to plot a country's reported ncovid-19 cases as a percentage of the country's population and graphs the reported velocity at which the virus is spreading through said country's population. Plots are normalised to start at the date of a country's first reported case.

![alt text](https://raw.githubusercontent.com/elodea/ncovid-19-case-pct-by-day/master/img/screen.png)
https://opendata.ecdc.europa.eu/covid19/casedistribution/json/

Virtually all countries seem to experience the same exponential curve behaviour. For some countries, this curve is delayed which may just indicate a lag in test kit availability.

China's curve in particular is very strange and does not seem to follow the same trend that other countries within the same region experience. Even Singapore and South Korea, known for their good management of the pandemic, have experienced a typical exponential curve. This seems to lend to the idea that China's data is a bit suss.

Some countries seem to have beaten the curve completely i.e. Japan and Taiwan.
