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
def inter_dist(message,date,start_time,day_counter,A,B,time,stop_time,cargo_mass,N_PAX):
    weekday=date.weekday()
    day_name=calendar.day_name[date.weekday()]
    coords_1 = (float(df.lat[df.id==A]),float(df.lon[df.id==A]))
    coords_2 = (float(df.lat[df.id==B]),float(df.lon[df.id==B]))
    airspeed=130 # kts Twin Otter
    airspeed=105 # kts Helicopter
    d=geopy.distance.distance(coords_1, coords_2).nm
    t=d/airspeed
    time+=t
    BB=str(df.name[df.id==B].values)[2:-2]
    AA=str(df.name[df.id==A].values)[2:-2]
    # print(BB)
    # print(df.name[df.id==A].aslist)
    # ,">",df.name[df.id==B])
    out_string=str(date)+","\
        +str(day_name)+","\
        +str(day_counter)+","\
        +str(start_time)+\
        ","+A+","+B+","\
        +str(cargo_mass)+","\
        +str(N_PAX)+","\
        "{:.0f}".format(d)+",{:.2f}".format(t)+","+ \
          "{:.1f}".format(time)+","+str(stop_time)+","+\
          "{:.4f}".format(coords_1[0])+",{:.4f}".format(coords_1[1])+","+\
          "{:.4f}".format(coords_2[0])+",{:.4f}".format(coords_2[1])+","+\
              AA+","+BB+","+\
            str(airspeed)+","+\
            message
    print(out_string)
    # print(out_
    out_concept.write(out_string+"\n")
    time+=stop_time

    return time
# ------------------------------------------------ end function to output ASCII text lines to be read into dataframe

campaign="Campaign_S_traverse_2021_Nordland"
# campaign="Campaign_NW_traverse_2021_Borek"
campaign="Swiss_Camp_2021"

ofile="./planning_info/"+campaign
out_concept=open(ofile+".csv","w+")
out_concept.write('date,day,day in a row count,start time (first of day),from,to,freight (kg),N PAX,distance (nm),fly time (h),arrival time (local time),stoppage time (H),from lat,from lon,destination lat,destination lon,start location name,landing location name,air speed kt,description of work\n')

# ------------------------------------------------ start define plan


if campaign=="Swiss_Camp_2021_July_16-23":

    cargo_mass=150
    date = datetime.date(2021, 7, 16)
    day_counter=1
    start_time=8.5 ; time=start_time
    message="put in full load to Swiss Camp. first arrival after 1 year. PAX names: Derek Houtz. Jason Box. Simon Steffen. nn1"
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,cargo_mass,4)
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,0,0)
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)

    start_time=13 ; time=start_time
    message="put in with 1 PAX remaining gear"
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,250,1)
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,250,0)
    output_kml(campaign,day_counter,"JAV","SWC","JAV","",red)
    day_counter+=1 ; date+=datetime.timedelta(days=1)
    
    date = datetime.date(2021, 7, 20)
    day_counter=1
    start_time=8.25 ; time=start_time
    message="flight 1 of full day charter. come in with tents for memorial event. set up sling operation. take out a ful load of stuff back to JAV in cabin"
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0)
    message="return with sling or full cabin"
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0)

    message="flight 2 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0)
    message="return with sling or full cabin"
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0)

    message="flight 3 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0)
    message="return with sling or full cabin"
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0)

    message="flight 4 of full day charter. come in empty? take out a ful load of stuff back to JAV. could be a sling load"
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0)
    message="return with sling or full cabin"
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,450,0)

    day_counter+=1 ; date+=datetime.timedelta(days=1)

    start_time=8.5 ; time=start_time
    message="bring one PAX in. Paolo Solari Bozzi. Marina Aliverti. and others? do memorial event with visitors this day?"
    N_PAX=2
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,200,N_PAX)
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,200,0)

    day_counter+=1 ; date+=datetime.timedelta(days=1)

    start_time=8.5 ; time=start_time
    message="bring 5 more PAX in for memorial event. Names as yet underfined. 2 come back after 1.5 h ground stop. leaving 10 on camp."
    N_PAX=5
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,1.5,100,N_PAX)
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,200,0)

    day_counter+=1 ; date+=datetime.timedelta(days=1)

    start_time=8.5 ; time=start_time
    message="Pull all out"
    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0)
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,5)

    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0)
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,3)

    time=inter_dist(message,date,start_time,day_counter,"JAV","SWC",time,0.5,0,0)
    time=inter_dist(message,date,start_time,day_counter,"SWC","JAV",time,0.5,100,2)
        
if campaign=="Campaign_NW_traverse_2021_Borek":

    df.name[df.id=="POL"]
    day_counter=1
    start_time=8.5 ; time=start_time
    time=inter_dist(message,date,start_time,day_counter,"POL","THU",time,1)
    output_kml(campaign,day_counter,"POL","THU","","",red)
    day_counter+=1
    
    # ------------------------------------ artifical weather delay
    out_concept.write(str(day_counter)+', weather delay\n') ; day_counter+=1
    
    # 2 AWS on board; DY2 and CP1
    # add cargo mass = 150 kg / AWS
    # tools 50 kg
    # PAX = 3
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"THU","CEN",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"CEN","THU",time,18)
    output_kml(campaign,day_counter,"THU","CEN","THU","",red)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"THU","HUM",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"HUM","THU",time,18)
    output_kml(campaign,day_counter,"THU","HUM","THU","",aqua)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"THU","PET",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"PET","THU",time,18)
    output_kml(campaign,day_counter,"THU","PET","THU","",orange)
    day_counter+=1
    
    
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"THU","NEM",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"NEM","THU",time,18)
    output_kml(campaign,day_counter,"THU","NEM","THU","",blue)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"THU","POL",time,4.5)
    output_kml(campaign,day_counter,"THU","POL","","",black)
    day_counter+=1


if campaign=="Campaign_S_traverse_2021_Nordland":

    df.name[df.id=="AEY"]
    day_counter=1
    start_time=8.5 ; time=start_time
    time=inter_dist(message,date,start_time,day_counter,"AEY","KUS",time,1)
    time=inter_dist(message,date,start_time,day_counter,"KUS","GOH",time,18)
    output_kml(campaign,day_counter,"AEY","KUS","GOH","",red)
    day_counter+=1
    
    # ------------------------------------ artifical weather delay
    out_concept.write(str(day_counter)+', weather delay\n') ; day_counter+=1
    
    # 2 AWS on board; DY2 and CP1
    # add cargo mass = 150 kg / AWS
    # tools 50 kg
    # PAX = 3
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"GOH","DY2",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"DY2","SFJ",time,18)
    output_kml(campaign,day_counter,"GOH","DY2","SFJ","",aqua)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"SFJ","SDL",time,0.7)
    time=inter_dist(message,date,start_time,day_counter,"SDL","DY2",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"DY2","SFJ",time,18)
    output_kml(campaign,day_counter,"SFJ","SDL","DY2","SFJ",burlywood)
    day_counter+=1
    
    start_time=8.5
    time=inter_dist(message,date,start_time,day_counter,"SFJ","CP1",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"CP1","JAV",time,18)
    output_kml(campaign,day_counter,"SFJ","CP1","JAV","",blue)
    day_counter+=1
    
    # ------------------------------------ artifical weather delay
    out_concept.write(str(day_counter)+', weather delay\n') ; day_counter+=1
    
    start_time=8.
    time=inter_dist(message,date,start_time,day_counter,"JAV","DY2",time,0.6)
    time=inter_dist(message,date,start_time,day_counter,"DY2","SDM",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"SDM","UAK",time,18)
    output_kml(campaign,day_counter,"JAV","DY2","SDM","UAK",black)
    day_counter+=1
    
    start_time=8.
    time=inter_dist(message,date,start_time,day_counter,"UAK","GOH",time,0.6)
    output_kml(campaign,day_counter,"UAK","GOH","","",blueviolet)
    day_counter+=1
    
    start_time=8.
    time=inter_dist(message,date,start_time,day_counter,"GOH","NSE",time,4.5)
    time=inter_dist(message,date,start_time,day_counter,"NSE","KUS",time,18)
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
