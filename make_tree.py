'''
Binary tree manipulation functions
'''
from random import random, randint

class node:
	def __init__(self, value = None):
		self.left = None
		self.right = None
		self.value = value

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
		val += '\n\t' + ('\t' * h) + 'L:' + render_tree(root.left, h + 1)
	
	if root.right is not None:
		val += '\n\t' + ('\t' * h) + 'R:' + render_tree(root.right, h + 1)
	
	return val

def create_tree(height, full = False):
	root = node()
	root.value = randint(0, 999)
	if height > 1:
		if random() > 0.1 or full:
			root.left = create_tree(height - 1, full)

		if random() > 0.1 or full:
			root.right = create_tree(height - 1, full)

	return root

def is_balanced(root):
	return abs(height(root.left) - height(root.right)) < 2

def height(root):
	if root == None:
		return 0;
	return 1 + max(height(root.left), height(root.right))

def ordered(root, ascending = True):
	if root == None:
		return True

	greater = root.right
	lesser = root.left
	if not ascending:
		greater = root.left
		lesser = root.right

	if lesser == None and greater == None:
		return True

	if not lesser <= root <= greater:
		return False

	return ordered(lesser, ascending) and ordered(greater, ascending)

def insert(val, root = None):
	if root == None:
		root = node()
		root.value = val
		return root

	if root.value >= val:
		if root.left != None:
			return insert(val, root.left)
		else:
			root.left = insert(val)
	else:
		if root.right != None:
			return insert(val, root.right)
		else:
			root.right = insert(val)

	return root