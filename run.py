# -*- coding: utf-8 -*-
from collider import *
from ploter import *
from Body import *


bill = Body(1., 1, [0., 0.], [0., 1.])
ring = Body(2., 4, [0., 0.], [0., 0.])
# init_angle(bill, ring, 0.5)
# switch_to_masspoint(bill, ring)

# pos_b, rad_b = run(bill, ring, 50)

pos_rigid = [bill.pos]
for i in range(10):
	collide_rigid(bill, ring)
	pos_rigid.append(bill.pos)
	print('New position:', bill.pos)
	print('New velocity:', bill.v)

# plot_vs_collision(rad_b, 51, "Radius")
# plot_pos(pos_rigid)