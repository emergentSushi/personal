class point:
	def __init__(self):
		self.x = 0
		self.y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y	

	def __str__(self):
		return "(" + str(self.x) + " " + str(self.y) + ")"

def element_open(data, p, contains = 0):
	return data[p.y][p.x] == contains

def get_potentials(data, p, open_value = 0):
	left = point(p.x - 1, p.y)
	right = point(p.x + 1, p.y)
	up = point(p.x, p.y - 1)
	down = point(p.x, p.y + 1)

	pot = []

	if left.x >= 0 and element_open(data, left, open_value):
		pot.append(left)
	
	if right.x < len(data[0]) and element_open(data, right, open_value):
		pot.append(right)
	
	if up.y >= 0 and element_open(data, up, open_value):
		pot.append(up)

	
	if down.y < len(data) and element_open(data, down, open_value):
		pot.append(down)

	return pot

def show(layout):
	for row in layout:
		print row