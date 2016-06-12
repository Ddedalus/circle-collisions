from collider import *
from numpy.linalg import norm


bill = Body(1, 1, [0, 0], [1, 1])
ring = Body(2, 4, [0, 0], [0, 0])
pos_b = [bill.pos]
print('Pęd początkowy:', bill.v * bill.m + ring.v * ring.m)

switch_to_masspoint(bill, ring)
print('Pęd masspoint:', bill.v * bill.m + ring.v * ring.m)

for i in range(10):
	pos_b.append(collide(bill, ring))
	# print(pos_b[-1])
	print('Pęd', i+1, ':', bill.v * bill.m + ring.v * ring.m)