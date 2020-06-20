#importing modules
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates




def unique(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result


def casesToday(place,placeArray,caseArray):
        if place in placeArray:
            return casesOfPlaces[placesHaveCases.index(place)]
        else: 
            return 0    




#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')


# Declare arrays for each province
ontario = []
bc = []
pei = []
ns = []
nb = []
quebec = []
manitoba = []
saskatchewan = []
alberta = []
nfld = []
yukon = []
nt = []
nunavut = []
rt = []
canada = []

c = 0
numberOfRows = len(casesPerDay)
for date in dates:
    placesHaveCases = []
    casesOfPlaces = []
    for cpd in range(c,numberOfRows,1):
        if casesPerDay['date'][c] == date:
            placesHaveCases.append(casesPerDay['prname'][c].lower())
            casesOfPlaces.append(casesPerDay['numtotal'][c])
            c+=1
        else:
            break
    
    
    # Fill province arrays with total cases in respective provinces
    ontario.append(casesToday("ontario",placesHaveCases,casesOfPlaces))
    bc.append(casesToday("british columbia",placesHaveCases,casesOfPlaces))
    pei.append(casesToday("prince edward island",placesHaveCases,casesOfPlaces))
    ns.append(casesToday("nova scotia",placesHaveCases,casesOfPlaces))
    nb.append(casesToday("new brunswick",placesHaveCases,casesOfPlaces))
    quebec.append(casesToday("quebec",placesHaveCases,casesOfPlaces))
    manitoba.append(casesToday("manitoba",placesHaveCases,casesOfPlaces))
    saskatchewan.append(casesToday("saskatchewan",placesHaveCases,casesOfPlaces))
    alberta.append(casesToday("alberta",placesHaveCases,casesOfPlaces))
    nfld.append(casesToday("newfoundland and labrador",placesHaveCases,casesOfPlaces))
    yukon.append(casesToday("yukon",placesHaveCases,casesOfPlaces))
    nt.append(casesToday("northwest territories",placesHaveCases,casesOfPlaces))
    nunavut.append(casesToday("nunavut",placesHaveCases,casesOfPlaces))
    rt.append(casesToday("repatriated travellers",placesHaveCases,casesOfPlaces))
    canada.append(casesToday("canada",placesHaveCases,casesOfPlaces))
        
    placesHaveCases.clear()
    casesOfPlaces.clear()
