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

working_dir='/Users/jason/Dropbox/AWS/AWS_Airport_positions/' # change this in your local system
os.chdir(working_dir)

fn='./distances/sites.csv'
df= pd.read_csv(fn)
df=df.drop(['Unnamed: 0'], axis=1)
# print(df.columns)


def inter_dist(A,B):
    coords_1 = (float(df.lat[df.id==A]),float(df.lon[df.id==A]))
    coords_2 = (float(df.lat[df.id==B]),float(df.lon[df.id==B]))
    airspeed=150 # kts
    d=geopy.distance.distance(coords_1, coords_2).nm
    t=d/airspeed
    print(A+'>'+B,"{:.0f}".format(d)+' nm',"{:.2f}".format(t)+' hours')

print("day 1")
inter_dist('AEY','KUS')
inter_dist('KUS','GOH')
print("day 2")
inter_dist('GOH','SFJ')
print("day 3")
inter_dist('SFJ','DY2')
inter_dist('DY2','SFJ')
print("day 4")
inter_dist('SFJ','DY2')
inter_dist('DY2','SDL')

