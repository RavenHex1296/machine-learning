import sys
import pandas as pd 
import numpy as np

sys.path.append('src')

df = pd.read_csv("dsu_fall23_tech_app_dataset.csv") 

# Question 1
# print(df[df.Race_Wins == df.Race_Wins.max()])
'''
Question 2
countries = list(df.Country.unique())
champions_count = {}

for country in countries:
    champions_count[country] = 0

for index, row in df.iterrows():
    if row['Has_Won_A_Championship']:
        champions_count[row['Country']] += 1

print(sorted(champions_count.items(), key=lambda x:x[1]))
'''

'''
Question 3
df = df.drop(df[(df.Total_Races < 5)].index)

names = list(df.Driver.unique())
race_win_proportions = {}

for index, row in df.iterrows():
    race_win_proportions[row["Driver"]] = row["Race_Wins"] / row["Total_Races"]

print(sorted(race_win_proportions.items(), key=lambda x:x[1]))
'''
'''
Question 4
names = list(df.Driver.unique())
season_num = {}

for index, row in df.iterrows():
    season_num[row["Driver"]] = len(str(df.Seasons[index]).split(", "))

print(sorted(season_num.items(), key=lambda x:x[1]))
'''
