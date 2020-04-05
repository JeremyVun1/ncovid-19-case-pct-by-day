from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FormatStrFormatter
import numpy as np

from lib.models import Axis_range
from lib.utility import enforce_int
from lib.renderer import render_graph_anim

fig = plt.figure(figsize=(20,10))

def create_subplot(plot_num, region):
    result = fig.add_subplot(plot_num)
    result.title.set_text(f"{region}")
    result.set_xlabel("Days")
    result.set_ylabel("%")
    result.yaxis.set_major_formatter(FormatStrFormatter('%.5f'))
    return result


def plot_case_pct(data, regions, cmp_countries, date, metric):
    plot_num = 221

    for region in regions:
        subplot = create_subplot(plot_num, region)

        countries = regions[region]
        countries = list(dict.fromkeys(cmp_countries + countries)) # remove duplicates
        for country in countries:
            if country in data:
                y = data[country].pct
                x = list(range(1, len(y) + 1))
                subplot.plot(x, y, label=country)
            
        subplot.legend()
        plot_num = plot_num + 1

    plt.suptitle(f"{date} \n {metric} as % of population since each countries first reported case")
    plt.show()


def get_all_countries(regions, cmp_countries, data):
    country_list = cmp_countries
    for region in regions:
        country_list = country_list + regions[region]

    country_list = list(dict.fromkeys(country_list)) # remove duplicates

    result = {}
    for c in country_list:
        if c in data:
            result[c] = data[c]

    return result


def get_max_n(data):
    result = 0

    for country in data:
        data_points = len(data[country].pct)
        if result < data_points:
            result = data_points

    return result


def create_lines(countries, subplot):
    result = {}
    for c in countries:
        result[c] = subplot.plot([], [])[0]
    
    return result


def clear_texts(texts):
    for text in texts:
        text.set_text("")


def plot_case_pct_anim(data, regions, cmp_countries, start_date, fps, metric, render=False):
    print("...plotting frames")
    fps = enforce_int(fps)
    countries = get_all_countries(regions, cmp_countries, data)
    max_n = get_max_n(data)

    subplot = create_subplot(111, 'all')

    lines = create_lines(countries, subplot)
    texts = []

    x_range = Axis_range(max_padding_pct=0.15)
    y_range = Axis_range(max_padding_pct=0.3)
    for i in range(0, max_n - 1):
        clear_texts(texts)

        for c in countries:
            if i < (len(countries[c].pct)-1):
                line = lines[c]
                x_data = np.append(line.get_xdata(), i)
                y_data = np.append(line.get_ydata(), countries[c].pct[i])
                line.set_xdata(x_data)
                line.set_ydata(y_data)
                texts.append(plt.text(i, countries[c].pct[i], c))

                # update the axis ranges
                x_range.set_max(i)
                y_range.set_max(countries[c].pct[i])
        
        plt.xlim(x_range.get_min(), 1 if x_range.get_max() == 0 else x_range.get_max())
        plt.ylim(y_range.get_min(), y_range.get_max())
        plt.suptitle(f"{start_date.strftime('%d-%m-%Y')} \n {metric} as % of population since each countries first reported case")

        if render:
            plt.savefig(f"img/anim/{start_date}")
        else:
            plt.pause(1/(fps*2))

        start_date = start_date + timedelta(days=1)

    if render:
        render_graph_anim(fps, target=f'{start_date}.avi')
    else:
        plt.show()