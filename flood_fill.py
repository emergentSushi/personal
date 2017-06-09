from grid_utils import *

grid = 	[[0,0,0,0],
		[0,2,0,0],
		[0,2,0,0],
		[0,0,0,0]]

def fill(data, start, fill_value = 1):
	starting_value = data[start.y][start.x]

	if starting_value == fill_value:
		return data

	data[start.y][start.x] = fill_value

	nexts = get_potentials(data, start, starting_value)

	for n in nexts:
		data = fill(data, n, fill_value)

	return data

print 'Open:'
show(grid)

grid = fill(grid, point(0,0), 3)

print 'Filled:'

show(grid)