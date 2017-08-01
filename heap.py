'''
Heap implementation, defaults to min heap.
Expects a 2 argument lambda that returns true if a comes before b
e.g. lambda a, b : a <= b
'''
class heap:
	def __init__(self, key = None):
		if key == None:
			key = lambda a, b : a <= b

		self._key = key
		self._store = []
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
		return "".join([str(x) for x in self._store])

	def empty(self):
		return self._last == 0

	__repr__ = __str__

	def peek(self):
		return self._store[0]

	def pop(self):
		top = self._store[0]
		self._store[0] = self._store[self._last - 1]
		self._last -= 1
		self.heapify()

		#we have to trim, padding None's into the array breaks a bunch of compare ops
		self.trim()
		return top

	def trim(self):
		self._store = self._store[0:self._last]

	def heapify(self):
		start = self.get_parent(self._last)

		while start >= 0:
			root = start

			while self.get_left(root) <= self._last:
				left_child = self.get_left(root)
				right_child = self.get_right(root)
				swap = root

				if self._key(self._store[swap], self._store[left_child]):
					swap = left_child
				
				if right_child <= self._last and self._key(self._store[swap], self._store[right_child]):
					swap = right_child

				if swap == root:
					break #all is right in the universe, swap comes before left and right
				else:
					self.swap(root, swap)
					root = swap

			start -= 1 #move on to the next lowest node

	def insert(self, value):
		self._store.append(value)
		self.heapify()
		self._last += 1
