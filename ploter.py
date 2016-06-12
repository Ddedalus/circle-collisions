import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def plot_bodies(b1, b2):
	fig = plt.figure()
	plt.axis('equal')
	ax = fig.add_subplot(111)
	print(b1.pos[0], b1.pos[1])
	c1 = Circle((b1.pos[0], b1.pos[1]), radius=b1.r, fill=False, color='g')
	c2 = Circle((b2.pos[0], b2.pos[1]), radius=b2.r, fill=False, color='r')

	ax.add_patch(c1)
	ax.add_patch(c2)

	ax.autoscale_view()
	ax.figure.canvas.draw()


def plot_pos(pos_b):
	plt.plot(*zip(*pos_b))
	plt.axis('equal')
	plt.show()
