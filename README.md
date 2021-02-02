in AWS_maintenance_flight_planner.py the user inserts flight plan data including a campaign name then the following fields:
- calendar date (YYYY-MM-DD)
- start time
- stoppage times
- 3-letter codes of starting and ending locations
- number of passengers (PAX)
- freight not including PAX weights
- work per flight leg including that on the ground


**flight plan outputs**

csv and Excel summary table that includes:
- calendar dates
- number of flight days from start to end of charter
- distances between 'airports'
- fly times between 'airports' (without taxi and circling)
- day of week, e.g. Monday, Tuesday
- freight
- cumulative fuel usage
- cumulative cost fuel used
- remaining fuel
- activities for each flight leg
- adding taxi and circling time
- total fly time not including taxi and circling

csv and Excel campaign totals tables that includes:
- total campaign flight hours
- total fuel usage
- cost of all fuel used in the campaign

    
**kml Google Earth** lines between places

![](images/example_map.jpg)

site info:

[list of site names and coordinates](planning_info/all_sites.csv)