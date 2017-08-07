from Queue import Queue
from random import randint

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

def search(root, goal):
	visited = [root]
	q = Queue()
	q.put(root)

	while not q.empty():
		current = q.get()
		if current.value == goal:
			return current

		for n in current.edges:
			if n not in visited:
				visited.append(n)
				q.put(n)

	return None

def dfs(root, goal, visited = []):
	visited.append(root)

	if root.value == goal:
		return root

	for n in root.edges:
		if n not in visited:
			return dfs(n, goal)

#generates a randomly linked graph of {size} elements as an adjacency list
def generate_graph(size, max_siblings = 2, directed = False):
	nodes = []

	for i in xrange(size):
		nodes.append(vertex(i))
		pass

	for x in xrange(size):
		for s in xrange(max_siblings):
			add_child(randint(0, size - 1), x, nodes, directed)

		pass

	return nodes

#adds node n to node x (and x to n if the graph is undirected)
def add_child(n, x, nodes, directed):
	if n != x:
		if nodes[n] not in nodes[x].edges:
			nodes[x].edges.append(nodes[n])

			if not directed and nodes[x] not in nodes[n].edges:
				nodes[n].edges.append(nodes[x])