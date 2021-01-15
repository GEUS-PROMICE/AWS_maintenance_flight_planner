#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021 01 16

@author: Jason Box, GEUS.dk

"""
import os
import pandas as pd
import numpy as np
import geopy.distance

working_dir='/Users/jason/Dropbox/AWS/AWS_maintenance_flight_planner/' # change this in your local system
os.chdir(working_dir)

df= pd.read_csv('./planning_info/all_sites.csv')
df=df.drop(["Unnamed: 0"], axis=1)
# print(df.columns)


def inter_dist(A,B,start_time,stop_time):
    coords_1 = (float(df.lat[df.id==A]),float(df.lon[df.id==A]))
    coords_2 = (float(df.lat[df.id==B]),float(df.lon[df.id==B]))
    airspeed=150 # kts
    d=geopy.distance.distance(coords_1, coords_2).nm
    t=d/airspeed
    start_time+=t
    # print(df.name[df.id==A].aslist)
    # ,">",df.name[df.id==B])
    print(A+">"+B+",{:.0f}".format(d)+" nm,{:.2f}".format(t)+"h transit,"+
          "arrival time{:.1f}".format(start_time)+" nm, stop time "+str(stop_time)+
          "h,"+
          A+":{:.4f}".format(coords_1[0])+"N"+",{:.4f}".format(abs(coords_1[1]))+"W,"+
          B+":{:.4f}".format(coords_2[0])+"N"+",{:.4f}".format(abs(coords_2[1]))+"W"
          )
    start_time+=stop_time

    return start_time


day_counter=1

start_time=8.5
print();print("day "+str(day_counter)+", start_time: "+str(start_time))
start_time=inter_dist("AEY","KUS",start_time,1)
start_time=inter_dist("KUS","GOH",start_time,1)
day_counter+=1

print();print("weather delay, day "+str(day_counter))
day_counter+=1

start_time=8.5
print();print("day "+str(day_counter)+", start_time: "+str(start_time))
start_time=inter_dist("GOH","DY2",start_time,4.5)
start_time=inter_dist("DY2","SFJ",start_time,1)
day_counter+=1

start_time=8.5
print();print("day "+str(day_counter)+", start_time: "+str(start_time))
start_time=inter_dist("SFJ","SDL",start_time,0.7)
start_time=inter_dist("DY2","SDL",start_time,4.5)
start_time=inter_dist("SDL","SFJ",start_time,18)
day_counter+=1

start_time=8.5
print();print("day "+str(day_counter)+", start_time: "+str(start_time))
start_time=inter_dist("SFJ","CP1",start_time,4.5)
start_time=inter_dist("CP1","JAV",start_time,18)
day_counter+=1

print();print("weather delay, day "+str(day_counter))
day_counter+=1

start_time=8.
print();print("day "+str(day_counter)+", start_time: "+str(start_time))
start_time=inter_dist("JAV","DY2",start_time,0.6)
start_time=inter_dist("DY2","SDM",start_time,4.5)
start_time=inter_dist("SDM","UAK",start_time,18)
day_counter+=1

start_time=8.
print();print("day "+str(day_counter)+", start_time: "+str(start_time))
start_time=inter_dist("UAK","GOH",start_time,0.6)
day_counter+=1

start_time=8.
print();print("day "+str(day_counter)+", start_time: "+str(start_time))
start_time=inter_dist("GOH","NSE",start_time,4.5)
start_time=inter_dist("NSE","KUS",start_time,18)
day_counter+=1

