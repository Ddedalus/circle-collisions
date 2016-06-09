from Body import *
import numpy as np
from numpy.linalg import inv


def collide(b, r):
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
	we_b = (b.u[1] * (r.m - b.m) + 2 * r.m * r.u[1]) / (b.m + r.m)
	we_r = (r.u[1] * (b.m - r.m) + 2 * b.m * b.u[1]) / (b.m + r.m)
	b.u[1] = we_b
	r.u[1] = we_r
	for k in [b, r]:
		k.new_v = np.dot(de_to_xy, k.u)

	pos = b.pos
	b.step()
	b.u, r.u = None, None
	r.step()
	return pos


def switch_to_masspoint(b, r):
	vx = (b.m * b.v[0] + r.m * r.v[0]) / (b.m + r.m)
	vy = (b.m * b.v[1] + r.m * r.v[1]) / (b.m + r.m)
	
	for k in [b, r]:
		k.v = k.v - np.array([vx, vy])
	
	return b, r
