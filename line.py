from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#logic in this cell scrapes the data, cleans it up and put it in a dataframe called new_df

tables = pd.read_html("https://www.nps.gov/aboutus/visitation-numbers.htm")
visit = tables[2]
new_df = pd.DataFrame([{"Year":"","Visitors":""}])
new_df.head()
# create a list to store the year values
years = []
# create a list to store the visitor values
visitors = []

visit

# iterate over every row in the data
for index, row in visit.iterrows():
    # iterate over every column in the row
    for i in range(0,row.size):
        # if the column position is divisible by 2
        if i % 2 == 0:
            # add to year list
            years.append(row[i])
        else:
            # else add to visitor list
            visitors.append(str(row[i]).replace(".",""))

#years
new_df = pd.DataFrame(years, visitors).reset_index()
new_df.dropna(inplace=True)
new_df.info()



new_df = new_df[new_df['index']!='nan']
# new_df = new_df.rename(columns={"index":"Visitors", 0:"Year"})
# new_df["Visitors"] = pd.to_numeric(new_df["Visitors"])

new_df.info()

new_df

new_df = new_df.rename(columns={"index":"Visitors", 0:"Year" })
new_df.head()

new_df = new_df[new_df.Year != "Total"]
#df.drop('reports', axis=1)
#df[df.name != 'Tina']

new_df["Visitors"]=pd.to_numeric(new_df["Visitors"])
new_df["Year"]=pd.to_numeric(new_df["Year"])

new_df = new_df.sort_values(by=['Year'])
# Data for plotting last 10 years of Visitor Attendance
s = (2748529490, 2855799410, 2813037690, 2789392160, 2827656820, 2736308950, 2928000820, 3072472520, 3309716890, 3308827510, 3182118330)
t = (2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='year', ylabel='annual visitors (million)',
       title='Yearly visitation for National Parks')
ax.grid()

fig.savefig("line.png")
plt.show()