#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021 01 16

user inserts flight plan data below, start time, stop time, airport codes of starting and ending locations

outputs:
    .csv and Excel versions
    kml Google Earth lines between places
    
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

# ------------------------------------------------ start function to output kml for Google Earth
def output_kml(campaign,day_counter,A,B,C,D,cchoice)    :

    kml = simplekml.Kml(open=1)
    
    if ((C!="")&(D!="")):
        lin = kml.newlinestring(name="path", description="flight legs",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B])),
                            (float(df.lon[df.id==C]),float(df.lat[df.id==C])),
                            (float(df.lon[df.id==D]),float(df.lat[df.id==D]))
                            ]
                    )
        kml_ofile="./planning_info/kml/"+campaign+"_day"+str(day_counter)+"_"+A+"_to_"+B+"_to_"+C+"_to_"+D+".kml"

    if ((C!="")&(D=="")):
        lin = kml.newlinestring(name="path", description="flight legs",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B])),
                            (float(df.lon[df.id==C]),float(df.lat[df.id==C]))
                            ]
                    )
        kml_ofile="./planning_info/kml/"+campaign+"_day"+str(day_counter)+"_"+A+"_to_"+B+"_to_"+C+".kml"

    if ((B!="")&(C=="")&(D=="")):
        lin = kml.newlinestring(name="path", description="flight legs",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B]))
                            ]
                    )

        kml_ofile="./planning_info/kml/"+campaign+"_day"+str(day_counter)+"_"+A+"_to_"+B+".kml"

    lin.lookat.latitude = 72
    lin.lookat.longitude = -55
    lin.lookat.range = 3000000
    lin.lookat.heading = 0
    lin.lookat.tilt = 0

    lin.style.linestyle.color = cchoice
    lin.style.linestyle.width = 2  # 10 pixels
    # Create a linestring with two points (ie. a line)
    # linestring = kml.newlinestring(name="A Line")
    # linestring.coords = [(float(df.lon[df.id==A]),float(df.lat[df.id==A])),(float(df.lon[df.id==B]),float(df.lat[df.id==B]))]
    
    # Save the KML
    kml.save(kml_ofile)
# ------------------------------------------------ end function to output kml for Google Earth

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

# ------------------------------------------------ start function to output ASCII text lines to be read into dataframe
def inter_dist(start_time,day_counter,A,B,time,stop_time):
    coords_1 = (float(df.lat[df.id==A]),float(df.lon[df.id==A]))
    coords_2 = (float(df.lat[df.id==B]),float(df.lon[df.id==B]))
    airspeed=130 # kts
    d=geopy.distance.distance(coords_1, coords_2).nm
    t=d/airspeed
    time+=t
    BB=str(df.name[df.id==B].values)[2:-2]
    AA=str(df.name[df.id==A].values)[2:-2]
    print(BB)
    # print(df.name[df.id==A].aslist)
    # ,">",df.name[df.id==B])
    out_string=str(day_counter)+","+str(start_time)+\
        ","+A+","+B+",{:.0f}".format(d)+",{:.2f}".format(t)+","+ \
          "{:.1f}".format(time)+","+str(stop_time)+\
          ",{:.4f}".format(coords_1[0])+",{:.4f}".format(coords_1[1])+","+\
          "{:.4f}".format(coords_2[0])+",{:.4f}".format(coords_2[1])+","+\
              AA+","+BB
    # print(out_string)
    # print(out_
    out_concept.write(out_string+"\n")
    time+=stop_time

    return time
# ------------------------------------------------ end function to output ASCII text lines to be read into dataframe

campaign="Campaign_S_traverse_2021_Nordland"
# campaign="Campaign_NW_traverse_2021_Borek"

ofile="./planning_info/"+campaign
out_concept=open(ofile+".csv","w+")
out_concept.write('day,start time,from,to,distance nm,fly time,arrival time,stoppage time,from lat,from lon,destination lat,destination lon,start location name,landing location name\n')

# ------------------------------------------------ start define plan

if campaign=="Campaign_NW_traverse_2021_Borek":

    df.name[df.id=="POL"]
    day_counter=1
    start_time=8.5 ; time=start_time
    time=inter_dist(start_time,day_counter,"POL","THU",time,1)
    output_kml(campaign,day_counter,"POL","THU","","",red)
    day_counter+=1
    
    # ------------------------------------ artifical weather delay
    out_concept.write(str(day_counter)+', weather delay\n') ; day_counter+=1
    
    # 2 AWS on board; DY2 and CP1
    # add cargo mass = 150 kg / AWS
    # tools 50 kg
    # PAX = 3
    start_time=8.5
    time=inter_dist(start_time,day_counter,"THU","CEN",time,4.5)
    time=inter_dist(start_time,day_counter,"CEN","THU",time,18)
    output_kml(campaign,day_counter,"THU","CEN","THU","",red)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(start_time,day_counter,"THU","HUM",time,4.5)
    time=inter_dist(start_time,day_counter,"HUM","THU",time,18)
    output_kml(campaign,day_counter,"THU","HUM","THU","",aqua)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(start_time,day_counter,"THU","PET",time,4.5)
    time=inter_dist(start_time,day_counter,"PET","THU",time,18)
    output_kml(campaign,day_counter,"THU","PET","THU","",orange)
    day_counter+=1
    
    
    start_time=8.5
    time=inter_dist(start_time,day_counter,"THU","NEM",time,4.5)
    time=inter_dist(start_time,day_counter,"NEM","THU",time,18)
    output_kml(campaign,day_counter,"THU","NEM","THU","",blue)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(start_time,day_counter,"THU","POL",time,4.5)
    output_kml(campaign,day_counter,"THU","POL","","",black)
    day_counter+=1


if campaign=="Campaign_S_traverse_2021_Nordland":

    df.name[df.id=="AEY"]
    day_counter=1
    start_time=8.5 ; time=start_time
    time=inter_dist(start_time,day_counter,"AEY","KUS",time,1)
    time=inter_dist(start_time,day_counter,"KUS","GOH",time,18)
    output_kml(campaign,day_counter,"AEY","KUS","GOH","",red)
    day_counter+=1
    
    # ------------------------------------ artifical weather delay
    out_concept.write(str(day_counter)+', weather delay\n') ; day_counter+=1
    
    # 2 AWS on board; DY2 and CP1
    # add cargo mass = 150 kg / AWS
    # tools 50 kg
    # PAX = 3
    start_time=8.5
    time=inter_dist(start_time,day_counter,"GOH","DY2",time,4.5)
    time=inter_dist(start_time,day_counter,"DY2","SFJ",time,18)
    output_kml(campaign,day_counter,"GOH","DY2","SFJ","",aqua)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(start_time,day_counter,"SFJ","SDL",time,0.7)
    time=inter_dist(start_time,day_counter,"SDL","DY2",time,4.5)
    time=inter_dist(start_time,day_counter,"DY2","SFJ",time,18)
    output_kml(campaign,day_counter,"SFJ","SDL","DY2","SFJ",burlywood)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(start_time,day_counter,"SFJ","CP1",time,4.5)
    time=inter_dist(start_time,day_counter,"CP1","JAV",time,18)
    output_kml(campaign,day_counter,"SFJ","CP1","JAV","",blue)
    day_counter+=1
    
    # ------------------------------------ artifical weather delay
    out_concept.write(str(day_counter)+', weather delay\n') ; day_counter+=1
    
    start_time=8.
    time=inter_dist(start_time,day_counter,"JAV","DY2",time,0.6)
    time=inter_dist(start_time,day_counter,"DY2","SDM",time,4.5)
    time=inter_dist(start_time,day_counter,"SDM","UAK",time,18)
    output_kml(campaign,day_counter,"JAV","DY2","SDM","UAK",black)
    day_counter+=1
    
    start_time=8.
    time=inter_dist(start_time,day_counter,"UAK","GOH",time,0.6)
    output_kml(campaign,day_counter,"UAK","GOH","","",blueviolet)
    day_counter+=1
    
    start_time=8.
    time=inter_dist(start_time,day_counter,"GOH","NSE",time,4.5)
    time=inter_dist(start_time,day_counter,"NSE","KUS",time,18)
    output_kml(campaign,day_counter,"GOH","NSE","KUS","",orange)
    day_counter+=1


# ------------------------------------------------ end define plan

# close output file
out_concept.close()
os.system("cat "+ofile+".csv")

# write to csv
df2=pd.read_csv(ofile+".csv")
# df=df.reset_index(drop=True, inplace=True)

# write to Excel
df2.to_excel(ofile+".xlsx", index=False)
