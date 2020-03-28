import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20,10))

def create_subplot(plot_num, region):
    result = fig.add_subplot(plot_num)
    result.title.set_text(f"{region}")
    result.set_xlabel("Days")
    result.set_ylabel("%")
    return result

def plot_case_pct(data, regions, cmp_countries):
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

    plt.suptitle("confirmed cases as % of population since each countries first reported casepip")
    plt.show()