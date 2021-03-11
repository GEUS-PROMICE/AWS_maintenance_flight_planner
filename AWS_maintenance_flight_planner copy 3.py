#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021 01 16

user inserts flight plan data below, start time, stop time, airport codes of starting and ending locations

code depends on inputs (airport coordinates, names) that are output from positions_combine_PROMICE_GCN_Airports.py

outputs:
    .csv and Excel versions
    kml Google Earth lines between places
    
@author: Jason Box, GEUS.dk

"""
import os
import pandas as pd
import geopy.distance
import simplekml
import datetime
from datetime import date
import calendar

global cost_per_li,airspeed,fuel_remaining,hourly_rate,N_crew,cost_per_day_person
cost_per_li=10.14 #DKK per liter, Fuel price at Summit has just been estimated at around 30 DKK/litre
fuel_remaining=1400#liters https://www.vikingair.com/twin-otter-information/technical-description
airspeed=140 # kts Twin Otter
# airspeed=105 # kts Helicopter
N_crew=3
cost_per_day_person=2.5 # kDKK, hotel 2k, food 0.5k

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
        # pnt = kml.newpoint(name=str(df.name[df.id==A].values)[2:-2])
        # pnt.coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
        #                     (float(df.lon[df.id==B]),float(df.lat[df.id==B])),
        #                     (float(df.lon[df.id==C]),float(df.lat[df.id==C])),
        #                     (float(df.lon[df.id==D]),float(df.lat[df.id==D]))
        #                     ]
        # pnt.style.labelstyle.color = simplekml.Color.red  # Make the text red
        # pnt.style.labelstyle.scale = 1.5  # text scaling multiplier
        # pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
        # pnt.altitudemode = simplekml.AltitudeMode.relativetoground
        # pnt.camera.latitude=float(df.lat[df.id==A])
        # pnt.camera.longitude=float(df.lat[df.id==A])
        # pnt.camera.altitude=4e5
        # pnt.camera.tilt = 0

        kml_ofile="./planning_info/kml/"+campaign+"_day"+str(day_counter)+"_"+A+"_to_"+B+"_to_"+C+"_to_"+D+".kml"

    if ((C!="")&(D=="")):
        lin = kml.newlinestring(name="path", description="flight legs",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B])),
                            (float(df.lon[df.id==C]),float(df.lat[df.id==C]))
                            ]
                    )
        # pnt = kml.newpoint(name=str(df.name[df.id==A].values)[2:-2])
        # pnt.coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
        #                     (float(df.lon[df.id==B]),float(df.lat[df.id==B])),
        #                     (float(df.lon[df.id==C]),float(df.lat[df.id==C]))
        #                     ]
        # pnt.style.labelstyle.color = simplekml.Color.red  # Make the text red
        # pnt.style.labelstyle.scale = 1.5  # text scaling multiplier
        # pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
        # pnt.altitudemode = simplekml.AltitudeMode.relativetoground
        # pnt.camera.latitude=float(df.lat[df.id==A])
        # pnt.camera.longitude=float(df.lat[df.id==A])
        # pnt.camera.altitude=4e5
        # pnt.camera.tilt = 0

        kml_ofile="./planning_info/kml/"+campaign+"_day"+str(day_counter)+"_"+A+"_to_"+B+"_to_"+C+".kml"

    if ((B!="")&(C=="")&(D=="")):
        lin = kml.newlinestring(name="path", description="flight legs",
                    coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
                            (float(df.lon[df.id==B]),float(df.lat[df.id==B]))
                            ]
                    )
        # pnt = kml.newpoint(name=str(df.name[df.id==A].values)[2:-2])
        # pnt.coords=[(float(df.lon[df.id==A]),float(df.lat[df.id==A])),
        #                     (float(df.lon[df.id==B]),float(df.lat[df.id==B]))
        #                     ]
        # pnt.style.labelstyle.color = simplekml.Color.red  # Make the text red
        # pnt.style.labelstyle.scale = 1.5  # text scaling multiplier
        # pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
        # pnt.altitudemode = simplekml.AltitudeMode.relativetoground
        # pnt.camera.latitude=float(df.lat[df.id==A])
        # pnt.camera.longitude=float(df.lat[df.id==A])
        # pnt.camera.altitude=4e5
        # pnt.camera.tilt = 0

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
def inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,A,B,time,stop_time,cargo_mass,N_PAX,fly_time):
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    coords_1 = (float(df.lat[df.id==A]),float(df.lon[df.id==A]))
    coords_2 = (float(df.lat[df.id==B]),float(df.lon[df.id==B]))
    fuel_use_rate=400 #l/h
    d=geopy.distance.distance(coords_1, coords_2).nm
    t=d/airspeed
    fly_time+=t # total fly time before taxi time
    t+=2*12/60 # circling, taxi at start and end
    time+=t
    fuel_use+=fuel_use_rate*fly_time
    fuel_remaining-=fuel_use_rate*d/airspeed
    fuel_cost=fuel_use*cost_per_li
    BB=str(df.name[df.id==B].values)[2:-2]
    AA=str(df.name[df.id==A].values)[2:-2]
    # print(BB)
    # print(df.name[df.id==A].aslist)
    # ,">",df.name[df.id==B])
    stop_time_string=str(stop_time)
    if stop_time==18:stop_time_string="end of flying"
    out_string=str(date)+","\
        +str(day_name)+","\
        +str(day_counter)+","\
        +str(start_time)+\
        ","+A+","+B+","\
        +str(cargo_mass)+","\
        +str(N_PAX)+","\
        "{:.0f}".format(d)+","+\
        "{:.1f}".format(t)+","+\
        "{:.0f}".format(fuel_use)+","+\
        "{:.0f}".format(fuel_cost/1000)+","+\
        "{:.0f}".format(fuel_remaining)+","+\
          "{:.1f}".format(time)+","+stop_time_string+","+\
          "{:.4f}".format(coords_1[0])+",{:.4f}".format(coords_1[1])+","+\
          "{:.4f}".format(coords_2[0])+",{:.4f}".format(coords_2[1])+","+\
              AA+","+BB+","+\
            str(airspeed)+","+\
            work
    print(out_string)
    # print(out_
    out_concept.write(out_string+"\n")
    time+=stop_time

    return time,fly_time,fuel_use,fuel_remaining
# ------------------------------------------------ end function to output ASCII text lines to be read into dataframe

# ------------------------------------------------ start function
def weather_day(day_counter,date):
    out_concept.write(str(day_counter)+'. weather delay\n')
    day_counter+=1
    date+=datetime.timedelta(days=1)
    
    return day_counter,date
# ------------------------------------------------ end function

# ------------------------------------------------ campaigns
# campaign="S_chartering_2021_Nordland"
# campaign="S_chartering_2021_Borek"
# campaign="NW_chartering_2021_Borek"
# campaign="NW_chartering_2021_Nordland"
campaign="Swiss_Camp_2021_July_23-29"
# campaign="NE_chartering_2021_Aug_Nordland"
# campaign="NE_chartering_2021_Aug_Borek"

# ------------------------------------------------ parameters
tools_mass=100 # kg
new_AWS_mass=150 # kg
crane_mass=50 # kg

# ------------------------------------------------ campaign output files
# summary table
ofile="./planning_info/"+campaign
out_concept=open(ofile+".csv","w+")
out_concept.write('date (YYYY-MM-DD),day,day in a row count,start time (first of day),from,to,freight (kg),N PAX,distance (nm),fly+taxi+circle time (h),fuel consumption litres,fuel consumption cost kDKK,fuel_remaining(liters),arrival time (local time),stoppage time (h),from lat,from lon,destination lat,destination lon,start location name,landing location name,air speed kt,description of work\n')

# fuel
ofile_daily="./planning_info/"+campaign+"_daily_totals"
out_daily=open(ofile_daily+".csv","w+")
out_daily.write('date (YYYY-MM-DD),fly_time,fly_cost,fuel consumption litres,fuel consumption cost kDKK,day cost per all people,last activity\n')

# ------------------------------------------------
# ------------------------------------------------ start defining all campaigns
# ------------------------------------------------

if campaign=="S_chartering_2021_Borek":
    hourly_rate=13.39157 #k DKK Borek
    min_cost_per_day=4
    day_counter=1
    
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 6, 16)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="transit to Greenland."
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"IKA","GOH",time,18,cargo_mass,N_PAX,fly_time)
    fuel_remaining=1400
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"IKA","GOH","","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,organize AWS\n") 
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    
    # ------------------------------------------------ new fly day
    day_counter+=1; date+=datetime.timedelta(days=1)
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=4*new_AWS_mass+150 # 3 new AWS plus tools_mass
    N_PAX=3
    work="transit to SFJ with 4 x AWS. leave 3 in SFJ at refueling"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"GOH","SFJ",time,1,cargo_mass,N_PAX,fly_time)
    fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass # 3 new AWS plus tools_mass
    work="first AWS maintenance. new AWS installation at DY2. no refueling"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","DY2",time,4.5,cargo_mass,N_PAX,fly_time)
    # fuel_remaining=1400 # ??
    work="return to SFJ to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"GOH","DY2","SFJ","",aqua)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="AWS maintenance using crane at SDL"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","SDL",time,0.7,cargo_mass,N_PAX,fly_time)
    # work="don'trefuel at Raven/DYE-2 on return"
    work="return to SFJ to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SDL","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    # fuel_remaining=1400
    work="return to SFJ to overnight"
    # time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"SFJ","SDL","SFJ","",burlywood)
    
    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="new AWS install at CP1. bring back whatever we can"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","CP1",time,4.5,cargo_mass-120,N_PAX,fly_time)
    work="return to JAV to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"CP1","JAV",time,18,cargo_mass-120,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"SFJ","CP1","JAV","",blue)
    
    # ------------------------------------ artifical weather delay
    day_counter+=1; date+=datetime.timedelta(days=1)
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,relax\n")
    fly_time=min_cost_per_day ; work='wx delay day'
    fly_time=min_cost_per_day ; fuel_use=0.
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    
    # ------------------------------------------------ new fly day
    day_counter+=1; date+=datetime.timedelta(days=1)
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="long day. bring fuel drum with. refuel 200 liters at Raven/DYE-2. proceed to SDM"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","DY2",time,0.6,cargo_mass,N_PAX,fly_time)
    fuel_remaining+=200
    work="to SDM. 2950 m ASL"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"DY2","SDM",time,4.5,cargo_mass-150,N_PAX,fly_time)
    work="to UAK to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SDM","UAK",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"JAV","DY2","SDM","UAK",black)
    
    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="transit"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"UAK","GOH",time,0.6,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"UAK","GOH","","",blueviolet)
    
    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="new AWS install at NSE"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"GOH","NSE",time,4.5,cargo_mass,N_PAX,fly_time)
    work="transit to DY2 to refuel. bring fuel drum with."
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NSE","DY2",time,0.5,cargo_mass-150,N_PAX,fly_time)
    fuel_remaining+=200
    work="transit to SFJ"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"DY2","SFJ",time,0.5,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"GOH","NSE","DY2","SFJ",orange)

    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=0
    work="transit back to Canada"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","IKA",time,4.5,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"SFJ","IKA","","",red)


if campaign=="S_chartering_2021_Nordland":
    hourly_rate=21.850 #kDKK Nordland
    min_cost_per_day=2
    day_counter=1

    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 6, 16)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="transit to Greenland. bring any cargo from Iceland?"
    day_counter=1
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"AEY","KUS",time,1,cargo_mass,N_PAX,fly_time)
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"KUS","GOH",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"AEY","KUS","GOH","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,organize AWS\n") 
    fly_time=min_cost_per_day ; fuel_use=0.
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    
    # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=4*new_AWS_mass+150 # 3 new AWS plus tools_mass
    N_PAX=3
    work="transit to SFJ with 4 x AWS. leave 3 in SFJ at refueling"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"GOH","SFJ",time,1,cargo_mass,N_PAX,fly_time)
    cargo_mass=1*new_AWS_mass+tools_mass # 3 new AWS plus tools_mass
    work="first AWS maintenance. new AWS installation at DY2"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","DY2",time,4.5,cargo_mass,N_PAX,fly_time)
    work="return to SFJ to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"GOH","DY2","SFJ","",aqua)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="AWS maintenance using crane at SDL"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","SDL",time,0.7,cargo_mass,N_PAX,fly_time)
    work="refuel at Raven/DYE-2 on return"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SDL","DY2",time,4.5,cargo_mass-50,N_PAX,fly_time)
    work="return to SFJ to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"SFJ","SDL","DY2","SFJ",burlywood)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="new AWS install at CP1. bring back whatever we can"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","CP1",time,4.5,cargo_mass-120,N_PAX,fly_time)
    work="return to JAV to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"CP1","JAV",time,18,cargo_mass-120,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"SFJ","CP1","JAV","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,relax\n") ; day_counter+=1; date+=datetime.timedelta(days=1)
    fly_time=min_cost_per_day ; fuel_use=0.
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="long day. refuel at Raven/DYE-2. proceed to SDM"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","DY2",time,0.6,cargo_mass,N_PAX,fly_time)
    work="to SDM. 2950 m ASL"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"DY2","SDM",time,4.5,cargo_mass-150,N_PAX,fly_time)
    work="to UAK to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SDM","UAK",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"JAV","DY2","SDM","UAK",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="transit"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"UAK","GOH",time,0.6,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"UAK","GOH","","",blueviolet)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="new AWS install at NSE"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"GOH","NSE",time,4.5,cargo_mass,N_PAX,fly_time)
    work="transit to KUS"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NSE","KUS",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"GOH","NSE","KUS","",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=0*new_AWS_mass+tools_mass
    work="transit to AEY"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"KUS","AEY",time,4.5,cargo_mass,N_PAX,fly_time)
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"KUS","AEY","","",orange)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")

if campaign=="NE_chartering_2021_Aug_Borek":
    hourly_rate=13.39157 #k DKK Borek
    min_cost_per_day=4
    day_counter=1
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 8, 7)
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=0 # for transit from Iceland
    work="transit from Iqaluit with no cargo"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"IKA","SFJ",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"IKA","SFJ","","",red)

    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="refuel at Summit 2 x 200 liters. basic maintanance at Summit"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","SUM",time,4,cargo_mass,N_PAX,fly_time)
    fuel_remaining+=400
    work="EGP new AWS install. Twin Otter overnights"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SUM","EGP",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"SFJ","SUM","EGP","",blue)

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    
    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="maintanance at NASA-E"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"EGP","NAE",time,4.,cargo_mass,N_PAX,fly_time)
    work="return to EGP for overnight 2"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NAE","EGP",time,4.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"EGP","NAE","EGP","",orange)
    
    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="crane maintanance at NASA-U"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"EGP","NAU",time,4.,cargo_mass,N_PAX,fly_time)
    work="return to coast. Upernavik"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NAU","JUV",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"EGP","NAU","JUV","",black)

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="flight to SFJ via JUV"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JUV","JAV",time,0.7,cargo_mass,N_PAX,fly_time)
    work="refuel in JAV then end day in SFJ"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SFJ",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"JUV","JAV","SFJ","",black)

    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="return to Canada"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","IKA",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"SFJ","IKA","","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

if campaign=="NE_chartering_2021_Aug_Nordland":
# Where HUB is either CNP or DAN/ZAC
    hourly_rate=21.850 #kDKK Nordland
    min_cost_per_day=2
    day_counter=1
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 8, 7)
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="transit from Iceland with some cargo"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"AEY","CNP",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"AEY","CNP","","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="refuel at Summit. basic maintanance at Summit"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"CNP","SUM",time,4,cargo_mass,N_PAX,fly_time)
    work="EGP new AWS install. Twin Otter overnights"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SUM","EGP",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"CNP","SUM","EGP","",blue)

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,organize AWS\n") 
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="maintanance at Summit"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"EGP","NAE",time,4.,cargo_mass,N_PAX,fly_time)
    work="return to EGP for overnight 2"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NAE","EGP",time,4.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"EGP","NAE","EGP","",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="crane maintanance at NASA-U"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"EGP","NAU",time,4.,cargo_mass,N_PAX,fly_time)
    work="return to coast. Upernavik"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NAU","JUV",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"EGP","NAU","JUV","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="return toward Iceland via Nuuk"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JUV","GOH",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"JUV","GOH","","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="return toward Iceland"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"GOH","AEY",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"GOH","AEY","","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

if campaign=="Swiss_Camp_2021_July_23-29":

    day_counter=1
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 7, 23)
    cargo_mass=150
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    N_PAX=3 # for transit from Iceland
    work="put in full load to Swiss Camp via 1.5 h ground stop at JAR. first arrival to Swiss Camp after 1 year. PAX names: Derek Houtz. Jason Box. Simon Steffen. nn1"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","JAR",time,0.5,cargo_mass,N_PAX,fly_time)
    work="after ground stop. to Swiss Camp"

    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAR","SWC",time,1.5,100,N_PAX,fly_time)
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,0,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=13 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="put in with 1 PAX remaining gear"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,250,1,fly_time)
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,250,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    day_counter=1
    date = datetime.date(2021, 7, 28)
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="flight 1 of 4. full day charter. come in with tents for memorial event. set up sling operation. take out a ful load of stuff back to JAV in cabin"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    work="return with sling or full cabin"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    work="flight 2 of 4. full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    work="return with sling or full cabin"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    work="flight 3 of 4. full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    work="return with sling or full cabin"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    work="flight 4 of 4. full day charter. come in +2 PAX take out a ful load of stuff back to JAV. could be a sling load"
    N_PAX=2
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,0,N_PAX,fly_time)
    work="return with sling or full cabin"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")


    # ------------------------------------------------ new fly day
    day_counter+=1
    date = datetime.date(2021, 7, 29)
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="flight 1 of 3. full day charter. camp pull out. full cabin or sling"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,100,0,fly_time)

    work="flight 2 of 3. full day charter. camp pull out with 1.5h stop at JAR. 2 PAX on return"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAR",time,1.5,100,4,fly_time)
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAR","JAV",time,0.5,100,4,fly_time)

    work="flight 3 of 3. full day charter. camp pull out with 1.5h stop at JAR. 3 PAX on return"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"JAV","SWC",time,0.5,0,3,fly_time)
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SWC","JAV",time,0.5,100,3,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")


if campaign=="NW_chartering_2021_Nordland":
    hourly_rate=21.850 #kDKK Nordland
    min_cost_per_day=2
    # ------------------------------------------------ new fly day
    day_counter=1
    date = datetime.date(2021, 8, 19)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="transit to W Greenland."
    ground_stop_time=18
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"AEY","SFJ",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"SFJ","THU","","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
     # ------------------------------------------------ new fly day
    work="transit to Thule"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","THU",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    work="pick people and cargo. move people and cargo to QAN airport"
    N_PAX=3 # for transit to THU
    cargo_mass=2*new_AWS_mass+tools_mass+crane_mass
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"THU","QAN",time,ground_stop_time,cargo_mass,3,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"THU","QAN","QAN","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
       
   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    work="new AWS install at Petermann ELA"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","PET",time,0.7,cargo_mass,N_PAX,fly_time)
    work="return to QAN to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"PET","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"QAN","PET","QAN","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="long day. new AWS install at Neem and visit Humboldt after NEEM landing and ground stop. no crane?"
    ground_stop_time=4.
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","NEM",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    work="new AWS install at Neem. recover some Neem kit? 4.5 h ground stop. after this and visit Humboldt after NEEM landing and "
    ground_stop_time=2.
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NEM","HUM",time,ground_stop_time,cargo_mass-100,N_PAX,fly_time)
    work="return to QAAN to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"HUM","QAN",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"QAN","NEM","HUM","QAN",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="service 1 existing AWS. 3 other towers. no crane?"
    ground_stop_time=5
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","CEN",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    work="return to QAN to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"CEN","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"QAN","CEN","QAN","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    work="return PAX to THU then return plane to soutward"
    ground_stop_time=1
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","THU",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    work="return to YRB with no PAX"
    N_PAX=0 # return to YRB with no pax
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"THU","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"QAN","THU","YRB","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

     # ------------------------------------------------ new fly day
    cargo_mass=0
    work="to Icelamd"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"SFJ","AEY",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"SFJ","AEY","","",red)

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")


if campaign=="NW_chartering_2021_Borek":
    hourly_rate=13.39157 #k DKK Borek
    min_cost_per_day=4
#     Proposed NW Loop:

# Day 1: YRB-THU-QAN (move people and cargo to QAN airport)
# Day 2: QAN-Petermann-QAN (1 new AWS)
# Day 3: QAN-NEEM-Humboldt-QAN (1 new AWS, 1 existing AWS)
# Day 4: QAN-CEN-QAN (1 existing AWS, 3 other towers)
# Day 5: QAN-THU-YRB (return people and cargo to THU base)
# Day 6: Weather
# Day 7: Weather
# Day 8: Weather

     # ------------------------------------------------ new fly day
    day_counter=1
    date = datetime.date(2021, 8, 20)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    work="transit to Greenland."
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"YRB","THU",time,1,cargo_mass,N_PAX,fly_time)
    work="move people and cargo to QAN airport"
    N_PAX=3 # for transit to THU
    cargo_mass=2*new_AWS_mass+tools_mass+crane_mass
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"THU","QAN",time,18,cargo_mass,3,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"YRB","THU","QAN","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
       
   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    work="new AWS install at Petermann ELA"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","PET",time,0.7,cargo_mass,N_PAX,fly_time)
    work="return to QAN to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"PET","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"QAN","PET","QAN","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="long day. bring 1 x 200 l fuel barrel with. new AWS install at Neem and visit Humboldt after NEEM landing and ground stop. no crane?"
    ground_stop_time=4.
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","NEM",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    fuel_remaining+=200
    work="new AWS install at Neem. recover some Neem kit? 4.5 h ground stop. after this and visit Humboldt after NEEM landing and "
    ground_stop_time=2.
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"NEM","HUM",time,ground_stop_time,cargo_mass-100,N_PAX,fly_time)
    work="return to QAAN to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"HUM","QAN",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"QAN","NEM","HUM","QAN",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass
    work="service 1 existing AWS. 3 other towers. no crane?"
    ground_stop_time=5
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","CEN",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    work="return to QAN to overnight"
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"CEN","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    output_kml(campaign,day_counter,"QAN","CEN","QAN","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0 ; fuel_use=0 ; fuel_remaining=1400
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    work="return PAX to THU then return plane to YRB"
    ground_stop_time=1
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"QAN","THU",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    work="return to YRB with no PAX"
    N_PAX=0 # return to YRB with no pax
    time,fly_time,fuel_use,fuel_remaining=inter_dist(fuel_remaining,fuel_use,work,date,start_time,day_counter,"THU","YRB",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(3+N_crew))+","+work+"\n")
    output_kml(campaign,day_counter,"QAN","THU","YRB","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")
    
    # ------------------------------------ artifical weather delay
    day_counter+=1 ; date+=datetime.timedelta(days=1)    
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    # day_counter,date=weather_day(day_counter,date)
    fly_time=min_cost_per_day ; fuel_use=0. ; work='wx delay day'
    out_daily.write(str(date)+",{:.1f}".format(fly_time)+",{:.1f}".format(hourly_rate*fly_time)+",{:.0f}".format(fuel_use)+",{:.1f}".format(fuel_use*cost_per_li/1000)+",{:.1f}".format(cost_per_day_person*(N_PAX+N_crew))+","+work+"\n")

# ------------------------------------------------
# ------------------------------------------------ end define all campaigns
# ------------------------------------------------

# close output files
out_daily.close()
out_concept.close()
os.system("cat "+ofile_daily+".csv")

files=[ofile,ofile_daily]

for f in files:
    # read csv
    df2=pd.read_csv(f+".csv")
    # df=df.reset_index(drop=True, inplace=True)
    if f==ofile_daily:
        n=len(df2)
        # asas
        # print(ofile_daily,df2.iloc[n,:])
        row = ["total", sum(df2.iloc[:,1]), sum(df2.iloc[:,2]),sum(df2.iloc[:,3]),sum(df2.iloc[:,4]),sum(df2.iloc[:,5]),""]
        row2 = ["grand total (MDKK)", (sum(df2.iloc[:,2])+ sum(df2.iloc[:,4])+sum(df2.iloc[:,5]))/1000.,"","","","",""]
        row3 = ["grand total incl. quarantine (MDKK)", (75+sum(df2.iloc[:,2])+ sum(df2.iloc[:,4])+sum(df2.iloc[:,5]))/1000.,"","","","",""]
        df2.loc[n] = row
        df2.loc[n+1] = row2
        df2.loc[n+3] = row3
        df2.to_csv(f+'.csv', index=False)
        # totals=df2.iloc[:,0]
    # write to Excel
    df2.to_excel(f+".xlsx", index=False)
