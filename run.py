from collider import *
import math

bill = Body(1, 1, [0.5, 0], [1, 1])
ring = Body(6.5, 4, [0, 0], [0, 0])


def run(bill, ring, it=10):
	pos_b = [bill.pos]
	rad_b = [bill.radius()]
	print('Pęd układu:', summary_momentum(bill, ring))

	for i in range(it):
		collide(bill, ring)
		pos_b.append(bill.pos)
		rad_b.append(bill.radius())

		# print(pos_b[-1])
		print('Radius:', bill.radius())

	return pos_b, rad_b

def init_angle(bill,  radius, fi = 0):
	a = math.tan(fi)
	bill.pos[0] = - (a * radius)/(a**2 + 1.)
	bill.pos[1] = radius - radius/(a ** 2 + 1.)
	bill.v = np.array([math.sin(fi), math.cos(fi)])


for k in range(10):
	init_angle(bill, ring.r, math.pi * k / 25.)
	print(bill.pos)