from __future__ import division
from visual import *
from visual.graph import *
scene.y=400

# Turn off autoscaling
autoscale=0

# Create objects: ground, cliff, cannon
# Ground is at y=0
# Ball initial position is initialPos
# Ball initial velocity is initial Pos height is 1000 m
# Ball size is enlarged for viewing.  For calculations, consider it to be 2 m diameter

# Initial Conditions
initialPos = vector(8.4,98.9,0)
initialVel = vector(52,52.3,0)

# Setup the scene
ground = box(pos=(0,0,0), length = 800, height = 1, width = 10, color=color.green)
cliff = box(pos=(initialPos.x-40,initialPos.y/4-1,0), length = ground.length/2+initialPos.x, height = initialPos.y, width = 10, color=color.green)

# Make Cannon
L=10
wheel = cylinder(pos=initialPos, axis=vector(0,0,1),radius=5, color=color.blue)
cannon = cylinder(pos=initialPos, axis=L*initialVel/mag(initialVel), radius=1)

# Setup ball and trail
ball = sphere(pos=initialPos, radius = 1, color=color.red)
trail = curve(color=ball.color)

# Constants
ball.m = 57.3    # ball's mass 
g = 9.8      # gravitational acceleration
pScale = 0.05  # scale for momentum arrow
fScale = 0.1  # scale for force arrow

# Drag constants
airDensity = 1.3        # density of air near the surface of the Earth
areaBall = pi*1**2    # cross-sectional area of the ball (diameter 2m)
dragCoeff = 0.1006       # drag coefficient for this ball

# Initialize ball's momentum
ball.p=ball.m*initialVel
pmag = mag(ball.p)
phat = ball.p/pmag

# Time Setup
t = 0
deltat = 1e-2

#Setup Force and momentum Arrows
pArrow = arrow(pos=initialPos, color=color.red)
fArrow = arrow(pos=initialPos, color=color.white)
fperpArrow = arrow(pos=initialPos, color=color.blue)
fparaArrow = arrow(pos=initialPos, color=color.green)

# This while loop, below, models the motion of the ball after it leaves the cannon
# Motion coninues until the ball's height reaches zero.

# MODIFY THE CODE IN THIS LOOP according to the instructions in the lab handout.
Kgraph=gcurve(color=color.red)
Ugraph=gcurve(color=color.cyan)
KplusUgraph=gcurve(color=color.yellow)


while t < 6.291:
    
    rate(1000)
    # Calculate the net force on the ball
    Fair = -.5*airDensity*areaBall*dragCoeff*(mag(ball.p/ball.m)**2)*phat
    Fnet = vector(0,-ball.m*g,0) + Fair
    ball.pi = ball.p
    Fmag = mag(Fnet)
    
        
    # Update the momentum of the ball
    ball.p = ball.p + Fnet*deltat
    pmag = mag(ball.p)
    phat = ball.p/pmag
        
    # Update the position of the ball
    ball.pos = ball.pos + (ball.p/ball.m)*deltat

    K = .5*ball.m*(mag(ball.p)/ball.m)**2
    U = ball.m*g*ball.pos.y
    
    # Update the trails of the ball
    trail.append(pos=ball.pos)
           
    # Calculate the force components
    F_tangent = (mag(ball.pi)- mag(ball.p))*phat/deltat
    F_tangentmag = mag(F_tangent)
    F_perpmag = sqrt((Fmag)*(Fmag) - (F_tangentmag)*(F_tangentmag))
    F_perp = Fnet - F_tangent

    #Find radius of the kissing circle
    ball.v = pmag/ball.m
    R = (ball.m*(ball.v)**2)/F_perpmag
    
    # Update the arrows representing the momentum, force and force components
    pArrow.axis = pScale*ball.p
    pArrow.pos = ball.pos

    fperpArrow.axis = fScale*F_perp
    fperpArrow.pos = ball.pos

    fparaArrow.axis = fScale*F_tangent
    fparaArrow.pos = ball.pos
    

    
    
    Kgraph.plot(pos=(t,K))
    Ugraph.plot(pos=(t,U))
    KplusUgraph.plot(pos=(t,K+U))
    
    # Update time
    t = t + deltat



    
print ("time=", t, "s")


pmag = mag(ball.p)

# In addition to time, print the final values of the following quantities:
print ("Speed is", (pmag/ball.m))
print ("X Velocity is", (ball.p.x/ball.m))
print ("Y Velocity is",(ball.p.y/ball.m))
print ("X position is", (ball.pos.x))
print ("Y position is", (ball.pos.y))
print ("Fperp", (F_perpmag))
print ("Fparr", (F_tangentmag))
print ("radius", R)

# magnitude of ball's velocity
# x-component of ball's velocity
# y-component of ball's velocity
# x-position of ball
