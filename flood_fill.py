from grid_utils import *

map1 = 	[[0,0,0,0],
		[0,2,0,0],
		[0,2,0,0],
		[0,0,0,0]]

map2 = 	[[1,1,1,1],
		[1,2,1,1],
		[1,2,1,1],
		[1,1,1,1]]

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
show(map2)

map2 = fill(map2, point(0,0), 3)

print 'Filled:'

show(map2)