from collider import *

bill = Body(1, 1, [0.5, 0], [1, 1])
ring = Body(6.5, 4, [0, 0], [0, 0])
pos_b = [bill.pos]

switch_to_masspoint(bill, ring)
print('Pęd układu:', summary_momentum(bill, ring))

for i in range(10):
	pos_b.append(collide(bill, ring))
	# print(pos_b[-1])
	print ('Radius:', np.linalg.norm(bill.v))