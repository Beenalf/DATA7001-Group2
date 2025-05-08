# Group 2, DATA7001 2025

"""
Tests for normality in the summer and winter medal counts
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from countries import SUMMER_COUNTRIES, SUMMER_COUNTRIES_1970, WINTER_COUNTRIES_1970, SUMMER_GAMES, WINTER_GAMES # map of years -> host countries
from load_data import df_athletes, df_hosts, df_medals, df_results # pd dataframes
from initial_analysis import summerGameSlugs, winterGameSlugs, slugToCountry
from plot_time_series import medalCountsSummer, medalCountsWinter
from analysis_winter import final_df



sns.histplot(final_df['medal_count'], bins=30, kde=True)
plt.title("Distribution of Medal Counts")
plt.xlabel("Medal Count")
plt.ylabel("Frequency")
plt.show()

from scipy.stats import shapiro

stat, p = shapiro(final_df['medal_count'])
print(f"Shapiro-Wilk p-value: {p:.4f}")