from __future__ import division
from visual import *
from visual.graph import * ##Invoke graphing routines
scene.y = 400 ##Move orbit window below graph
scene.width =1024
scene.height = 760

#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15000
mMoon = 0
deltat = 60
pscale = 2
fscale = 4000
dpscale = 150

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
scene.range=80*Earth.radius
Moon = sphere(pos=vector(4e8,0,0), radius=1.75e6, color=color.white)
# Choose an exaggeratedly large radius for the
# space craft so that you can see it!
craft = sphere(pos=vector(-64640000, -6208000,0), color=color.yellow)
vcraft = vector(814,2877,0)
pcraft = mcraft*vcraft
vMoon = sqrt((G*mEarth)/mag(Moon.pos - Earth.pos))
vMoon = vector(0,vMoon,0)
pMoon = mMoon * vMoon

parr = arrow(color=color.green)
#farr = arrow(color=color.cyan)
#dparr = arrow(color=color.red)
Fnet_tangent_arrow = arrow(color = color.yellow)
Fnet_perp_arrow = arrow(color=color.magenta)


trail = curve(color=craft.color)    ## craft trail: starts with no points
mtrail = curve(color=Moon.color)
t = 0
scene.autoscale = 0       ## do not allow camera to zoom in or out

#CALCULATIONS

print('p=', pcraft)
U_graph = gcurve(color=color.blue) #A plot of the Potential energy
K_graph = gcurve(color=color.yellow) #A plot of the Kinetic energy
Energy_graph = gcurve(color=color.green) #A plot of the Total energy


while t < 385680:
    rate(20000000000)       ## slow down motion to make animation look nicer
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
    

    trail.append(pos=craft.pos) ## this adds the new position of the spacecraft to the trail

    #print('pmag = ', mag(pcraft))
    #print('speed = ', mag(pcraft/mcraft))
    #print('F_perp = ', mag(Fnet_perp))
    #print('separation = ', mag(r1))

    #scene.center=craft.pos
    #scene.range=craft.radius*60

##    K_craft =  .5*mcraft*(mag(pcraft)/mcraft)**2             #Initial kinetic energy of the spacecraft
##    U_craft_Earth = (-G*mEarth*mcraft)/mag(r1)          #Craft + Earth interaction energy
##    U_craft_Moon =  (-G*mEarth*mcraft)/mag(r2)        #Craft + Moon interaction energy
##    E = K_craft + U_craft_Earth + U_craft_Moon         #Approximate Total energy
##
##    U_graph.plot(pos=(t,U_craft_Earth+U_craft_Moon))    #Potential energy as a function of time
##    K_graph.plot(pos=(t,K_craft))                       #Kinetic energy as a function of time
##    Energy_graph.plot(pos=(t,E))                        #Total energy as a function of time
##
##
##    r_EarthMoon = Moon.pos - Earth.pos          #Relative position vector from Earth to Moon
##    r_craftMoon = Moon.pos - craft.pos          #Relative position vector from spacecraft to Moon
##    r_EarthMoon_hat = r_EarthMoon/mag(r_EarthMoon)
##    r_craftMoon_hat = r_craftMoon/mag(r_craftMoon)
##    Force_EarthMoon = ((-G*mEarth*mMoon)/mag(r_EarthMoon)**2)*r_EarthMoon_hat     #Force on Moon due to Earth
##    Force_craftMoon = ((-G*mcraft*mMoon)/mag(r_craftMoon)**2)*r_craftMoon_hat      #Force on Moon due to spacecraft
##    Fnet_Moon = Force_EarthMoon + Force_craftMoon        #Net force on Moon
##
##    pMoon = pMoon + Fnet_Moon * deltat            #Update momentum of Moon
##    Moon.pos = Moon.pos + (pMoon/mMoon)*deltat        #Update momentum of Moon
##
##    mtrail.append(pos= Moon.pos) ## this adds the new position of the spacecraft to the trail

    t = t+deltat

#print('Fnet=', Fnet)
print('Final position =', craft.pos)
print('Final velocity =', pcraft/mcraft)
print('Fg =',Fnet)
#print('Calculations finished after ',t,'seconds')
print('Fperp = ', Fnet_perp)
print('mag Fperp = ', mag(Fnet_perp))
print('mag Fparallel = ', mag(Fnet_tangent))
