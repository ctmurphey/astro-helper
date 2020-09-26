import ipinfo
from astropy.time import Time
import datetime
from astropy import units as u
import numpy as np


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days   = [31,    28,     31,    30,    31,   30,     31,    31,    30,     31,    30,   31 ]



### Next goal in development: get coordinates these from lookup of objects
RA = float(input("\nEnter the object's right ascension: "))
DEC = float(input("Enter the object's declination: "))

if RA < 0: #solely for time of year calculations
    ra = RA + 360
else:
    ra = RA

timeofyear = ra/360 * 365

for i in range(len(days)):
    if timeofyear - days[i] > 0:
        timeofyear -= days[i]
    else:
        month = months[i]
        day = int(timeofyear)+1
        break





cur_time = datetime.datetime.now()

handler = ipinfo.getHandler()
details = handler.getDetails()
lat = float(details.latitude)*u.deg
lon = float(details.longitude)*u.deg


t = Time(cur_time, scale='utc', location=(lat, lon))
LST = t.sidereal_time('mean')

LST_str = str(LST)

if(LST_str[1] == "h"): 
    LST_str = "0"+LST_str

hours   = float(LST_str[:2])
minutes = float(LST_str[3:5])
seconds = float(LST_str[6:-1])

LST_d = hours + minutes/60 + seconds/3600

RA = RA*u.deg
DEC = DEC*u.deg

H = ((LST_d*u.hourangle).to(u.deg) - RA).to(u.hourangle)

time_left = -H.value
def time_tuple(arg):
    hours_left = int(arg)
    mins = (arg-hours_left)*60
    min_left = int(mins)
    secs = (mins-min_left)*60
    return(hours_left, min_left, secs)

print("\nThe best time to view the object is around %s %d" %(month, day))

print("\nView in the sky in %s, %s:" % (details.city, details.region))
print("The object will be at zenith in %d hours, %d minutes, %d seconds" % time_tuple(time_left))

if(abs(lat.value+DEC.value) > 90):
    print('Object never sets below horizon\n')

elif(abs(lat.value-DEC.value) > 90):
    print("Object never rises above horizon\n")

else:
    x = -np.tan(DEC)*np.tan(lat)
    delta_t = float((np.arccos(x.value)))*12/np.pi

    t_to_rise = time_left - delta_t
    t_to_set  = time_left + delta_t

    rise_tuple = time_tuple(t_to_rise)
    set_tuple  = time_tuple(t_to_set)

    print("The object will rise in %d hours %d minutes %d seconds" % rise_tuple)
    print("The object will set in %d hours %d minutes %d seconds\n" % set_tuple)