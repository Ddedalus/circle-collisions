import numpy as np


class Body:
	def __init__(self, mass, radius, position=[0.0, 0.0], velocity=[0.0, 0.0]):
		"""m, r, pos, v"""
		self.m, self.r = mass, radius
		self.pos = np.array(position)
		self.v = np.array(velocity)
		self.new_pos = None		# should be defined as np.array's
		self.new_v = None

	def step(self):
		self.pos = self.new_pos
		self.v = self.new_v
		self.new_v, self.new_pos = None, None

	def v_sq(self):
		return np.linalg.norm(self.v) ** 2

	def radius(self):
		return np.linalg.norm(self.pos)

def len_sq(body1, body2, new=False):
	if new:
		return (body1.new_pos[0] - body2.new_pos[0]) ** 2 + (body1.new_pos[1] - body2.new_pos[1]) ** 2
	else:
		return (body1.pos[0] - body2.pos[0]) ** 2 + (body1.pos[1] - body2.pos[1]) ** 2
