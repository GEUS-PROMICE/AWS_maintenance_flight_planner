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
import simplekml

working_dir="/Users/jason/Dropbox/AWS/AWS_maintenance_flight_planner/" # change this in your local system
os.chdir(working_dir)

df= pd.read_csv("./planning_info/all_sites.csv")
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
    out_string=A+">"+B+",{:.0f}".format(d)+" nm,{:.2f}".format(t)+"h transit,"+ \
          "arrival time{:.1f}".format(start_time)+" nm, stop time "+str(stop_time)+\
          "h,"+A+":{:.4f}".format(coords_1[0])+"N"+",{:.4f}".format(abs(coords_1[1]))+"W,"+\
          B+":{:.4f}".format(coords_2[0])+"N"+",{:.4f}".format(abs(coords_2[1]))+"W"
    # print(out_string)
    out_concept.write(out_string+"\n")
    start_time+=stop_time

    return start_time

def day_start(day_counter,start_time):
    out_string="day "+str(day_counter)+", start_time: "+str(start_time)
    out_concept.write(out_string+"\n")

def output_kml(day_counter,A,B,C,D,cchoice)    :

    kml = simplekml.Kml(open=1)
    
    if ((C!="")&(D!="")):
        lin = kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B])),
                            (float(df.lon[df.id==C]),float(df.lat[df.id==C])),
                            (float(df.lon[df.id==D]),float(df.lat[df.id==D]))
                            ]
                    )
        ofile="./planning_info/day"+str(day_counter)+"_"+A+"_to_"+B+"_to_"+C+"_to_"+D+".kml"

    if ((C!="")&(D=="")):
        lin = kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B])),
                            (float(df.lon[df.id==C]),float(df.lat[df.id==C]))
                            ]
                    )
        ofile="./planning_info/day"+str(day_counter)+"_"+A+"_to_"+B+"_to_"+C+".kml"

    if ((B!="")&(C=="")&(D=="")):
        lin = kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B]))
                            ]
                    )

        ofile="./planning_info/day"+str(day_counter)+"_"+A+"_to_"+B+".kml"

    lin.lookat.latitude = float(df.lat[df.id==A])
    lin.lookat.longitude = float(df.lon[df.id==A])
    lin.lookat.range = 3000000
    lin.lookat.heading = 56
    lin.lookat.tilt = 0

    lin.style.linestyle.color = cchoice
    lin.style.linestyle.width = 2  # 10 pixels
    # Create a linestring with two points (ie. a line)
    # linestring = kml.newlinestring(name="A Line")
    # linestring.coords = [(float(df.lon[df.id==A]),float(df.lat[df.id==A])),(float(df.lon[df.id==B]),float(df.lat[df.id==B]))]
    
    # Save the KML
    kml.save(ofile)

campaign="S_traverse_2021_v1"""
ofile="./planning_info"+campaign+".csv"
out_concept=open(ofile,"w+")


red = 'ff0000ff'
antiquewhite = 'ffd7ebfa'
aqua = 'ffffff00'
aquamarine = 'ffd4ff7f'
orange = 'ff00a5ff'
bisque = 'ffc4e4ff'
black = 'ff000000'
blanchedalmond = 'ffcdebff'
blue = 'ffff0000'
blueviolet = 'ffe22b8a'
brown = 'ff2a2aa5'
burlywood = 'ff87b8de'
cadetblue = 'ffa09e5f'

# -------------------------------------- start set plan

day_counter=1
start_time=8.5
day_start(day_counter,start_time)
start_time=inter_dist("AEY","KUS",start_time,1)
start_time=inter_dist("KUS","GOH",start_time,1)
output_kml(day_counter,"AEY","KUS","GOH","",red)
day_counter+=1

print();print("weather delay, day "+str(day_counter))
day_counter+=1

start_time=8.5
day_start(day_counter,start_time)
start_time=inter_dist("GOH","DY2",start_time,4.5)
start_time=inter_dist("DY2","SFJ",start_time,1)
output_kml(day_counter,"GOH","DY2","SFJ","",aqua)
day_counter+=1

start_time=8.5
day_start(day_counter,start_time)
start_time=inter_dist("SFJ","SDL",start_time,0.7)
start_time=inter_dist("SDL","DY2",start_time,4.5)
start_time=inter_dist("DY2","SFJ",start_time,18)
output_kml(day_counter,"SFJ","SDL","DY2","SFJ",burlywood)
day_counter+=1


start_time=8.5
day_start(day_counter,start_time)
start_time=inter_dist("SFJ","CP1",start_time,4.5)
start_time=inter_dist("CP1","JAV",start_time,18)
output_kml(day_counter,"SFJ","CP1","JAV","",blue)
day_counter+=1

print();print("weather delay, day "+str(day_counter))
day_counter+=1

start_time=8.
day_start(day_counter,start_time)
start_time=inter_dist("JAV","DY2",start_time,0.6)
start_time=inter_dist("DY2","SDM",start_time,4.5)
start_time=inter_dist("SDM","UAK",start_time,18)
output_kml(day_counter,"JAV","DY2","SDM","UAK",black)
day_counter+=1

start_time=8.
day_start(day_counter,start_time)
start_time=inter_dist("UAK","GOH",start_time,0.6)
output_kml(day_counter,"UAK","GOH","","",blueviolet)
day_counter+=1

start_time=8.
day_start(day_counter,start_time)
start_time=inter_dist("GOH","NSE",start_time,4.5)
start_time=inter_dist("NSE","KUS",start_time,18)
output_kml(day_counter,"GOH","NSE","KUS","",orange)
day_counter+=1

# -------------------------------------- end set plan
out_concept.close()
os.system("cat "+ofile)

