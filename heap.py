from make_tree import render_tree

class heap:
	def __init__(self):
		self._store = [None] * 100
		self._last = 0

	def get_parent(self, i):
		return (i -1) // 2

	def get_left(self, i):
		return 2 * i + 1

	def get_right(self, i):
		return 2 * i + 2

	def swap(self, i, j):
		temp = self._store[i]
		self._store[i] = self._store[j]
		self._store[j] = temp

	
	def __str__(self):
		return "".join([str(x) for x in self._store if x != None])

	__repr__ = __str__

	def peek(self):
		return self._store[0]

	def pop(self):
		max = self._store[0]
		self._store[0] = self._store[self._last]
		self._store[self._last] = None
		self._last -= 1

		self.heapify()

		return max

	def heapify(self):
		start = self.get_parent(self._last)

		while start >= 0:
			root = start

			while self.get_left(root) <= self._last:
				left_child = self.get_left(root)
				right_child = self.get_right(root)
				swap = root

				if self._store[swap] < self._store[left_child]:
					swap = left_child
				
				if right_child <= self._last and self._store[swap] <= self._store[right_child]:
					swap = right_child

				if swap == root:
					break #all is right in the universe, swap >= left and swap >= right
				else:
					self.swap(root, swap)
					root = swap

			start -= 1 #move on to the next lowest node

	def insert(self, value):
		self._store[self._last] = value
		self.heapify()
		self._last += 1

h = heap()


for x in xrange(1,10):
	h.insert(x)
	pass

print str(h)

print h.pop()
print h.pop()
print h.pop()
print h.pop()
print h.pop()
print h.pop()
print h.pop()
print h.pop()

print h
