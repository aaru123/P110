from random import random
import statistics
import csv
import pandas as pd
import random
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

mean = statistics.mean(data)
print('popularity mean :',mean)

meanlist = []

def randomNo(counter):
    data1 =[]
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        data1.append(value)
    mean1 = statistics.mean(data1)
    return mean1
  


def setup():
    for i in range(0,100):
    mean2 = randomNo(30)
    meanlist.append(mean2)
        
   
print(meanlist)

fig = ff.create_distplot([meanlist],['temp'], show_hist= False)
fig.show()

    