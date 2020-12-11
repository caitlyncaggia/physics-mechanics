# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
scene.width =1024
scene.height = 760

#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat = 60
pscale = 0.2
fscale = 800
dpscale = 15

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
scene.range=11*Earth.radius
# Choose an exaggeratedly large radius for the
# space craft so that you can see it!
craft = sphere(pos=vector(-6.336e7, -3.584e6,0), color=color.yellow)
vcraft = vector(519,2851,0)
pcraft = mcraft*vcraft

parr = arrow(color=color.green)
farr = arrow(color=color.cyan)
dparr = arrow(color=color.red)

trail = curve(color=craft.color)    ## craft trail: starts with no points
t = 0
scene.autoscale = 0       ## do not allow camera to zoom in or out

#CALCULATIONS

print('p=', pcraft)

while t < 2270592:
    rate(200)       ## slow down motion to make animation look nicer
    ## you must add statements for the iterative update of 
    ## gravitational force, momentum, and position
    
    r = craft.pos - Earth.pos
    rmag = mag(r)
    Fmag = (-G * mcraft* mEarth)/(rmag)**2
    rhat = r/rmag
    Fnet = Fmag * rhat

    pcrafti = pcraft
    
    pcraft = pcraft + Fnet*deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat

    if rmag < Earth.radius:
        break

    parr.pos = craft.pos
    parr.axis = pcraft * pscale

    farr.pos = craft.pos
    farr.axis = Fnet * fscale

    deltap = pcraft - pcrafti
    dparr.pos = craft.pos
    dparr.axis = deltap * dpscale
    
    ## check to see if the spacecraft has crashed on the Earth.
    ## if so, get out of the calculation loop
    

    trail.append(pos=craft.pos) ## this adds the new position of the spacecraft to the trail
    t = t+deltat

#print('Fnet=', Fnet)
print('Final position =', craft.pos)
print('Final velocity =', pcraft/mcraft)
#print('Calculations finished after ',t,'seconds')
