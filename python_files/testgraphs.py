import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import zipfile
#
#Graph numbers killed split by year
#
zf = zipfile.ZipFile('datasets/full_dataset_raw.csv.zip')

data = pd.read_csv(zf.open('stage3.csv'))
#split n_killed numbers based on year

kills_14 = 0
kills_15 = 0
kills_16 = 0
kills_17 = 0
kills_18 = 0
for date, kills in zip(data4["date"], data4["n_killed"]):
    if "2014" in date:
        kills_14 = kills_14 + kills
    if "2015" in date:
        kills_15 = kills_15 + kills
    if "2016" in date:
        kills_16 = kills_16 + kills
    if "2017" in date:
        kills_17 = kills_17 + kills
    if "2018" in date:
        kills_18 = kills_18 + kills
print(kills_14)
print(kills_15)
print(kills_16)
print(kills_17)
print(kills_18)

#instantiate x and y
objects = ('2014', '2015', '2016', '2017', '2018')
y_pos = np.arange(len(objects))
performance = [kills_14,kills_15,kills_16,kills_17,kills_18]

#plot graph
plt.bar(y_pos, performance, align='center', color='#20CA23')
plt.xticks(y_pos, objects)
plt.ylabel('Deaths')
plt.title('Deaths by year')
plt.show()

#
#Graph numbers injured split by year
#

#split n_injured numbers based on year
injured_14 = 0
injured_15 = 0
injured_16 = 0
injured_17 = 0
injured_18 = 0
for date, injured in zip(data4["date"], data4["n_injured"]):
    if "2014" in date:
        injured_14 = injured_14 + injured
    if "2015" in date:
        injured_15 = injured_15 + injured
    if "2016" in date:
        injured_16 = injured_16 + injured
    if "2017" in date:
        injured_17 = injured_17 + injured
    if "2018" in date:
        injured_18 = injured_18 + injured
print(injured_14)
print(injured_15)
print(injured_16)
print(injured_17)
print(injured_18)

#instantiate x and y
objects = ('2014', '2015', '2016', '2017', '2018')
y_pos = np.arange(len(objects))
performance = [injured_14,injured_15,injured_16,injured_17,injured_18]

#plot graph
plt.bar(y_pos, performance, align='center', color='#20CA23')
plt.xticks(y_pos, objects)
plt.ylabel('Injuries')
plt.title('Injuries by year')
plt.show()

#
# Graph that combines injured and killed numbers
#

n_groups = 5
killed = (kills_14, kills_15, kills_16, kills_17, kills_18)
injured = (injured_14, injured_15, injured_16, injured_17, injured_18)

# plot graph
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, killed, bar_width,
                 alpha=opacity,
                 color='#268328',
                 label='Killed')

rects2 = plt.bar(index + bar_width, injured, bar_width,
                 alpha=opacity,
                 color='#20CA23',
                 label='Injured')
plt.xlabel('Year')
plt.title('Kills and injuries by year')
plt.xticks(index + bar_width/2, ('2014', '2015', '2016', '2017', '2018'))

plt.legend()
plt.tight_layout()
plt.show()
fig = plt.figure()

#
# Graph gives number of times certain specific conditions apply to incidents
#

#instantiate x and y
objects = ('dead', 'murder', 'suicide', 'robbery', 'officer involved', 'drug involvement', 'home invasion', 'domestic violence')
y_pos = np.arange(len(objects))

#these numbers where given by earlier code written in preprocessing.py
performance = [53685,53281,53357,19495,17738, 16962, 10441, 6008]
plt.bar(y_pos, performance, align='center', color='#20CA23')
plt.xticks(y_pos, objects)
plt.title('Specifications gun violence')
fig.autofmt_xdate()
plt.show()

#
# Graph splits incidents by state
#

word_list = data4["state"]
from collections import Counter
words_to_count = (word for word in word_list if word[:1].isupper())
states = Counter(words_to_count)
#take top 10 states with most incidents
top_10 = (states.most_common(10))

states = []
numbers = []
for element in top_10:
    #add name of state and number of incidents to x and y respectively
    states.append(element[0])
    numbers.append(element[1])

#plot graph
fig = plt.figure()
y_pos = np.arange(len(states))
plt.bar(y_pos, numbers, align='center', color='#20CA23')
plt.xticks(y_pos, states)
plt.ylabel('Incidents')
plt.title('Incidents per state')
fig.autofmt_xdate()
plt.show()
