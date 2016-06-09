from collider import *


bill = Body(1, 1, x=0, y=0, vx=1, vy=1)
ring = Body(2, 4, x=0, y=0, vx=0, vy=0)
pos_b = [[bill.x, bill.y]]

switch_to_massspoint(bill, ring)

for i in range(50):
	pos_b.append(collide(bill, ring))
	print(pos_b[-1])