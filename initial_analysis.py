# Group 2, DATA7001 2025

"""
Initial analysis of the datasets that we'll use in our report
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from countries import SUMMER_GAMES, WINTER_GAMES
from load_data import df_athletes, df_hosts, df_medals, df_results

# Create a map of years to game-slugs (name-year combinations)
summerGameSlugs = {
    2024: "paris-2024",
    2020: "tokyo-2020",
    2016: "rio-2016",
    2012: "london-2012",
    2008: "beijing-2008",
    2004: "athens-2004",
    2000: "sydney-2000",
    1996: "atlanta-1996",
    1992: "barcelona-1992",
    1988: "seoul-1988",
    1984: "los-angeles-1984",
    1980: "moscow-1980",
    1976: "montreal-1976",
    1972: "munich-1972",
    1968: "mexico-city-1968",
    1964: "tokyo-1964",
    1960: "rome-1960",
    1956: "melbourne-1956",
    1952: "helsinki-1952",
    1948: "london-1948",
    1936: "berlin-1936",
    1932: "los-angeles-1932",
    1928: "amsterdam-1928",
    1924: "paris-1924",
    1920: "antwerp-1920",
    1912: "stockholm-1912",
    1908: "london-1908",
    1904: "st-louis-1904",
    1900: "paris-1900",
    1896: "athens-1896"
}

winterGameSlugs = {
    2022: "beijing-2022",
    2018: "pyeongchang-2018",
    2014: "sochi-2014",
    2010: "vancouver-2010",
    2006: "turin-2006",
    2002: "salt-lake-city-2002",
    1998: "nagano-1998",
    1994: "lillehammer-1994",
    1992: "albertville-1992",
    1988: "calgary-1988",
    1984: "sarajevo-1984",
    1980: "lake-placid-1980",
    1976: "innsbruck-1976",
    1972: "sapporo-1972",
    1968: "grenoble-1968",
    1964: "innsbruck-1964",
    1960: "squaw-valley-1960",
    1956: "cortina-d-ampezzo-1956",
    1952: "oslo-1952",
    1948: "st-moritz-1948",
    1936: "garmisch-partenkirchen-1936",
    1932: "lake-placid-1932",
    1928: "st-moritz-1928",
    1924: "chamonix-1924"
}

slugToCountry = {
    "paris-2024": "France",
    "tokyo-2020": "Japan",
    "rio-2016": "Brazil",
    "london-2012": "Great Britain",
    "beijing-2008": "People's Republic of China",
    "athens-2004": "Greece",
    "sydney-2000": "Australia",
    "atlanta-1996": "United States of America",
    "barcelona-1992": "Spain",
    "seoul-1988": "Republic of Korea",
    "los-angeles-1984": "United States of America",
    "moscow-1980": "Soviet Union",
    "montreal-1976": "Canada",
    "munich-1972": "Federal Republic of Germany",
    "mexico-city-1968": "Mexico",
    "tokyo-1964": "Japan",
    "rome-1960": "Italy",
    "melbourne-1956": "Australia",
    "helsinki-1952": "Finland",
    "london-1948": "United Kingdom",
    "berlin-1936": "Germany",
    "los-angeles-1932": "United States",
    "amsterdam-1928": "Netherlands",
    "paris-1924": "France",
    "antwerp-1920": "Belgium",
    "stockholm-1912": "Sweden",
    "london-1908": "United Kingdom",
    "st-louis-1904": "United States",
    "paris-1900": "France",
    "athens-1896": "Greece",
    "beijing-2022": "People's Republic of China",
    "pyeongchang-2018": "Republic of Korea",
    "sochi-2014": "Olympic Athletes from Russia",
    "vancouver-2010": "Canada",
    "turin-2006": "Italy",
    "salt-lake-city-2002": "United States of America",
    "nagano-1998": "Japan",
    "lillehammer-1994": "Norway",
    "albertville-1992": "France",
    "calgary-1988": "Canada",
    "sarajevo-1984": "Yugoslavia",
    "lake-placid-1980": "United States of America",
    "innsbruck-1976": "Austria",
    "sapporo-1972": "Japan",
    "grenoble-1968": "France",
    "innsbruck-1964": "Austria",
    "squaw-valley-1960": "United States",
    "cortina-d-ampezzo-1956": "Italy",
    "oslo-1952": "Norway",
    "st-moritz-1948": "Switzerland",
    "garmisch-partenkirchen-1936": "Germany",
    "lake-placid-1932": "United States",
    "st-moritz-1928": "Switzerland",
    "chamonix-1924": "France"
}

#slugs = df_results[["slug_game"]].drop_duplicates()
#print(f"slugs: {slugs}\n")