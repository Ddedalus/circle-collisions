import numpy as np

# 0 - ball, 1 - ring; ball is inside ring
# r0 < r1
# collision condition: distance = r0-r1
#
#


def main():
	m = np.array([1.0, 3.0])
	r = np.array([1.0, 5.0])
	x = np.array([[0.0, 0.0]])
	y = np.array([[0.0, 0.0]])
	vx = np.array([[0.0, 0.0]])
	vy = np.array([[0.0, 0.0]])
	# array: [time][body]

	def V_sq (body, time=-1):  # total velocity
		return vx[time][body]**2 + vy[time][body]**2

	# Collision time t: At + Bt + C = 0 where:
	A = V_sq(0) + V_sq(1) - 2 * (vx[-1][0]*vx[-1][1] + vy[-1][0] * vy[-1][1])
	                             # 2 * dot_product(V1, V2)
	B = np.sum(y[-1]) * np.sum(vy[-1]) - 2 * np.sum(x[-1]) * np.sum(vx[-1])
	C = (x[-1][0] - x[-1][1])**2 + (y[-1][0] - y[-1][1])**2 - (r[1] - r[0])**2

	D = B**2 - 4*A*C

	if D <= 0:
		print("Negative discriminant:", D, "no ongoing collision...")
		return 1

	t = np.minimum((-B + np.sqrt(D))*0.5/A, (-B - np.sqrt(D)) * 0.5 / A)

	new_x = [x[-1][0] + t*vx[-1][0], x[-1][1] + t*vx[-1][1]]
	new_y = [y[-1][0] + t * vy[-1][0], y[-1][1] + t * vy[-1][1]]






	x.append(new_x)
	y.append(new_y)


main()