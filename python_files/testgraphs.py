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

# Comments: 
# Grafiek 1, Deaths by year:
# Er is duidelijk een stijgende lijn te zien in de doden per jaar van 2014 tot 2017.
# Er is weinig te zeggen over 2018, doordat er alleen data is van de eerste paar maanden. 
# 
# Grafiek 2, Injured by year: Eenzelfde stijgende lijn als in grafiek 1 is hier ook zichtbaar.
# 
# Grafiek 3, grafiek 1 en 2 in een grafiek: Als de grafieken met elkaar vergeleken worden,
# wordt duidelijk dat de verhouding doden/gewonden ongeveer gelijk blijft, zo'n 1:2.
# 
# Grafiek 4, aantallen specificaties: In de dataset is aanvullende informatie gegeven
# over specifieke incidenten. Deze zijn ingedeeld in een aantal vaste woorden die het vaakst voorkomen.
# 
# Grafiek 5, incidenten per staat: Hier zijn de top 10 landen met meeste incidenten aangegeven.
# Interessant om hier te onderzoeken is waarom illinois en california bijvoorbeeld specifiek zo
# zo veel incidenten hebben, komt dat door inwonersaantallen of zijn er andere elementen die meespelen?
#

allstates = []
allnumbers = []

for element in all_states:
    allstates.append(element[0])
    allnumbers.append(element[1])

#searched up data of population of individual states
d ={'California': 39144818,
'Texas': 27469114,
'Florida':20271272,
'New York': 19795791,
'Illinois':12859995,
'Pennsylvania':12802503,
'Ohio':11613423,
'Georgia':10214860,
'North Carolina':10042802,
'Michigan':9922576,
'New Jersey':8958013,
'Virginia':8382993,
'Washington':7170351,
'Arizona':6828065,
'Massachusetts':6794422,
'Indiana':6619680,
'Tennessee':6600299,
'Missouri':6083672,
'Maryland':6006401,
'Wisconsin':5771337,
'Minnesota':5489594,
'Colorado':5456574,
'South Carolina':4896146,
'Alabama':4858979,
'Louisiana':4670724,
'Kentucky':4425092,
'Oregon':4028977,
'Oklahoma':3911338,
'Connecticut':3590886,
'Iowa':3123899,
'Utah':2995919,
'Mississippi':2992333,
'Arkansas':2978204,
'Kansas':2911641,
'Nevada':2890845,
'New Mexico':2085109,
'Nebraska':1896190,
'West Virginia':1844128,
'Idaho':1654930,
'Hawaii':1431603,
'New Hampshire':1330608,
'Maine':1329328,
'Rhode Island':1056298,
'Montana':1032949,
'Delaware':945934,
'South Dakota':858469,
'North Dakota':756927,
'Alaska':738432,
'Vermont':626042,
'Wyoming':586107,
'District of Columbia': 693972}

population = []
#couple amount of incidents of state to population of state
for x in allstates:
    for y in d:
        if x == y:
            population.append(d[y])

#plot graph
x = population
y = allnumbers
plt.scatter(x,y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.show()

# Waarnemingen: Het plotten van de grafiek geeft niet heel duidelijke resultaten.
# De staten met de meeste incidenten zijn vrijwel uitsluitend grote staten, maar hier zijn wel veel verschillen in. 
# Zo is illinois met 12859995 een stuk lager qua inwonersaantal dan california met 39144818, maar illinois heeft meer incidenten.

print("Starting reading data...")
data = pd.read_excel('datasets/MASTER_DATASET.xlsx')


#
# Incidenten per maand
# 

jan = 0
feb = 0
mar= 0
apr = 0
mei = 0
jun = 0
jul = 0
aug = 0
sep = 0
okt = 0
nov = 0
dec = 0
for date in data["date"]:
    date = str(date)
    if "01" in date:
        jan = jan+1
    if "02" in date:
        feb = feb+1
    if "03" in date:
        mar = mar+1
    if "04" in date:
        apr = apr+1
    if "05" in date:
        mei = mei+1
    if "06" in date:
        jun = jun+1
    if "07" in date:
        jul=jul+1
    if "08" in date:
        aug=aug+1
    if "09" in date:
        sep=sep+1
    if "10" in date:
        okt=okt+1
    if "11" in date:
        nov=nov+1
    if "12" in date:
        dec=dec+1

        
#plot graph 
fig = plt.figure()
objects = ('jan','feb','mar','apr','mei','jun','jul','aug','sep','okt','nov','dec')
y_pos = np.arange(len(objects))
performance = [jan, feb, mar, apr, mei, jun, jul, aug, sep, okt, nov, dec]
print(performance)
print(sum(performance))
plt.bar(y_pos, performance, align='center', color='#20CA23')
plt.xticks(y_pos, objects)
plt.title('Incidenten per maand')
plt.show()


#Incidenten per maand
#
#Meeste incidenten vinden plaats in januari en maart. Hierna zijn de hoogste waarden juist in de zomer(juli en augustus) en zijn december en november het laagste. 
#Wintermaanden kan misschien verklaard worden met de natuurlijke associatie van het koude weer met depressie, 
#Algemeen wordt hierdoor veronderstelt dat er meer zelfmoorden/zelfmoordpogingen in de winter zijn. Februari is hierbij
#waarschijnlijk lager omdat deze maand een paar dagen korter is.
#Deze incidenten zijn echter niet uitsluitend suicide-situaties, dus het is moeilijk te zeggen in hoeverre dit van toepassing is.


jan_killed = 0
feb_killed = 0
mar_killed= 0
apr_killed = 0
mei_killed = 0
jun_killed = 0
jul_killed = 0
aug_killed = 0
sep_killed = 0
okt_killed = 0
nov_killed = 0
dec_killed = 0

jan_injured = 0
feb_injured = 0
mar_injured= 0
apr_injured = 0
mei_injured = 0
jun_injured = 0
jul_injured = 0
aug_injured = 0
sep_injured = 0
okt_injured = 0
nov_injured = 0
dec_injured = 0

for date, killed, injured in zip(data["date"], data["n_killed"], data["n_injured"]):
    date = str(date)
    if "01" in date:
        jan_killed = jan_killed+killed
        jan_injured = jan_injured+injured
    if "02" in date:
        feb_killed = feb_killed+killed
        feb_injured = feb_injured+injured
    if "03" in date:
        mar_killed = mar_killed+killed
        mar_injured = mar_injured+injured
    if "04" in date:
        apr_killed = apr_killed+killed
        apr_injured = apr_injured+injured
    if "05" in date:
        mei_killed = mei_killed+killed
        mei_injured = mei_injured+injured
    if "06" in date:
        jun_killed = jun_killed+killed
        jun_injured= jun_injured+injured
    if "07" in date:
        jul_killed=jul_killed+killed
        jul_injured = jul_injured+injured
    if "08" in date:
        aug_killed=aug_killed+killed
        aug_injured = aug_injured+injured
    if "09" in date:
        sep_killed=sep_killed+killed
        sep_injured = sep_injured+injured
    if "10" in date:
        okt_killed=okt_killed+killed
        okt_injured = okt_injured+injured
    if "11" in date:
        nov_killed=nov_killed+killed
        nov_injured = nov_injured+injured
    if "12" in date:
        dec_killed=dec_killed+killed
        dec_injured = dec_injured+injured
        

        
#plot graph
n_groups = 12
killed = (jan_killed, feb_killed, mar_killed, apr_killed, mei_killed,jun_killed,jul_killed, aug_killed, sep_killed, okt_killed, nov_killed, dec_killed)
injured = (jan_injured, feb_injured, mar_injured, apr_injured, mei_injured, jun_injured, jul_injured, aug_injured, sep_injured, okt_injured, nov_injured, dec_injured )
print(killed)
print(injured)
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
plt.title('Kills and injuries by month')
plt.xticks(index + bar_width/2, ('jan','feb','mar','apr','mei','jun','jul','aug','sep','okt','nov','dec'))
plt.legend()
 
plt.tight_layout()
plt.show()


#Kills/Injuries per maand
#
#Opvallend andere indeling dan aantal incidenten. Hoogste waarden bij kills zijn januari en maart, waarbij de laagste
#waarde april is. Hoogste waarden bij injuries zijn juli, januari en augustus die allen dicht bij elkaar zitten,
#met als laagste waarden februari. Wat opvalt hierbij is dat de verhouding van doden en gewonden verschild per maand, 
# februari is het laagste in gewonden, maar zit in de top 5 bij doden. 