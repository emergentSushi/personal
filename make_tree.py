'''
Generates an unordered binary tree of at least height n
'''
from random import random, randint

class node:
	def __init__(self):
		self.left = None
		self.right = None
		self.value = None

	@staticmethod
	def output(root, h = 0):
		val = 'Val:' + str(root.value)

		if root.left is not None:
			val += '\n' + ('\t' * h) + 'L:' + node.output(root.left, h + 1)
		
		if root.right is not None:
			val += '\n' + ('\t' * h) + 'R:' + node.output(root.right, h + 1)
		
		return val

def createTree(height):
	root = node()
	root.value = randint(0, 999)
	if height > 0:
		if random() > 0.1:
			root.left = createTree(height - 1)

		if random() > 0.1:
			root.right = createTree(height - 1)

	return root