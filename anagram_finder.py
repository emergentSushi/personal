'''
noun: anagram; plural noun: anagrams

    a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

Finds anagrams from input, english dictionary only (see fulldict.txt and shortdict.txt).

Theoretically supports unicode if run under Python 3
'''

class TrieNode:
	def __init__(self, val):
		self.value = val
		self.children = []

def insert(head, s):
	if len(s) == 0: #base case, no more input to insert
		return

	#if the current node doesn't contain a child with the value we intend to search
	target = next((c for c in head.children if c.value == s[:1]), None)

	#then add it
	if target == None:
		target = TrieNode(s[:1])
		head.children.append(target)

	#and continue the insertion with the rest of the string minus the first character
	insert(target, s[1:])

anagrams = []

def find_anagrams(head, s, partial):
	#if we have a child node from here that is a newline character (conveniently added while reading the dictionary)
	#then we know that this node represents an acceptable final character for a word
	terminusChild = next((child for child in head.children if child.value == "\n"), None)

	partial += head.value

	#if there's no more input and it is acceptable to terminate the sequence at this node
	#then we have an anagram :), but don't add it if it's already in the list
	if s == "" and terminusChild != None and not partial in anagrams:
		anagrams.append(partial)
		return

	#look for a child with a value that matches any of the remaining characters in the input word
	for c in s:
		target = next((child for child in head.children if child.value == c), None)

		if target != None:
			i = s.find(c) #slice out the character we just found a child for and continue the search
			find_anagrams(target, s[:i] + s[i + 1:], partial)
			


trie_head = TrieNode("")

with open("fulldict.txt") as f:
	dict = f.readlines()
	for w in dict:
		insert(trie_head, w)

while(True):
	user_input = raw_input("Enter a word: ")

	#clean up user input
	find_anagrams(trie_head, user_input.lower().strip(), "")
	print(anagrams)
	anagrams = []

