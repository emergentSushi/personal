'''
Basic graph manipulation
'''

class vertex:
	def __init__(self, value = None):
		self.value = value
		self.edges = []

	def __str__(self):
		return str(self.value) + ":" +  ",".join([str(e.value) for e in self.edges])

def to_adjacency_list(adjacency_matrix):
	graph_vertices = [vertex(n) for n in range(len(adjacency_matrix[0]))]

	for y in range(len(adjacency_matrix)):
		for x in range(len(adjacency_matrix[y])):
			if adjacency_matrix[y][x] == 1:
				graph_vertices[y].edges.append(graph_vertices[x])
			pass
		pass

	return graph_vertices

def to_adjacency_matrix(vertices):
	matrix = [[0 for x in range(len(vertices))] for y in range(len(vertices))]

	for v in vertices:
		for e in v.edges:
			matrix[v.value][e.value] = 1
		pass

	return matrix
