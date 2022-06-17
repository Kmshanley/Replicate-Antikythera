import math
from datetime import datetime, timedelta

epoch = datetime(2000, 1,1,0,0,0)

def polar2rect(dis, angle):
    return [dis * math.cos(angle), dis * math.sin(angle)]
    
def rect2polar(x, y):
    return [math.sqrt(x**2 + y**2), math.atan(y/x)]

class CicularOrbit:
    def __init__(self, radius, yearLength, epochAngle, parent = None):
        self.radius = radius               #km
        self.yearLength = yearLength       #timedelta
        self.epochAngle = epochAngle       #degrees
        self.parent = parent               #only for 2+nd order orbits

    def getAngleAt(self, time):
        rotations = (time - epoch) / self.yearLength
        currentAngle = (self.epochAngle + (360 * rotations)) % 360
        return currentAngle

    def getPosAt(self, time):
        pos = polar2rect(self.radius, self.getAngleAt(time))
        if(self.parent != None):
            pos[0] = pos[0] + self.parent.getPosAt(time)[0]
            pos[1] = pos[1] + self.parent.getPosAt(time)[1]

        return pos
        

earthDistance = 149600000
earthYear = timedelta(days = 365, hours = 6, minutes = 9, seconds = 9, milliseconds = 76)
earth = CicularOrbit(earthDistance, earthYear, 0)

moonDistance = 238900
moonYear = timedelta(days = 29.53059)
moon = CicularOrbit(moonDistance, moonYear, 0, earth)

testdate = datetime(2022,9,15)

print(earth.getPosAt(testdate))
print(moon.getPosAt(testdate))