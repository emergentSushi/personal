'''
Basic grid algorithms
'''
class point:
	def __init__(self):
		self.x = 0
		self.y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y	

	def __str__(self):
		return "(" + str(self.x) + " " + str(self.y) + ")"

#returns true if the given point (p) in the grid (data) is open (== 0 or == open_value)
def element_open(data, p, open_value = 0):
	return data[p.y][p.x] == open_value

#returns a list of all possible open
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

#flood fill
def fill(data, start, fill_value = 1):
	starting_value = data[start.y][start.x]

	if starting_value == fill_value:
		return data

	data[start.y][start.x] = fill_value

	nexts = get_potentials(data, start, starting_value)

	for n in nexts:
		data = fill(data, n, fill_value)

	return data

def show(layout):
	for row in layout:
		print row