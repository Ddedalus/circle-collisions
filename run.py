# -*- coding: utf-8 -*-
from collider import *
from ploter import *
from Body import *
import copy

it = 20
bill_0 = Body(1., 0., [0., 0.], [1., 1.])
ring_0 = Body(2., 4., [0., 0.], [0., 0.])

init_angle(bill_0, ring_0, math.pi / 5.0)
plot_bodies(bill_0, ring_0, 'Initial position')

bill_i, ring_i = copy.copy(bill_0), copy.copy(ring_0)
switch_to_masspoint(bill_i, ring_i)


bill_r, ring_r = copy.copy(bill_0), copy.copy(ring_0)
# switch_to_masspoint(bill_r, ring_r) # - causes crash
ring_r.v = np.array([0., 0.])

pos_rigid = [bill_r.pos]
pos_inertial = [bill_i.pos]

for i in range(it):
	bill_r, ring_r = collide_rigid(bill_r, ring_r)
	bill_i, ring_i = collide_inertial(bill_i, ring_i)
	pos_rigid.append(list(bill_r.pos))
	pos_inertial.append(bill_i.pos)


# plot paths
def ploter():
	plt.plot(*zip(*pos_rigid), color='r')
	plt.autoscale()
	plt.axis('equal')
	plt.title("Rigid path")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('pos rigid.png')
	plt.title("Both paths")
	plt.plot(*zip(*pos_inertial), color='b')
	plt.savefig('pos both.png')

	plt.close()

	plt.plot(*zip(*pos_inertial), color='b')
	plt.autoscale()
	plt.axis('equal')
	plt.title("Inertial path")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('pos inertial.png')
	plt.close()


ploter()
def ploter2():
	plt.plot(*zip(*pos_inertial), color='r')
	plt.autoscale()
	plt.axis('equal')
	plt.title("pi/8 path graph")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('pos pi_3.png')
	plt.close()
