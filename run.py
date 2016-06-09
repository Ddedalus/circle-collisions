from collider import *


bill = Body(1, 1, [0, 0], [1, 1])
ring = Body(1, 4, [0, 0], [0, 0])
pos_b = [bill.pos]

for i in range(50):
	pos_b.append(collide(bill, ring))
	print(pos_b[-1])