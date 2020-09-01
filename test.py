import cgc_tools
import numpy as np
import datetime
a = np.random.random([15,15])*20
#print(a)
b = np.random.random([15,15])*20
t1 = datetime.datetime.now()
lat = np.array([0,10,10,0,0])
lon = np.array([0,0,10,10,0])
output = cgc_tools.multiinout(a,b,lat,lon)

t2 = datetime.datetime.now()
print("15*15:",t2-t1)
#print(output)

a = np.random.random([150,150])*20
b = np.random.random([150,150])*20
#a = np.random.random([15,15])*20
#print(a)
#b = np.random.random([15,15])*20
t1 = datetime.datetime.now()
lat = np.array([0,10,10,0,0])
lon = np.array([0,0,10,10,0])
output = cgc_tools.multiinout(a,b,lat,lon)

t2 = datetime.datetime.now()
print("150*150:",t2-t1)
#print(output)

a = np.random.random([1500,1500])*20
#print(a)
b = np.random.random([1500,1500])*20
t1 = datetime.datetime.now()
lat = np.array([0,10,10,0,0])
lon = np.array([0,0,10,10,0])
output = cgc_tools.multiinout(a,b,lat,lon)

t2 = datetime.datetime.now()
print("1500*1500:",t2-t1)
print(output)


