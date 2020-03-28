**Usage**
> pipenv install

> python main.py

Modify data/watchlist.json to change the countries that get plotted.

This script uses ECDC ncovid-19 data (March 28, 2020) to plot a country's reported ncovid-19 cases as a percentage of the country's population to explore the reported velocity at which the virus spreads through a country's population. Each country's plot is normalised to start at the date of a their first reported case.

![alt text](https://raw.githubusercontent.com/elodea/ncovid-19-case-pct-by-day/master/img/plot.png)

Almost all countries seem to experience the same exponential curve behaviour. For some countries, this curve is delayed which may just indicate a lag in test kit availability.

China's curve in particular is very strange and does not seem to follow the same trend that other countries within the same region experience. Even Singapore and South Korea, known for their good management of the pandemic, have experienced a typical exponential curve. This seems to lend to the idea that China's data is a bit suss.

Some countries seem to have beaten the curve completely i.e. Japan and Taiwan.
