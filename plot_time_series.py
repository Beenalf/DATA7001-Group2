# Group 2, DATA7001 2025

"""
This file plots a time series of medals won in each Olympic games for
a series of countries. Hosting years will be highlighted.

Summer and winter Olympic games will be plotted separately.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from countries import SUMMER_COUNTRIES, SUMMER_COUNTRIES_1970, WINTER_COUNTRIES_1970, SUMMER_GAMES, WINTER_GAMES # map of years -> host countries
from load_data import df_athletes, df_hosts, df_medals, df_results # pd dataframes
from initial_analysis import summerGameSlugs, winterGameSlugs, slugToCountry


def getMedalCounts(gameSlugs, startYear, endYear):
    """
    Return the medal counts for each country between startYear and endYear (inclusive)
    Use 'summer' to determine if the results should be for the summer or winter Olympics
    """
    gameSlugs = {year: slug for year, slug in gameSlugs.items() if startYear <= year <= endYear}

    df_filtered = df_results[
        (df_results["slug_game"].isin(gameSlugs.values())) &
        (df_results["medal_type"].notna())
    ]
    
    # Group by year and country to count medals (e.g, london-2012 as a row and United Kingdom as a column)
    medalCounts = df_filtered.groupby(['slug_game', 'country_name']).size().unstack(fill_value=0)

    # Sort medalCounts by year by 
    slug_to_year = {slug: year for year, slug in gameSlugs.items()}

    # Create a new column with years for sorting
    medalCounts["year"] = medalCounts.index.map(slug_to_year)

    # Sort by year, then remove the helper column
    medalCounts = medalCounts.sort_values("year")
    medalCounts = medalCounts.drop(columns="year")

    return medalCounts


def plotMedalTrends(medalCounts, hostDict, countries, title):
    """
    Plots the medal counts for each country listed
    """
    plt.figure(figsize=(14, 7))

    for country in countries:
        years = medalCounts.index
        counts = medalCounts.get(country, pd.Series([0]*len(years), index=years))
        
        is_host = [slugToCountry.get(year) == country for year in years]
        
        plt.plot(years, counts, label=country)
        plt.scatter(years[is_host], counts[is_host], color='red', zorder=5, label=None) # f"{country} (Host)" if any(is_host) else None

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Medal Count")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Year ranges
START_YEAR = 1970
END_YEAR = 2022

# Plot the medal counts
medalCountsSummer = getMedalCounts(summerGameSlugs, START_YEAR, END_YEAR)

# Prune out moscow-1980, the Soviet Union, and West Germany
medalCountsSummer = medalCountsSummer[medalCountsSummer.index != "moscow-1980"]
SUMMER_COUNTRIES_1970.remove("Soviet Union")
SUMMER_COUNTRIES_1970.remove("Federal Republic of Germany")
#print(f"Summeer medal count:\n{medalCountsSummer}\n")

plotMedalTrends(medalCountsSummer, summerGameSlugs, SUMMER_COUNTRIES_1970, "Summer Olympics Medal Counts")

medalCountsWinter = getMedalCounts(winterGameSlugs, START_YEAR, END_YEAR)

# Prune out Yugoslavia and Russia
WINTER_COUNTRIES_1970.remove("Yugoslavia")
WINTER_COUNTRIES_1970.remove("Olympic Athletes from Russia")

plotMedalTrends(medalCountsWinter, winterGameSlugs, WINTER_COUNTRIES_1970, "Winter Olympics Medal Counts")

