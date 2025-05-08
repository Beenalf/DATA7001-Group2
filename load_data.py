# Group 2, DATA7001 2025

"""
Loads and filters the data that will be used in the analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from countries import SUMMER_GAMES, WINTER_GAMES

#DATASET_PATH = "./data/through2016"
HOSTS_DATASET_PATH = "data/through2022/olympic_hosts.csv"
MEDALS_DATASET_PATH = "./data/through2022/olympic_medals.csv"
ATHLETES_DATASET_PATH = "./data/through2022/olympic_athletes.csv"
RESULTS_DATASET_PATH = "./data/through2022/olympic_results.csv"

PARIS_DATASET_PATH = "./data/paris2024/"

df_hosts = pd.read_csv(HOSTS_DATASET_PATH)
df_medals = pd.read_csv(MEDALS_DATASET_PATH)
df_athletes = pd.read_csv(ATHLETES_DATASET_PATH)
df_results = pd.read_csv(RESULTS_DATASET_PATH)

# Print out info about the datasets
# print(f"Hosts datasets:")
# print(df_hosts.head())
# print(df_hosts.info())

# print(f"\nMedals dataset:")
# print(df_medals.head())
# print(df_medals.info())

# print("\nthletes dataset:")
# print(df_athletes.head())
# print(df_athletes.info())

# print("\nResults dataset:")
# print(df_results.head())
# print(df_results.info())
