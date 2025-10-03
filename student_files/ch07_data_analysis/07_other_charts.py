import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure(figsize=(12, 6), facecolor='#fff5ff')

cities = ['Colorado Springs', 'Phoenix', 'Raleigh', 'Milwaukee', 'Seattle']
cities_abbr = ['COS', 'PHX', 'RDU', 'MKE', 'SEA']
elevations = [6172, 1132, 437, 723, 429]
populations = [431000, 1488000, 423000, 599000, 634000]
median_age = [34.5, 32.8, 32.8, 31.1, 36.1]
median_income = [53550, 46601, 55170, 35186, 70172]
median_house = [205600, 162300, 202800, 113900, 436600]

# chart 1 - pie
sub1 = figure.add_subplot(221)
sub1.pie(populations,
         labels=cities,
         colors=['#ffccee', '#fdef2e', '#23c78a', '#a0b055', '#5623a8'],
         explode=[0, 0.2, 0, 0, 0],
         autopct='%1.1f%%',
         shadow=True, startangle=45)
sub1.set_title('Populations')

# chart 2 - horizontal bar
sub2 = figure.add_subplot(222)
bar_height = 0.8
y_ticks = np.arange(len(cities))
sub2.barh(y_ticks, median_age, height=bar_height, align='center', color='#ff559e')
sub2.set_yticks(y_ticks)                        # define the tick marks on y-axis
sub2.set_xlim((31, 37))                         # limit the x-axis value range
sub2.set_yticklabels(cities_abbr)               # city abbreviation instead of numbers
sub2.set_title('Median Age')

for loc, age in enumerate(median_age):
    sub2.annotate(str(age), xy=(median_age[loc], loc),
                  xycoords='data', xytext=(+5, -5),
                  textcoords='offset points', fontsize=14)

# chart 3 - grouped bars
sub3 = figure.add_subplot(2, 2, (3, 4))
bar_width = 0.35
x_ticks = np.arange(len(cities))
sub3.bar(x_ticks, median_income, width=bar_width, color='#634170')
sub3.set_xticks(x_ticks + bar_width)
sub3.set_xticklabels(cities)
sub3.set_ylim(30000, 80000)
sub3.set_title('Income and Housing Costs')
sub3.legend(['Income'], loc='upper left', frameon=False)
sub3b = sub3.twinx()                            # create a second bar axis on the right-side
sub3b.bar(x_ticks + bar_width, median_house, width=bar_width, color='#a2b79e')
sub3b.set_ylim(100000, 500000)
sub3b.set_yticks(np.arange(100000, 600000, 100000))
sub3b.set_yticklabels(['100k', '200k', '300k', '400k', '500k'])
sub3b.legend(['Housing'], loc='upper right', frameon=False)

plt.show()
