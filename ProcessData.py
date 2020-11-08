from pathlib import Path
import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def extract_material_data(columns_wanted):
    """
    Extract data on brewing material data over time

    Args:
        columns_wanted: a list of columns of data you want to be extracted

    Returns:
        List of lists in in the format
        [list_of_years,[list_of_percent_data1,etc],[list_of_lbs_data1,etc]]
    """
    material_percent_lists = []
    material_total = []
    for col in columns_wanted:
        years = []
        material_percents = []
        material_amount = []
        for year in range(2008, 2015, 1):
            file = Path("ExtractedCSV/Materials{0}.csv".format(year))
            data = pd.read_csv(file, names=["Material(lbs)", "Current Month",
                                            "Prior Month",
                                            "Current Year Cumulative",
                                            "Prior Year Cumulative"])
            years.append(year)
            current_material = int(
                data["Current Year Cumulative"][col].replace(",", ""))
            material_amount.append(current_material)
            # divide weight of material by total weight and
            # multiply by 100 to get a percent
            material_percent = current_material / \
                int(data["Current Year Cumulative"][11].replace(",", "")) * 100
            material_percents.append(material_percent)
        material_percent_lists.append(material_percents)
        material_total.append(material_amount)
    return [years, material_percent_lists, material_total]


def extract_num_of_breweries():
    """
    Extract data on breweries over time

    Returns:
        List of lists in in the format
        [list_of_years,list_of_number_of_breweries]
    """
    years = []
    breweries = []
    for year in range(2008, 2015, 1):
        sum_micros = 0
        file_name = Path("ExtractedCSV/NumBrewers{0}.csv".format(year))
        data = pd.read_csv(file_name)
        data = data.drop(columns=["Unnamed: 2"])
        years.append(year)
        for col in range(8, 11, 1):
            if year == 2010:
                sum_micros = 0
                for col in range(7, 10, 1):
                    sum_micros += int(data["Number of Breweries (1)"]
                                      [col].replace(",", ""))
            else:
                sum_micros += int(data["Number of Breweries (1)"]
                                  [col].replace(",", ""))
        breweries.append(sum_micros)
    return [years, breweries]


def extract_hop_data(hop_headings):
    """
    Extract data on brewing material data over time

    Args:
        hop_headings: a list of data wanted
                    gets called using headings from dataframe

    Returns:
        List of lists in in the format
        [list_of_years,[list_of_data1,list_of_data2,etc]]
    """
    cumulative_data = []
    for things in hop_headings:
        years = []
        current_hop_set = []
        for year in range(2008, 2020, 1):
            # no data was reported in 2013
            if year == 2013:
                continue
            file_name = Path("ExtractedCSV/Hops{0}.csv".format(year))
            data = pd.read_csv(file_name)
            years.append(year)
            # fixes imported number that have commas in the middle
            if "," in str(data[things][2]):
                num = data[things][2].replace(",", "")
                current_hop_set.append(float(num))
            elif "." in str(data[things][2]):
                current_hop_set.append(float(data[things][2]))
        cumulative_data.append(current_hop_set)
    return [years, cumulative_data]


def plot_microbreweries_and_hop_concentration():
    """
    create dual axis plots of data with hop concentration and
    number of microbreweries over time
    """
    mat_data = extract_material_data([0, 7])
    brewery_data = extract_num_of_breweries()
    fig, ax1 = plt.subplots()
    fig.suptitle(
        'Fig 1: Microbreweries and Concentration of Hops in Beer over Time')
    ax1.set_xlabel('year')
    ax1.set_ylabel("breweries")
    years = brewery_data[0]
    breweries = brewery_data[1]
    ax1.plot(years, breweries, "grey")
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()
    ax2.set_xlabel('year')
    ax2.set_ylabel("Concentration of Hops (%)")
    years = mat_data[0]
    hop_percent = mat_data[1][1]
    plt.plot(years, hop_percent, "g")
    ax2.tick_params(axis='y')

    green = mpatches.Patch(color='green', label='Hops')
    grey = mpatches.Patch(color='grey', label='Breweries')
    plt.legend(handles=[grey, green])

    plt.show()


def plot_hop_production_consumption():
    """
    create plot of production of hops and brewery consuption of hops over time
    """
    hop_data = extract_hop_data(["$ per lb avg", "production"])
    mat_data = extract_material_data([0, 7])
    fig, ax1 = plt.subplots()
    fig.suptitle('Fig 2: Hop Production and Hop usage over Time')
    ax1.set_xlabel('year')
    ax1.set_ylabel("Hops (lbs)")
    years = mat_data[0]
    hops_lbs = mat_data[2][1]
    plt.plot(years, hops_lbs, "g")
    years = hop_data[0]
    hop_production = hop_data[1][1]
    # multiply by 1000 because the units of the data
    # downloaded were scaled down by 1000
    hop_production = [x * 1000 for x in hop_production]
    plt.plot(years, hop_production, "grey")
    ax1.tick_params(axis='y')

    green = mpatches.Patch(color='green', label='Hop use by Breweries')
    grey = mpatches.Patch(color='grey', label='Hop Production')
    plt.legend(handles=[grey, green])

    plt.show()


def plot_hop_price():
    """
    create plot of hop price over time
    """
    hop_data = extract_hop_data(["$ per lb avg", "production"])
    fig, ax1 = plt.subplots()
    fig.suptitle('Fig 3: Hop Price over Time')
    ax1.set_xlabel('year')
    ax1.set_ylabel("Hop Price ($)")
    years = hop_data[0]
    hop_price = hop_data[1][0]
    plt.plot(years, hop_price, "green")
    ax1.tick_params(axis='y')
    plt.show()
