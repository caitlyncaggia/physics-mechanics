from __future__ import division
from visual import *
baseball = sphere(pos=vector(-4,-2,5), radius=0.40, color=color.red)
tennisball = sphere(pos=vector(3,1,2), radius=0.15, color=color.green)
bt = arrow(pos=baseball.pos, axis=(tennisball.pos - baseball.pos), color=color.cyan)

arrow(pos=bt.pos, axis=vector(bt.axis.x,0,0), color=color.yellow)
arrow(pos=bt.pos, axis=vector(0,bt.axis.y,0), color=color.yellow)
arrow(pos=bt.pos, axis=vector(0,0,bt.axis.z), color=color.yellow)

