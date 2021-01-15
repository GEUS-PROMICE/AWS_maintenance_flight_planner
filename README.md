# AWS_maintenance_flight_planner
AWS_maintenance_flight_planner

The inputs are location A to  B, start time, stoppage time. The latest code it looks like to following for days 1-3:

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

first cut at a S Traverse flight plan reads:

day 1, start_time: 8.5
AEY>KUS,473 nm,3.15h transit,arrival time11.7 nm, stop time 1h,AEY:65.6547N,18.0757W,KUS:65.5745N,37.1349W
KUS>GOH,380 nm,2.53h transit,arrival time15.2 nm, stop time 1h,KUS:65.5745N,37.1349W,GOH:64.1917N,51.6742W

weather delay, day 2

day 3, start_time: 8.5
GOH>DY2,193 nm,1.29h transit,arrival time9.8 nm, stop time 4.5h,GOH:64.1917N,51.6742W,DY2:66.4800N,46.2789W
DY2>SFJ,110 nm,0.73h transit,arrival time15.0 nm, stop time 1h,DY2:66.4800N,46.2789W,SFJ:67.0106N,50.7110W

day 4, start_time: 8.5
SFJ>SDL,161 nm,1.07h transit,arrival time9.6 nm, stop time 0.7h,SFJ:67.0106N,50.7110W,SDL:65.9995N,44.5002W
DY2>SDL,52 nm,0.35h transit,arrival time10.6 nm, stop time 4.5h,DY2:66.4800N,46.2789W,SDL:65.9995N,44.5002W
SDL>SFJ,161 nm,1.07h transit,arrival time16.2 nm, stop time 18h,SDL:65.9995N,44.5002W,SFJ:67.0106N,50.7110W

day 5, start_time: 8.5
SFJ>CP1,191 nm,1.28h transit,arrival time9.8 nm, stop time 4.5h,SFJ:67.0106N,50.7110W,CP1:69.8798N,46.9867W
CP1>JAV,94 nm,0.63h transit,arrival time14.9 nm, stop time 18h,CP1:69.8798N,46.9867W,JAV:69.2405N,51.0664W

weather delay, day 6

day 7, start_time: 8.0
JAV>DY2,199 nm,1.32h transit,arrival time9.3 nm, stop time 0.6h,JAV:69.2405N,51.0664W,DY2:66.4800N,46.2789W
DY2>SDM,204 nm,1.36h transit,arrival time11.3 nm, stop time 4.5h,DY2:66.4800N,46.2789W,SDM:63.1489N,44.8172W
SDM>UAK,121 nm,0.81h transit,arrival time16.6 nm, stop time 18h,SDM:63.1489N,44.8172W,UAK:61.1614N,45.4178W

day 8, start_time: 8.0
UAK>GOH,251 nm,1.67h transit,arrival time9.7 nm, stop time 0.6h,UAK:61.1614N,45.4178W,GOH:64.1917N,51.6742W

day 9, start_time: 8.0
GOH>NSE,268 nm,1.79h transit,arrival time9.8 nm, stop time 4.5h,GOH:64.1917N,51.6742W,NSE:66.4797N,42.5002W
NSE>KUS,142 nm,0.95h transit,arrival time15.2 nm, stop time 18h,NSE:66.4797N,42.5002W,KUS:65.5745N,37.1349W

A later version can create an excel table and have calendar days.

Jason
