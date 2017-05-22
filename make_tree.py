'''
Generates an unordered binary tree of at most height n
'''
from random import random, randint

class node:
	def __init__(self):
		self.left = None
		self.right = None
		self.value = None

	def __str__(self):
		return node.output(self)

	def __lt__(self, other):
		if other is None:
			return False
		return self.value < other.value

	def __le__(self, other):
		if other is None:
			return False
		return self.value <= other.value

	def __eq__(self, other):
		if other is None:
			return False
		return self.value == other.value

	def __ne__(self, other):
		if other is None:
			return True
		return self.value != other.value

	def __gt__(self, other):
		if other is None:
			return True
		return self.value > other.value

	def __ge__(self, other):
		if other is None:
			return True
		return self.value >= other.value

def render_tree(root, h = 0):
	val = 'Val:' + str(root.value) + ''

	if root.left is not None:
		val += '\n\t' + ('\t' * h) + 'L:' + renderTree(root.left, h + 1)
	
	if root.right is not None:
		val += '\n\t' + ('\t' * h) + 'R:' + renderTree(root.right, h + 1)
	
	return val

def create_tree(height, full = False):
	root = node()
	root.value = randint(0, 999)
	if height > 1:
		if random() > 0.1 or full:
			root.left = createTree(height - 1, full)

		if random() > 0.1 or full:
			root.right = createTree(height - 1, full)

	return root

def is_balanced(root):
	return abs(height(root.left) - height(root.right)) < 2

def height(root):
	if root == None:
		return 0;
	return 1 + max(height(root.left), height(root.right))
