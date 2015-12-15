# program to calculate the radius of 2 planets that are under a flux of asteroids. I assume a perfectly non elastic collision, a spherical surface for each planet and that they have the same density.

G=6.67408*10**-11 #gravitational constant in SI
rho=1000 #density: 1000 kg /m^3, water density
v0=40000 #original speed of asteroid in m/s
r1=1500 #radius of planet 1 in meters
r2=3000 # radius of planet 2 in meters

y1squared = r1**2 + (8 * 3.14159265 *G* rho*r1**4) / (3 * v0**2) #radius squared of the cross section for planet 1
y2squared = r2**2 + (8 * 3.14159265 *G* rho*r2**4) / (3 * v0**2) #radius squared of the cross section for planet 2

quotient = y2squared/y1squared 
prob1= 1 / ( quotient + 1)

print('The probability of planet 1 to be hit is',prob1)

#if random.random() < 0.2:
