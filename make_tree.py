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

	def __str__(self):
		return str(self.value)


	def is_subtree(self, subtree):
		subtree_list = subtree.to_inorder_array()
		return ''.join([str(x) for x in subtree_list]) in ''.join([str(x) for x in self.to_inorder_array()])

	def to_inorder_array(self):
		ret = []

		if self.left != None:
			ret += self.left.to_inorder_array()

		ret += [self.value]

		if self.right != None:
			ret += self.right.to_inorder_array()

		return ret

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

	#Semantics of the node class define a None value as being less than everything
	#hence the lesser node being None is not a special case
	if (not lesser <= root <= greater) and (not lesser <= root and greater == None):
		return False

	return ordered(lesser, ascending) and ordered(greater, ascending)

def sort(root):
	values = root.to_inorder_array()
	sorted_root = insert(values[0])

	for v in values[1:]:
		insert(v, sorted_root)
		pass

	return sorted_root

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