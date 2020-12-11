from __future__ import division                 ## treat integers as real numbers in division
from visual import *
from visual.graph import *
scene.width=600
scene.height = 760


## Setup graphing windows
gdisplay(width=500, height=250, x=600, y=1)
gdisplay(width=500, height=250, x=600, y=300)
#pgraph = gcurve(color=color.yellow)
#ygraph = gcurve(color=color.yellow)
U_graph = gcurve(color=color.blue) #A plot of the Potential energy
K_graph = gcurve(color=color.yellow) #A plot of the Kinetic energy
Energy_graph = gcurve(color=color.green) #A plot of the Total energy
Energy_2 = gcurve(color=color.red)

## constants and data
g = 9.8
mball = 0.2134 #kilograms
L0 = 0.3   #meters
ks = 12  #Newtons/meter
deltat = 1e-3 #seconds
pscale = 0.5
fscale = 0.06
gScale = 0.1
sScale = 0.04

t = 0      

## objects
ceiling = box(pos=(0,0,0), size = (0.2, 0.01, 0.2))         ## origin is at ceiling
ball = sphere(pos=(0.2394, -0.1059, -0.2637), radius=0.025, color=color.orange) ## note: spring initially compressed
spring = helix(pos=ceiling.pos, color=color.cyan, thickness=.003, coils=40, radius=0.015) ## change the color to be your spring color
spring.axis = ball.pos - ceiling.pos
trail = curve(color=ball.color)

## initial values
vBall = vector(-0.067, 0.432, 0.08)
ball.p = mball*vBall

## improve the display
#scene.autoscale = 0             ## don't let camera zoom in and out as ball moves
scene.center = vector(0,-L0,0)   ## move camera down to improve display visibility

## calculation loop

pArrow = arrow(pos = ball.pos, axis = ball.p * pscale, color = color.red)
fnetArrow = arrow(pos = ball.pos, color = color.white)
gravArrow = arrow(pos = ball.pos, color = color.green)
sArrow = arrow(pos = ball.pos, color = color.yellow)
while t < 3.681:           ## make this short to read period off graph
    rate(500)
    r = spring.axis
    rMag = mag(r)
    rHat = r/rMag
    s = rMag - L0
    Fspring = -(ks*s) * rHat
    Fgrav = vector(0, -mball*g, 0)
    ballphat = norm(ball.p)
    Fdrag = 6*pi*0.081*ball.radius*-ballphat
    Fnet = Fspring + Fgrav + Fdrag 
    ball.p = ball.p + Fnet * deltat
    ball.pos = ball.pos + (ball.p/mball)*deltat
    spring.axis = ball.pos - ceiling.pos

    
    
    pArrow.pos = ball.pos
    pArrow.axis = ball.p * pscale
    fnetArrow.pos = ball.pos
    fnetArrow.axis = Fnet * fscale
    gravArrow.pos = ball.pos
    gravArrow.axis = Fgrav * gScale
    sArrow.pos = ball.pos
    sArrow.axis = Fspring * sScale
    trail.append(pos=ball.pos)
     
    t = t + deltat
    #pgraph.plot(pos=(t, ball.p.y))
    #ygraph.plot(pos=(t, Fnet.y))
    K =  .5*mball*(mag(ball.p)/mball)**2             #Initial kinetic energy of the spacecraft
    U_Earth = mball*g*(ball.pos.y-ceiling.pos.y)          #Craft + Earth interaction energy
    U_spring =  .5*ks*(s)**2       #Craft + Moon interaction energy
    E1 = K + U_Earth + U_spring         #Approximate Total energy
    E2 = K + U_spring

    U_graph.plot(pos=(t,U_Earth+U_spring))    #Potential energy as a function of time
    K_graph.plot(pos=(t,K))                       #Kinetic energy as a function of time
    Energy_graph.plot(pos=(t,E1))   #Total energy as a function of time
    Energy_2.plot(pos=(t,E2))

    

print ("Final position of ball: ",ball.pos)
print ("Final velocity of ball: ",ball.p/mball)
print ("Final parallel component of net force: ",ball.pos)
print ("Final perpendicular component of net force: ",ball.p/mball)
