import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(18, 9), subplot_kw=dict(aspect="equal"))

recipe = ["2920249 Alaska_Region",
          "55770379 Intermountain_Region",
          "21807708 Midwest_Region",
          "54174137 National Capital_Region",
          "57039300 Northeast_Region",
          "63329468 Pacific West_Region",
          "63170592 Southeast_Region"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} )".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Regions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=12, weight="bold")

ax.set_title("2018 NPS Attendance: By Region")
fig.savefig("pie.png")
plt.show()