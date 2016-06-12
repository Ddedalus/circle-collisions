from Body import *
import math


def collide(b, r):
	# mass, radius, x, y, vx, vy

	A = b.v_sq() + r.v_sq() - 2 * (b.vx * r.vx + b.vy * r.vy)
	B = 2 * ((b.x - r.x) * (b.vx - r.vx) + (b.y - r.y) * (b.vy - r.vy))
	C = (b.x - r.x)**2 + (b.y - r.y)**2 - (b.r - r.r)**2
	D = B**2 - 4 * A * C        # discriminant of L**2 = (b.r - r.r)**2

	if D < 0:
		print("Negative discriminant:", D, "no ongoing collision...")
		return 1

	t1 = (-B + math.sqrt(D)) * 0.5 / A
	t2 = (-B - math.sqrt(D)) * 0.5 / A
	t = max(t1, t2)

	for k in [b, r]:
		k.new_x, k.new_y = k.x + t * k.vx, k.y + t * k.vy

	sin_f = (b.new_x - r.new_x) / math.sqrt(len_sq(b, r, new=True))
	cos_f = (b.new_y - r.new_y) / math.sqrt(len_sq(b, r, new=True))
	# angle between x-y and d-e coordinates
	# d is tangent to both circles in point of collision

	for k in [b, r]:
		k.vd = k.vx * cos_f - k.vy * sin_f
		k.ve = k.vx * sin_f + k.vy * cos_f
	# velocities in new coordinates

	b.we = (b.ve * (r.m - b.m) + 2 * r.m * r.ve) / (b.m + r.m)
	r.we = (r.ve * (b.m - r.m) + 2 * b.m * b.ve) / (b.m + r.m)

	for k in [b, r]:
		k.new_vx = k.vd * cos_f + k.we * sin_f
		k.new_vy = - k.vd * sin_f + k.we * cos_f

	pos = b.pos()
	b.step()
	b.we = b.vd = b.ve = None
	r.we = r.vd = r.ve = None
	r.step()
	return pos


def switch_to_massspoint(b, r):
	vx = (b.m * b.vx + r.m * r.vx) / (b.m + r.m)
	vy = (b.m * b.vy + r.m * r.vy) / (b.m + r.m)
	for k in [b,r]:
		k.vx -= vx
		k.vy -= vy

	return b, r

