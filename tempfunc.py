import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")

data=df["reading_time"].tolist()

def random_set_mean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean = statistics.mean(data_set) 
    return mean

def show_fig(mean_list):
    df = mean_list
    df_mean = statistics.mean(df)

    fig = ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[df_mean,df_mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_mean(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean Of Reading Time Is:-",mean)

setup()

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean = random_set_mean(100) 
        mean_list.append(set_of_mean)

    std = statistics.stdev(mean_list)
    print("The standard deviation is:-", std)

standard_deviation()