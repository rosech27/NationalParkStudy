import pandas as pd
import matplotlib as plt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
s = (2748529490, 2855799410, 2813037690, 2789392160, 2827656820, 2736308950, 2928000820, 3072472520, 3309716890, 3308827510, 3182118330)
t = (2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='year', ylabel='annual visitors (million)',
       title='Yearly visitation for National Parks')
ax.grid()

fig.savefig("line.png")
plt.show()