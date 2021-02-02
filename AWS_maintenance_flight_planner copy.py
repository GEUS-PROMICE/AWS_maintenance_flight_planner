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
def inter_dist(message,date,start_time,day_counter,A,B,time,stop_time,cargo_mass,N_PAX,fly_time):
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    coords_1 = (float(df.lat[df.id==A]),float(df.lon[df.id==A]))
    coords_2 = (float(df.lat[df.id==B]),float(df.lon[df.id==B]))
    airspeed=140 # kts Twin Otter
    # airspeed=105 # kts Helicopter
    d=geopy.distance.distance(coords_1, coords_2).nm
    t=d/airspeed
    fly_time+=t # total fly time before taxi time
    t+=2*12/60 # circling, taxi at start and end
    time+=t
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
        "{:.0f}".format(d)+",{:.1f}".format(t)+","+ \
          "{:.1f}".format(time)+","+stop_time_string+","+\
          "{:.4f}".format(coords_1[0])+",{:.4f}".format(coords_1[1])+","+\
          "{:.4f}".format(coords_2[0])+",{:.4f}".format(coords_2[1])+","+\
              AA+","+BB+","+\
            str(airspeed)+","+\
            message
    print(out_string)
    # print(out_
    out_concept.write(out_string+"\n")
    time+=stop_time

    return time,fly_time
# ------------------------------------------------ end function to output ASCII text lines to be read into dataframe

# ------------------------------------------------ start function
def weather_day(day_counter,date):
    out_concept.write(str(day_counter)+'. weather delay\n')
    day_counter+=1
    date+=datetime.timedelta(days=1)
    
    return day_counter,date
# ------------------------------------------------ end function

# ------------------------------------------------ campaigns
campaign="S_chartering_2021_Nordland"
campaign="S_chartering_2021_Borek"
# campaign="NW_chartering_2021_Borek"
# campaign="NW_chartering_2021_Nordland"
# campaign="Swiss_Camp_2021_July_23-30"
# campaign="NE_chartering_2021_Aug_Nordland"
campaign="NE_chartering_2021_Aug_Borek"

# ------------------------------------------------ parameters
tools_mass=100 # kg
new_AWS_mass=150 # kg
crane_mass=50 # kg

# ------------------------------------------------ campaign output file
ofile="./planning_info/"+campaign
out_concept=open(ofile+".csv","w+")
out_concept.write('date (YYYY-MM-DD),day,day in a row count,start time (first of day),from,to,freight (kg),N PAX,distance (nm),fly+taxi+circle time (h),arrival time (local time),stoppage time (h),from lat,from lon,destination lat,destination lon,start location name,landing location name,air speed kt,description of work\n')

# ------------------------------------------------
# ------------------------------------------------ start defining all campaigns
# ------------------------------------------------

if campaign=="S_chartering_2021_Borek":

    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 6, 16)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0
    message="transit to Greenland."
    day_counter=1
    time,fly_time=inter_dist(message,date,start_time,day_counter,"IKA","GOH",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"IKA","GOH","","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,organize AWS\n") ; day_counter+=1; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=4*new_AWS_mass+150 # 3 new AWS plus tools_mass
    N_PAX=3
    message="transit to SFJ with 4 x AWS. leave 3 in SFJ at refueling"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"GOH","SFJ",time,1,cargo_mass,N_PAX,fly_time)
    cargo_mass=1*new_AWS_mass+tools_mass # 3 new AWS plus tools_mass
    message="first AWS maintenance. new AWS installation at DY2"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","DY2",time,4.5,cargo_mass,N_PAX,fly_time)
    message="return to SFJ to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"GOH","DY2","SFJ","",aqua)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="AWS maintenance using crane at SDL"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","SDL",time,0.7,cargo_mass,N_PAX,fly_time)
    message="refuel at Raven/DYE-2 on return"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SDL","DY2",time,4.5,cargo_mass-50,N_PAX,fly_time)
    message="return to SFJ to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","SDL","DY2","SFJ",burlywood)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="new AWS install at CP1. bring back whatever we can"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","CP1",time,4.5,cargo_mass-120,N_PAX,fly_time)
    message="return to JAV to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"CP1","JAV",time,18,cargo_mass-120,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","CP1","JAV","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,relax\n") ; day_counter+=1; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="long day. refuel at Raven/DYE-2. proceed to SDM"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","DY2",time,0.6,cargo_mass,N_PAX,fly_time)
    message="to SDM. 2950 m ASL"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"DY2","SDM",time,4.5,cargo_mass-150,N_PAX,fly_time)
    message="to UAK to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SDM","UAK",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","DY2","SDM","UAK",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    message="transit"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"UAK","GOH",time,0.6,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"UAK","GOH","","",blueviolet)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="new AWS install at NSE"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"GOH","NSE",time,4.5,cargo_mass,N_PAX,fly_time)
    message="transit to DY2 to refuel"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NSE","DY2",time,0.5,cargo_mass-150,N_PAX,fly_time)
    message="transit to SFJ"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"DY2","SFJ",time,0.5,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"GOH","NSE","DY2","SFJ",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=0
    message="transit back to Canada"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","IKA",time,4.5,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")


if campaign=="S_chartering_2021_Nordland":


    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 6, 16)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0
    message="transit to Greenland. bring any cargo from Iceland?"
    day_counter=1
    time,fly_time=inter_dist(message,date,start_time,day_counter,"AEY","KUS",time,1,cargo_mass,N_PAX,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"KUS","GOH",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"AEY","KUS","GOH","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,organize AWS\n") ; day_counter+=1; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=4*new_AWS_mass+150 # 3 new AWS plus tools_mass
    N_PAX=3
    message="transit to SFJ with 4 x AWS. leave 3 in SFJ at refueling"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"GOH","SFJ",time,1,cargo_mass,N_PAX,fly_time)
    cargo_mass=1*new_AWS_mass+tools_mass # 3 new AWS plus tools_mass
    message="first AWS maintenance. new AWS installation at DY2"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","DY2",time,4.5,cargo_mass,N_PAX,fly_time)
    message="return to SFJ to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"GOH","DY2","SFJ","",aqua)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="AWS maintenance using crane at SDL"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","SDL",time,0.7,cargo_mass,N_PAX,fly_time)
    message="refuel at Raven/DYE-2 on return"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SDL","DY2",time,4.5,cargo_mass-50,N_PAX,fly_time)
    message="return to SFJ to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"DY2","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","SDL","DY2","SFJ",burlywood)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="new AWS install at CP1. bring back whatever we can"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","CP1",time,4.5,cargo_mass-120,N_PAX,fly_time)
    message="return to JAV to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"CP1","JAV",time,18,cargo_mass-120,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","CP1","JAV","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    out_concept.write(out_string+" weather delay,,,,,,,,,,,,,,,,,relax\n") ; day_counter+=1; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="long day. refuel at Raven/DYE-2. proceed to SDM"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","DY2",time,0.6,cargo_mass,N_PAX,fly_time)
    message="to SDM. 2950 m ASL"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"DY2","SDM",time,4.5,cargo_mass-150,N_PAX,fly_time)
    message="to UAK to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SDM","UAK",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","DY2","SDM","UAK",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    message="transit"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"UAK","GOH",time,0.6,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"UAK","GOH","","",blueviolet)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="new AWS install at NSE"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"GOH","NSE",time,4.5,cargo_mass,N_PAX,fly_time)
    message="transit to KUS"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NSE","KUS",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"GOH","NSE","KUS","",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=0*new_AWS_mass+tools_mass
    message="transit to AEY"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"KUS","AEY",time,4.5,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")

if campaign=="NE_chartering_2021_Aug_Borek":
# Where HUB is either CNP or DAN/ZAC

    day_counter=1
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 8, 7)
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8.25 ; time=start_time ; fly_time=0
    N_PAX=0 # for transit from Iceland
    message="transit from Iqaluit with no cargo"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"IKA","SFJ",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"IKA","SFJ","","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8. ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="refuel at Summit. basic maintanance at Summit"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","SUM",time,4,cargo_mass,N_PAX,fly_time)
    message="EGP new AWS install. Twin Otter overnights"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SUM","EGP",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","SUM","EGP","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)
    
    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="maintanance at NASA-E"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"EGP","NAE",time,4.,cargo_mass,N_PAX,fly_time)
    message="return to EGP for overnight 2"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NAE","EGP",time,4.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"EGP","NAE","EGP","",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    
    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="crane maintanance at NASA-U"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"EGP","NAU",time,4.,cargo_mass,N_PAX,fly_time)
    message="return to coast. Upernavik"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NAU","JUV",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"EGP","NAU","JUV","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="flight to SFJ via JUV"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JUV","JAV",time,0.7,cargo_mass,N_PAX,fly_time)
    message="refuel in JAV then end day in SFJ"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SFJ",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JUV","JAV","SFJ","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=8.5 ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="return to Canada"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","IKA",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","IKA","","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

if campaign=="NE_chartering_2021_Aug_Nordland":
# Where HUB is either CNP or DAN/ZAC

    day_counter=1
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 8, 7)
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8.25 ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="transit from Iceland with some cargo"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"AEY","CNP",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"AEY","CNP","","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    start_time=8. ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="refuel at Summit. basic maintanance at Summit"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"CNP","SUM",time,4,cargo_mass,N_PAX,fly_time)
    message="EGP new AWS install. Twin Otter overnights"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SUM","EGP",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"CNP","SUM","EGP","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="maintanance at Summit"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"EGP","NAE",time,4.,cargo_mass,N_PAX,fly_time)
    message="return to EGP for overnight 2"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NAE","EGP",time,4.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"EGP","NAE","EGP","",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=9. ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="crane maintanance at NASA-U"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"EGP","NAU",time,4.,cargo_mass,N_PAX,fly_time)
    message="return to coast. Upernavik"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NAU","JUV",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"EGP","NAU","JUV","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=8.5 ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="return toward Iceland via Nuuk"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JUV","GOH",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JUV","GOH","","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

    # ------------------------------------------------ new fly day
    cargo_mass=0*new_AWS_mass+tools_mass+crane_mass
    start_time=8.5 ; time=start_time ; fly_time=0
    N_PAX=3 # for transit from Iceland
    message="return toward Iceland"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"GOH","AEY",time,18.,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"GOH","AEY","","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)    

if campaign=="Swiss_Camp_2021_July_23-30":

    day_counter=1
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 7, 23)
    cargo_mass=150
    start_time=8.5 ; time=start_time ; fly_time=0
    message="put in full load to Swiss Camp. first arrival after 1 year. PAX names: Derek Houtz. Jason Box. Simon Steffen. nn1"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,cargo_mass,4,fly_time)
    message="return empty to JAV"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,0,4,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=13 ; time=start_time ; fly_time=0
    message="put in with 1 PAX remaining gear"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,250,1,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,250,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 7, 27)
    day_counter=1
    start_time=8.25 ; time=start_time ; fly_time=0
    message="flight 1 of full day charter. come in with tents for memorial event. set up sling operation. take out a ful load of stuff back to JAV in cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    message="flight 2 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    message="flight 3 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    message="flight 4 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")

    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    start_time=8.5 ; time=start_time ; fly_time=0
    message="bring one PAX in. Paolo Solari Bozzi. Marina Aliverti. and others? do memorial event with visitors this day?"
    N_PAX=2
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,200,N_PAX,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,200,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    message="bring 5 more PAX in for memorial event. Names as yet underfined. 2 come back after 1.5 h ground stop. leaving 10 on camp."
    N_PAX=5
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,1.5,100,N_PAX,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,200,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    message="Pull all out"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,5,fly_time)

    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,3,fly_time)

    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,2,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
if campaign=="Swiss_Camp_2021_July_16-23":

    day_counter=1
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 7, 16)
    cargo_mass=150
    start_time=8.5 ; time=start_time ; fly_time=0
    message="put in full load to Swiss Camp. first arrival after 1 year. PAX names: Derek Houtz. Jason Box. Simon Steffen. nn1"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,cargo_mass,4,fly_time)
    message="return empty to JAV"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,0,4,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=13 ; time=start_time ; fly_time=0
    message="put in with 1 PAX remaining gear"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,250,1,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,250,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    # ------------------------------------------------ new fly day
    date = datetime.date(2021, 7, 20)
    day_counter=1
    start_time=8.25 ; time=start_time ; fly_time=0
    message="flight 1 of full day charter. come in with tents for memorial event. set up sling operation. take out a ful load of stuff back to JAV in cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    message="flight 2 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    message="flight 3 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)

    message="flight 4 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    message="return with sling or full cabin"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")

    # ------------------------------------------------ new fly day
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    start_time=8.5 ; time=start_time ; fly_time=0
    message="bring one PAX in. Paolo Solari Bozzi. Marina Aliverti. and others? do memorial event with visitors this day?"
    N_PAX=2
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,200,N_PAX,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,200,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    message="bring 5 more PAX in for memorial event. Names as yet underfined. 2 come back after 1.5 h ground stop. leaving 10 on camp."
    N_PAX=5
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,1.5,100,N_PAX,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,200,0,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------------------ new fly day
    start_time=8.5 ; time=start_time ; fly_time=0
    message="Pull all out"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,5,fly_time)

    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,3,fly_time)

    time,fly_time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0,fly_time)
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,2,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")

if campaign=="NW_chartering_2021_Nordland":
     # ------------------------------------------------ new fly day
    day_counter=1
    date = datetime.date(2021, 8, 19)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0
    message="transit to W Greenland."
    ground_stop_time=18
    time,fly_time=inter_dist(message,date,start_time,day_counter,"AEY","SFJ",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","THU","","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
     # ------------------------------------------------ new fly day
    message="transit to Thule"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","THU",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    message="pick people and cargo. move people and cargo to QAN airport"
    N_PAX=3 # for transit to THU
    cargo_mass=2*new_AWS_mass+tools_mass+crane_mass
    time,fly_time=inter_dist(message,date,start_time,day_counter,"THU","QAN",time,ground_stop_time,cargo_mass,3,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"THU","QAN","QAN","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
       
   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    message="new AWS install at Petermann ELA"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","PET",time,0.7,cargo_mass,N_PAX,fly_time)
    message="return to QAN to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"PET","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","PET","QAN","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="long day. new AWS install at Neem and visit Humboldt after NEEM landing and ground stop. no crane?"
    ground_stop_time=4.
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","NEM",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    message="new AWS install at Neem. recover some Neem kit? 4.5 h ground stop. after this and visit Humboldt after NEEM landing and "
    ground_stop_time=2.
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NEM","HUM",time,ground_stop_time,cargo_mass-100,N_PAX,fly_time)
    message="return to QAAN to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"HUM","QAN",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","NEM","HUM","QAN",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="service 1 existing AWS. 3 other towers. no crane?"
    ground_stop_time=5
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","CEN",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    message="return to QAN to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"CEN","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","CEN","QAN","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    message="return PAX to THU then return plane to soutward"
    ground_stop_time=1
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","THU",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    message="return to YRB with no PAX"
    N_PAX=0 # return to YRB with no pax
    time,fly_time=inter_dist(message,date,start_time,day_counter,"THU","SFJ",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","THU","YRB","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

     # ------------------------------------------------ new fly day
    cargo_mass=0
    message="to Icelamd"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"SFJ","AEY",time,18,cargo_mass,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"SFJ","AEY","","",red)

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)


if campaign=="NW_chartering_2021_Borek":

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
    date = datetime.date(2021, 8, 20)
    cargo_mass=0 # for transit from Iceland
    N_PAX=0 # for transit from Iceland
    start_time=8.5 ; time=start_time ; fly_time=0
    message="transit to Greenland."
    day_counter=1
    time,fly_time=inter_dist(message,date,start_time,day_counter,"YRB","THU",time,1,cargo_mass,N_PAX,fly_time)
    message="move people and cargo to QAN airport"
    N_PAX=3 # for transit to THU
    cargo_mass=2*new_AWS_mass+tools_mass+crane_mass
    time,fly_time=inter_dist(message,date,start_time,day_counter,"THU","QAN",time,18,cargo_mass,3,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"YRB","THU","QAN","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
       
   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    message="new AWS install at Petermann ELA"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","PET",time,0.7,cargo_mass,N_PAX,fly_time)
    message="return to QAN to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"PET","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","PET","QAN","",blue)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8. ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="long day. new AWS install at Neem and visit Humboldt after NEEM landing and ground stop. no crane?"
    ground_stop_time=4.
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","NEM",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    message="new AWS install at Neem. recover some Neem kit? 4.5 h ground stop. after this and visit Humboldt after NEEM landing and "
    ground_stop_time=2.
    time,fly_time=inter_dist(message,date,start_time,day_counter,"NEM","HUM",time,ground_stop_time,cargo_mass-100,N_PAX,fly_time)
    message="return to QAAN to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"HUM","QAN",time,18,cargo_mass-150,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","NEM","HUM","QAN",orange)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass
    message="service 1 existing AWS. 3 other towers. no crane?"
    ground_stop_time=5
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","CEN",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    message="return to QAN to overnight"
    time,fly_time=inter_dist(message,date,start_time,day_counter,"CEN","QAN",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","CEN","QAN","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

   # ------------------------------------------------ new fly day
    start_time=8.25 ; time=start_time ; fly_time=0
    cargo_mass=1*new_AWS_mass+tools_mass+crane_mass
    message="return PAX to THU then return plane to YRB"
    ground_stop_time=1
    time,fly_time=inter_dist(message,date,start_time,day_counter,"QAN","THU",time,ground_stop_time,cargo_mass,N_PAX,fly_time)
    message="return to YRB with no PAX"
    N_PAX=0 # return to YRB with no pax
    time,fly_time=inter_dist(message,date,start_time,day_counter,"THU","YRB",time,18,cargo_mass-50,N_PAX,fly_time)
    out_concept.write(",,,,,,,,total fly time no taxi or circling,{:.1f}".format(fly_time)+"\n")
    output_kml(campaign,day_counter,"QAN","THU","YRB","",black)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)

    # ------------------------------------ artifical weather delay
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    out_string=str(date)+","+str(day_name)+","+str(day_counter)
    day_counter,date=weather_day(day_counter,date)
# ------------------------------------------------
# ------------------------------------------------ end define all campaigns
# ------------------------------------------------

# close output file
out_concept.close()
os.system("cat "+ofile+".csv")

# write to csv
df2=pd.read_csv(ofile+".csv")
# df2[stoppage time (H)]=18
# df=df.reset_index(drop=True, inplace=True)

# write to Excel
df2.to_excel(ofile+".xlsx", index=False)
