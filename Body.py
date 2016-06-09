class Body:
	def __init__(self, mass, radius, x=0.0, y=0.0, vx=0.0, vy=0.0):
		# pass 2D values as list/tuple?
		"""mass, radius, x, y, vx, vy"""
		self.m, self.r = mass, radius
		self.x, self.y = x,y
		self.vx, self.vy = vx, vy
		self.new_x, self.new_y = None, None
		self.new_vx, self.new_vy = None, None

	def pos(self):
		return [self.x, self.y]

	def step(self):
		self.x, self.y = self.new_x, self.new_y
		self.vx, self.vy = self.new_vx, self.new_vy
		self.new_vx, self.new_vy, self.new_y, self.new_x = None, None, None, None

	def v_sq(self):
		return self.vx**2 + self.vy**2


def len_sq(body1, body2, new=False):
	if new:
		return (body1.new_x - body2.new_x) ** 2 + (body1.new_y - body2.new_y) ** 2
	else:
		return (body1.x - body2.x) ** 2 + (body1.y - body2.y) ** 2