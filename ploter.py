import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


# matplotlib.use('Agg')


class Plotter:
	live = False


font = {'family': 'serif',
        'color': 'darkred',
        'weight': 'normal',
        'size': 16}


def plot_bodies(b1, b2, title='Position'):
	fig = plt.figure()
	plt.axis('equal')
	plt.title(title)
	ax = fig.add_subplot(111)

	p1 = Circle((b1.pos[0], b1.pos[1]), radius=0.1, fill=True, color='g')
	p2 = Circle((b2.pos[0], b2.pos[1]), radius=0.1, fill=True, color='r')
	c1 = Circle((b1.pos[0], b1.pos[1]), radius=b1.r, fill=False, color='g')
	c2 = Circle((b2.pos[0], b2.pos[1]), radius=b2.r, fill=False, color='r')

	ax.add_patch(c1)
	ax.add_patch(c2)
	ax.add_patch(p1)
	ax.add_patch(p2)

	ax.autoscale_view()
	if Plotter.live is True:
		ax.figure.canvas.draw()
	else:
		plt.savefig('plot/position graph.png')
	plt.close()


def plot_single_path(pos_b, title=''):
	fig = plt.figure()
	plt.plot(*zip(*pos_b))
	plt.autoscale()
	plt.axis('equal')
	ax = fig.add_subplot(111)

	p1 = Circle(pos_b[0], radius=0.1, fill=True, color='b')
	plt.title("Path " + title)
	plt.xlabel('x')
	plt.ylabel('y')

	ax.add_patch(p1)
	if Plotter.live is True:
		plt.show()
	else:
		plt.savefig('plot/path single ' + title.lower() + '.png')

	plt.close()


def plot_compare_paths(pos_rigid, pos_inertial):

	fig, ax = plt.subplots(1)

	plt.plot(*zip(*pos_rigid), color='r', label='rigid')
	plt.plot(*zip(*pos_inertial), color='g', label='inertial')
	ax.legend(loc='upper right')
	ax.autoscale_view()
	ax.relim()

	p1 = Circle(pos_rigid[0], radius=0.1, fill=True, color='r')
	p2 = Circle(pos_inertial[0], radius=0.1, fill=True, color='g')

	for p in [p1, p2]:
		ax.add_patch(p)

	plt.title("Both paths")
	plt.axis('equal')
	plt.xlabel('x')
	plt.ylabel('y')

	if Plotter.live is True:
		plt.show()
	else:
		plt.savefig('plot/path compare.png')

	plt.close()


def plot_vs_collision(data, title='Data'):
	plt.title(title + ' vs collision number')
	plt.plot(range(len(data) - 1), data)
	plt.axis('equal')
	plt.xlabel('collision')
	plt.ylabel(title.lower())
	if Plotter.live is True:
		plt.show()
	else:
		plt.savefig('plot/collision vs ' + title.lower() + '.png')
