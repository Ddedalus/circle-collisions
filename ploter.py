import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def plot_bodies(b1, b2, title = 'Position'):
	fig = plt.figure()
	plt.axis('equal')
	plt.title(title)
	ax = fig.add_subplot(111)
	# print('Pos b1:', b1.pos)
	c1 = Circle((b1.pos[0], b1.pos[1]), radius=b1.r, fill=False, color='g')
	c2 = Circle((b2.pos[0], b2.pos[1]), radius=b2.r, fill=False, color='r')

	ax.add_patch(c1)
	ax.add_patch(c2)

	ax.autoscale_view()
	#ax.figure.canvas.draw()
	plt.savefig('position test.png')
	plt.close()


def plot_pos(pos_b):
	plt.plot(*zip(*pos_b))
	plt.axis('equal')
	plt.title("Position graph")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()


def plot_vs_collision(data, length, title='Data'):
	plt.title(title + ' vs collision number')
	plt.plot(range(length), data)
	plt.axis('equal')
	plt.xlabel('collision')
	plt.ylabel(title.lower())
	plt.show()
