# -*- coding: utf-8 -*-
from collider import *
from ploter import *
from Body import *

it = 100
bill_0 = Body(1., 1., [0., 0.], [1., 1.])
ring_0 = Body(2., 4., [0., 0.], [0., 0.])
switch_to_masspoint(bill_0, ring_0)
init_angle(bill_0, ring_0, math.pi/8.0)
plot_bodies(bill_0, ring_0, 'Initial position')

pos_rigid = [bill_0.pos]
pos_inertial = [bill_0.pos]
bill_i, ring_i = bill_0, ring_0
bill_r, ring_r = bill_0, ring_0

for i in range(it):
	bill_r, ring_r = collide_rigid(bill_r, ring_r)
	bill_i, ring_i = collide_rigid(bill_i, ring_i)
	pos_rigid.append(list(bill_r.pos))
	pos_inertial.append(bill_i.pos)

#plot paths
def ploter():
	plt.plot(*zip(*pos_rigid), color='r')
	plt.axis('equal')
	plt.title("Rigid path graph")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('pos rigid.png')
	plt.plot(*zip(*pos_inertial), color='b')
	plt.savefig('pos both.png')
	
	plt.close()
	
	plt.plot(*zip(*pos_inertial), color='b')
	plt.axis('equal')
	plt.title("Inertial path graph")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('pos inertial.png')
	plt.close()
	
# ploter()
plt.plot(*zip(*pos_inertial), color='r')
plt.axis('equal')
plt.title("pi/8 path graph")
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('pos pi_8.png')
plt.close()