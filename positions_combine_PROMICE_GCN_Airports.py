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


fn='./input_data/PROMICE_info_from_GPS_data_2017-2018.csv'
df_p = pd.read_csv(fn,sep='\t')
print(df_p.columns)
fn='./input_data/GCN info ca.2000.csv'
df_g = pd.read_csv(fn)
print(df_g.columns)
fn='./input_data/Airports_in_and_Around_Greenland.txt'
df_a = pd.read_csv(fn)
print(df_a.columns)

n_p=len(df_p)
n_g=len(df_g)
n_a=len(df_a)

n=len(df_p)+len(df_g)+len(df_a)

d=np.zeros((2,n))
d[0,0:n_p]=df_p.lat
d[0,n_p:n_p+n_g]=df_g.lat
d[0,n_p+n_g:n_p+n_g+n_a]=df_a.lat

d[1,0:n_p]=df_p.lon
d[1,n_p:n_p+n_g]=df_g.lon
d[1,n_p+n_g:n_p+n_g+n_a]=df_a.lon

name=['']*n
name[0:n_p]=df_p.name
name[n_p:n_p+n_g]=df_g.name
name[n_p+n_g:n_p+n_g+n_a]=df_a.name

cod=['']*n
cod[0:n_p]=df_p.name
cod[n_p:n_p+n_g]=df_g.nickname
cod[n_p+n_g:n_p+n_g+n_a]=df_a.code

df = pd.DataFrame(columns = ['id','name','lat','lon'],index=None) 
df.lat=d[0,:]
df.lon=d[1,:]
df.name=name
df.id=cod

df.to_csv('./planning_info/all_sites.csv')
