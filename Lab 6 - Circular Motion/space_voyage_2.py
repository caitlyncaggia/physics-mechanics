# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
scene.width =1024
scene.height = 760

#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15000
mMoon = 7e22
deltat = 10
pscale = 2
fscale = 40000
dpscale = 150

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
scene.range=80*Earth.radius
Moon = sphere(pos=vector(4e8,0,0), radius=1.75e6, color=color.white)
# Choose an exaggeratedly large radius for the
# space craft so that you can see it!
craft = sphere(pos=vector(-6.4e7, 0,0), color=color.yellow)
vcraft = vector(0,3.27e3,0)
pcraft = mcraft*vcraft

parr = arrow(color=color.green)
#farr = arrow(color=color.cyan)
#dparr = arrow(color=color.red)
Fnet_tangent_arrow = arrow(color = color.yellow)
Fnet_perp_arrow = arrow(color=color.magenta)


trail = curve(color=craft.color)    ## craft trail: starts with no points
t = 0
scene.autoscale = 0       ## do not allow camera to zoom in or out

#CALCULATIONS

print('p=', pcraft)

while t < 90120000:
    rate(2000)       ## slow down motion to make animation look nicer
    ## you must add statements for the iterative update of 
    ## gravitational force, momentum, and position
    
    r1 = craft.pos - Earth.pos
    rmag1 = mag(r1)
    FmagE = (-G * mcraft* mEarth)/rmag1**2
    rhat1 = r1/rmag1
    Fearth = FmagE * rhat1

    r2 = craft.pos - Moon.pos
    rmag2 = mag(r2)
    FmagM = (-G * mcraft * mMoon)/rmag2**2
    rhat2 = r2/rmag2
    Fmoon = FmagM * rhat2
    
    Fnet = Fearth + Fmoon

    pcrafti = pcraft
    p_init = mag(pcrafti)
    
    pcraft = pcraft + Fnet*deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    p_final = mag(pcraft)

    p = pcraft - pcrafti
    phat = pcraft/mag(pcraft)

    Fnet_tangent =( (p_final - p_init)/deltat ) * phat
    Fnet_perp = Fnet - Fnet_tangent
    

    if rmag1 < Earth.radius:
        break

    if rmag2 < Moon.radius:
        break


    parr.pos = craft.pos
    parr.axis = pcraft * pscale

    #farr.pos = craft.pos
    #farr.axis = Fnet * fscale

    deltap = pcraft - pcrafti
    #dparr.pos = craft.pos
    #dparr.axis = deltap * dpscale

    Fnet_tangent_arrow.pos = craft.pos
    Fnet_tangent_arrow.axis = phat * fscale * 1000

    Fnet_perp_arrow.pos = craft.pos
    Fnet_perp_arrow.axis = Fnet_perp * fscale * 10
    
    
    ## check to see if the spacecraft has crashed on the Earth.
    ## if so, get out of the calculation loop
    

    trail.append(pos=craft.pos) ## this adds the new position of the spacecraft to the trail
    t = t+deltat

    #print('pmag = ', mag(pcraft))
    #print('speed = ', mag(pcraft/mcraft))
    #print('F_perp = ', mag(Fnet_perp))
    #print('separation = ', mag(r1))

    #scene.center=craft.pos
    #scene.range=craft.radius*60

#print('Fnet=', Fnet)
print('Final position =', craft.pos)
print('Final velocity =', pcraft/mcraft)
print('Fg =',Fnet)
#print('Calculations finished after ',t,'seconds')
