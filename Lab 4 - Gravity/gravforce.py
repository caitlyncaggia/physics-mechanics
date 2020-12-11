from __future__ import division
from visual import *

G = 6.7e-11
mcraft = 15e3
mplanet = 6e24
Fscale = -40000

planet = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.blue)
craft1 = sphere(pos=vector(-13e7, 6.5e7,0), radius=3e6, color=color.red)
craft2 = sphere(pos=vector(-6.5e7, 6.5e7,0), radius=3e6, color=color.red)
craft3 = sphere(pos=vector(0, 6.5e7,0), radius=3e6, color=color.red)
craft4 = sphere(pos=vector(6.5e7, 6.5e7,0), radius=3e6, color=color.red)
craft5 = sphere(pos=vector(13e7, 6.5e7,0), radius=3e6, color=color.red)

#part 4 - calculate force of gravity
r = craft1.pos - planet.pos
rmag = mag(r)
Fmag = (-G * mcraft* mplanet)/(rmag)**2
rhat = r/rmag
Fnet = -Fmag * rhat
print("Fnet =", Fnet)

arr1 = arrow(pos=craft1.pos, axis=Fnet*Fscale, color=color.yellow)


#part 8 - add the other spacecrafts

r2 = craft2.pos - planet.pos
rmag2 = mag(r2)
Fmag2 = (-G * mcraft* mplanet)/(rmag2)**2
rhat2 = r2/rmag2
Fnet2 = -Fmag2 * rhat2
arr2 = arrow(pos=craft2.pos, axis=Fnet2*Fscale, color=color.yellow)

r3 = craft3.pos - planet.pos
rmag3 = mag(r3)
Fmag3 = (-G * mcraft* mplanet)/(rmag3)**2
rhat3 = r3/rmag3
Fnet3 = -Fmag3 * rhat3
arr3 = arrow(pos=craft3.pos, axis=Fnet3*Fscale, color=color.yellow)

r4 = craft4.pos - planet.pos
rmag4 = mag(r4)
Fmag4 = (-G * mcraft* mplanet)/(rmag4)**2
rhat4 = r4/rmag4
Fnet4 = -Fmag4 * rhat4
arr4 = arrow(pos=craft4.pos, axis=Fnet4*Fscale, color=color.yellow)

r5 = craft5.pos - planet.pos
rmag5 = mag(r5)
Fmag5 = (-G * mcraft* mplanet)/(rmag5)**2
rhat5 = r5/rmag5
Fnet5 = -Fmag5 * rhat5
arr5 = arrow(pos=craft5.pos, axis=Fnet5*Fscale, color=color.yellow)

#Part 9 - label an arrow
label(pos=vector(craft3.pos.x, craft3.pos.y - 6.5e7/2, craft3.pos.z), text='Force of Gravity on Craft 3')
label(pos=planet.pos, text = 'Planet')
label(pos=craft3.pos, text = 'Spacecraft 3')




