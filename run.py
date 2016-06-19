# -*- coding: utf-8 -*-
from collider import *
from ploter import *
from Body import *
from numpy.linalg import norm
import math


def angle(pos1, pos2, pos3):
	cos = -0.5 * (norm(pos1 - pos3) ** 2 - norm(pos1 - pos2) ** 2 - norm(pos2 - pos3) ** 2) / (norm(
		pos1 - pos2) * norm(pos2 - pos3))
	return math.acos(cos)


bill_0 = Body(1., 1, [1., 1.], [2., 1.])
ring_0 = Body(2., 4, [0., 0.], [0., 0.])
# init_angle(bill, ring, 0.5)
# switch_to_masspoint(bill, ring)

# pos_b, rad_b = run(bill, ring, 50)
def run_rigid():
	pos_rigid = [bill_0.pos]
	bill, ring = bill_0, ring_0
	for i in range(10):
		bill, ring = collide_rigid(bill, ring)
		pos_rigid.append(bill.pos)
		print('New position:', bill.pos)
	# print('New velocity:', bill.v)

	# plot_vs_collision(rad_b, 51, "Radius")
	plot_pos(pos_rigid)

	angles = []
	for i in range(1, 9):
		angles.append(angle(pos_rigid[i-1], pos_rigid[i], pos_rigid[1+i]))

	plot_vs_collision(angles, len(angles))


pos_inertial = run_inertial(bill_0, ring_0, 50)
angles = []
for i in range(1, 49):
	angles.append(angle(pos_inertial[i-1], pos_inertial[i], pos_inertial[1+i]))
plot_vs_collision(angles, len(angles), 'Angle in inertial')
