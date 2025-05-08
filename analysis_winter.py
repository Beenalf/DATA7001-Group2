# Group 2, DATA7001 2025

"""
This file performs statistical analysis on the Olympic game
medal counts.

Summer and winter Olympic games will be analysed separately.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from countries import SUMMER_COUNTRIES, SUMMER_COUNTRIES_1970, WINTER_COUNTRIES_1970, SUMMER_GAMES, WINTER_GAMES # map of years -> host countries
from load_data import df_athletes, df_hosts, df_medals, df_results # pd dataframes
from initial_analysis import summerGameSlugs, winterGameSlugs, slugToCountry
from plot_time_series import medalCountsSummer, medalCountsWinter

medalCountsSummer = medalCountsSummer.loc[:, medalCountsSummer.columns.isin(SUMMER_COUNTRIES_1970)]
medalCountWinter = medalCountsWinter.loc[:, medalCountsWinter.columns.isin(WINTER_COUNTRIES_1970)]
#print(medalCountsSummer)
#print(medalCountsSummer.size)

medalCountsSummer = medalCountWinter

# Make a copy of the structure of the original DataFrame, filled with zeros
hostFlagsSummer = pd.DataFrame(0, index=medalCountsSummer.index, columns=medalCountsSummer.columns)

# Set '1' where the country hosted the games
for game_slug in medalCountsSummer.index:
    host_country = slugToCountry.get(game_slug)
    if host_country in medalCountsSummer.columns:
        hostFlagsSummer.loc[game_slug, host_country] = 1

# Reshape both DataFrames to long format
medals_long = medalCountsSummer.reset_index().melt(id_vars='slug_game', var_name='country_name', value_name='medal_count')
hosts_long = hostFlagsSummer.reset_index().melt(id_vars='slug_game', var_name='country_name', value_name='host_flag')

# Rename index to match
medals_long.rename(columns={'index': 'slug_game'}, inplace=True)
hosts_long.rename(columns={'index': 'slug_game'}, inplace=True)

# Merge them together
final_df = pd.merge(medals_long, hosts_long, on=['slug_game', 'country_name'])

#print(f"\n Dataframe info: {hostFlags.info()}.")
#print(f"\nfinal_df head: {final_df.head()}")
print(final_df)


hosted = final_df[final_df['host_flag'] == 1]['medal_count']
not_hosted = final_df[final_df['host_flag'] == 0]['medal_count']


from scipy.stats import ttest_ind, mannwhitneyu

# T-test (assumes normality)
t_stat, t_pval = ttest_ind(hosted, not_hosted, equal_var=False)

# Mann-Whitney U test (non-parametric)
u_stat, u_pval = mannwhitneyu(hosted, not_hosted, alternative='two-sided')

print(f"T-test p-value: {t_pval:.4f}")
print(f"Mann-Whitney U test p-value: {u_pval:.4f}")

if u_pval < 0.05:
    print("There is a statistically significant difference in medal counts for host countries.")
else:
    print("No statistically significant difference found for host countries.")


# Visualize
sns.boxplot(data=final_df, x='host_flag', y='medal_count')
plt.xticks([0, 1], ['Non-host Country', 'Host the Olympics'])
plt.title('Medal Count by Hosting Status (Winter)')
plt.show()