# program to calculate the radius of 2 planets that are under a flux of asteroids. I assume a perfectly non elastic collision, a spherical surface for each planet and that they have the same density.
# Later on, it would be nice if v0 gets updated and picked with a gaussian distribution centered near 30 km/s with some small standard deviation

import random
G = 6.67408 * 10**-11 # gravitational constant in SI
rho = 1000 # density: 1000 kg /m^3, water density
v0 = 40000 # original speed of asteroid in m/s
r1 = 1500000 # radius of planet 1 in meters
r2 = 1700000 # radius of planet 2 in meters
r01 = r1
r02 = r2
massasteroid = 10**15 # mass of the asteroid in kg
V1 = (4 / 3) * 3.14159265 * r1**3
V2 = (4 / 3) * 3.14159265 * r2**3

y1squared = r1**2 + (8 * 3.14159265 *G* rho*r1**4) / (3 * v0**2) #radius squared of the cross section for planet 1
y2squared = r2**2 + (8 * 3.14159265 *G* rho*r2**4) / (3 * v0**2) #radius squared of the cross section for planet 2
quotient = y2squared/y1squared 

counter = 0
for i in range(1,1000000):  # number of asteroids
	prob1= 1 / ( quotient + 1)
	if random.random() < prob1: # if the 1st planet has been hit by an asteroid then:
		
		r1 = r1 * ((rho*V1 + massasteroid) / (rho * V1))**(1/3) # update the radius of the planet, where V1 is the volume of the planet before the hit
		y1squared = r1**2 + (8 * 3.14159265 *G* rho*r1**4) / (3 * v0**2) #update the cross section radius
		quotient = y2squared/y1squared #update also the quotient
		V1 = (4 / 3) * 3.14159265 * r1**3 # update the volume now
	else: # the 2nd planet has been hit
		r2 = r2 * ((rho*V2 + massasteroid) / (rho * V2))**(1/3)
		y2squared = r2**2 + (8 * 3.14159265 *G* rho*r2**4) / (3 * v0**2)
		quotient = y2squared/y1squared
		V2 = (4 / 3) * 3.14159265 * r2**3
	counter = counter +1


print('The number of asteroids is',counter)
print('The radius of planet 1 is x times bigger than originally', r1/r01,r1)
print('The radius of planet 2 is y times bigger than originally ', r2/r02,r2)
