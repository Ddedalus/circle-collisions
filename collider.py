# -*- coding: utf-8 -*-from Body import *
import numpy as np
from numpy.linalg import inv, norm
import math
import copy, logging
from Body import len_sq


def collide_inertial(bill, ring):
	b = copy.copy(bill)
	r = copy.copy(ring)
	# mass, radius, x, y, vx, vy

	A = b.v_sq() + r.v_sq() - 2 * np.dot(b.v, r.v)
	B = 2 * ((b.pos[0] - r.pos[0]) * (b.v[0] - r.v[0]) + (b.pos[1] - r.pos[1]) * (b.v[1] - r.v[1]) )
	C = (b.pos[0] - r.pos[0])**2 + (b.pos[1] - r.pos[1])**2 - (b.r - r.r)**2
	D = B**2 - 4 * A * C        # discriminant of L**2 = (b.r - r.r)**2

	if D < 0:
		print("Negative discriminant:", D, "no ongoing collision...")
		return 1

	t1 = (-B + D**0.5) * 0.5 / A
	t2 = (-B - D**0.5) * 0.5 / A
	t = max(t1, t2)

	for k in [b, r]:
		k.new_pos = k.pos + t * k.v

	sin_f = (b.new_pos[0] - r.new_pos[0]) / len_sq(b, r, new=True) ** 0.5
	cos_f = (b.new_pos[1] - r.new_pos[1]) / len_sq(b, r, new=True) ** 0.5
	# angle between x-y and d-e coordinates
	# d is tangent to both circles in point of collision
	xy_to_de = np.array([[cos_f, - sin_f], [sin_f, cos_f]])
	de_to_xy = inv(xy_to_de)
	# coordinates transformation matrix

	for k in [b, r]:
		k.u = np.dot(xy_to_de, k.v)
	# velocities in new coordinates

	# collision
	we_b = (b.u[1] * (b.m - r.m) + 2 * r.m * r.u[1]) / (b.m + r.m)
	we_r = (r.u[1] * (r.m - b.m) + 2 * b.m * b.u[1]) / (b.m + r.m)
	b.u[1] = we_b
	r.u[1] = we_r
	for k in [b, r]:
		k.new_v = np.dot(de_to_xy, k.u)

	b.step()
	b.u, r.u = None, None
	r.step()
	return b, r
	
	
# ----------------------------------------------------------------------------- #
# -------------------------      collide rigid     ---------------------------- #
# ----------------------------------------------------------------------------- #


def collide_rigid(bill, ring):
	"""Mass of ring is infinite, and it's speed is zero"""

	b = copy.copy(bill)
	r = copy.copy(ring)
	# b.pos -= r.pos  # switch to center of ring

	logging.info("Mass of ring treated now as infinite.")
	if norm(r.v) > 0.0000001:
		print('Warning, ignoring ring velocity!')
	
	# print('Velocity of b', b.v)
	if norm(b.v) == 0.:
		print('Error, zero bill velocity!')
		return 1
	
	A = norm(b.v)**2
	B = 2 * (b.pos[0] * b.v[0] + b.pos[1] * b.v[1])
	C = (norm(b.pos))**2 - (r.r - b.r)**2
	D = B**2 - 4 * A * C        # discriminant of L**2 = (b.r - r.r)**2
	t1 = (-B + D**0.5) * 0.5 / A
	t2 = (-B - D**0.5) * 0.5 / A
	t = max(t1, t2)

	b.new_pos = b.pos + t * b.v
	
	# not sure which angle it actually is...
	sin_f = b.new_pos[0] / norm(b.new_pos)
	cos_f = b.new_pos[1] / norm(b.new_pos)
	# angle between x-y and d-e coordinates
	# d is tangent to both circles in point of collision
	xy_to_de = np.array([[cos_f, - sin_f], [sin_f, cos_f]])
	de_to_xy = inv(xy_to_de)
	# coordinates transformation matrix

	b.u = np.dot(xy_to_de, b.v)
	b.u[1] = - b.u[1]
	# velocity in new coordinates, collision on line e
	
	b.new_v = np.dot(de_to_xy, b.u)
	# print('b.new_v=', b.new_v)
	# collision, check this twice

	pos = b.pos
	b.step()
	b.u = None
	return b, r


def switch_to_masspoint(b, r):
	vx = (b.m * b.v[0] + r.m * r.v[0]) / (b.m + r.m)
	vy = (b.m * b.v[1] + r.m * r.v[1]) / (b.m + r.m)
	v = (b.v * b.m + r.v * r.m)/(b.m + r.m)
	x = (b.m * b.pos[0] + r.m * r.pos[0]) / (b.m + r.m)
	y = (b.m * b.pos[1] + r.m * r.pos[1]) / (b.m + r.m)
	pos = (b.pos * b.m + r.pos * r.m)/(b.m + r.m)
	for k in [b, r]:
		k.v = k.v - v
		k.pos = k.pos - pos

	print('Momentum:', b.v * b.m + r.v * r.m)
	print('Masspoint:', b.pos * b.m + r.pos * r.m)


def init_angle(bill, ring, fi=0, velocity=1.):
	# works properly in max range only with ring.pos=[0 0]
	y = ring.r * (1. - math.cos(2 * fi)) * 0.5
	x = - ring.r * math.sin(2 * fi) * 0.5
	# in coordinates according to ring's center

	bill.pos = np.array([x, y]) + ring.pos
	bill.v = np.array([math.sin(fi) * velocity, math.cos(fi) * velocity])

	if np.linalg.norm(ring.pos - bill.pos) > ring.r - bill.r:
		print('Warning: Angle over limit!', fi)
		return 1

	return 0


def summary_momentum(bill, ring):
	return bill.v * bill.m + ring.v * ring.m


def run_inertial(bill, ring, it=10):
	pos_b = [bill.pos]
	rad_b = [np.linalg.norm(bill.pos)]
	b = copy.copy(bill)
	r = copy.copy(ring)
	switch_to_masspoint(b, r)

	for i in range(it):
		b, r = collide_inertial(b, r)
		pos_b.append(b.pos)
		# rad_b.append(np.linalg.norm(bill.pos))

	# print(pos_b[-1])
	# print('Radius:', bill.radius())

	return pos_b
