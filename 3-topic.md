# IV. Tree

## What is a Binary-Search Tree?

The binary-search tree or BST has many of the same uses as the binary-search algorithm, and can be thought of as a refinement on it.

It helps to first understand the binary-search algorithm before moving on to why a BST can be even better for some operations.

## Binary-Search Algorithm

In the binary-search algorithm, the goal is to do better than simply iterating through a list to find something (that would have a performance of O(n)).

Instead, you would put the item into a SORTED list. For example, if it was the name "John Doe", you could put it in alphabetically in a 1000-page phone book.

To find "John Doe" again later, flip to page 500. If you went past "D", go to page 250. If not, go to page 750, and so on. That is a LOT faster than searching page by page. In fact, binary-search has a performance of O(log n)--much better than O(n).

## Proving It

For those curious, it can be shown how binary search is O(log n). Like usual, you just analyze the worst-case scenario, which is cutting the search space in half each time until only one item is left.

The first check results in it having only n/2 items left, the second in having n/4 items left, etc. If it was check 50 it would have only n/2^50 items left.

 If the goal is to know how many checks have been made when it is solved, you can see that when there is only ONE item left (ie. when it is solved), it would equal n / 2 ^ checks.
 
 Now, you could solve that equation for checks. That will be left as an exercise for the reader. With a little algebra, and ignoring any remaining coefficients, this will reduce to log n checks left--ie. performance of O(log n).

 ## Why Trees?

The binary-search algorithm requires a sorted array. Unfortunately, if you want to add another name to the phone book, you have to move all the other names after it, which costs O(n).

If you put that name into a BST, it would only cost O(log n) for insertion--the same speed as searching--and remain sorted.

Consider a tree of this structure:

			|Lyle
			|
		Kyle
		|	|
		|	|Jorge
	John
		|	|Jack
		|	|
		|Ingrid
			|
			|Immanuel

To insert Xavier, you simply check if Xavier
is after John in the alphabet, inserting higher
if it is. Then you check again at Kyle, Lyle,
etc:

				|Xaxier
				|
			|Lyle
			|
		Kyle
		|	|
		|	|Jorge
	John
		|	|Jack
		|	|
		|Ingrid
			|
			|Immanuel

This is so much faster for instertion because (1) the rest of the tree can remain as is, with no shifting of elements, and (2) a small number of nested levels can store an exponentially large number of elements.

(2) means you don't have to do n checks for the sorting process--in fact, your search space cuts in half each time, just like the binary search, so insertion is O(log n).

## Example

You've been tasked with coding the framework that a robot uses to store its memories, which have a name as well as various other properties like audio, video, and even tactile data.

For now, the memories only have a name. Eventually a large language model will be used to generate names based on the audio and video data.

A previous researcher used the name property to implement the add() and get() functions of the BST class:

	class Node:
		def __init__(self, name):
			self.left = None
			self.right = None
			self.name = name

		def get_left(self):
			return self.left
		
		def get_right(self):
			return self.right
		
		def set_left(self, left):
			self.left = left

		def set_right(self, right):
			self.right = right
		
		def get_name(self):
			return self.name
		

	class BST:
		def __init__(self):
			self.root = None

		def add(self, new):
			self.__add(self.root, new)

		def __add(self, current, new):
			if self.root == None:
				self.root = new
				return
			if new.name > current.name and current.right == None:
				current.right = new
				return
			
			if new.name > current.name and current.right != None:
				self.__add(current.right, new)
				return

			if new.name < current.name and current.left == None:
				current.left = new
				return

			if new.name < current.name and current.left != None:
				self.__add(current.left, new)
				return

		def get(self, name):
			return self.__get(self.root, name)

		def __get(self, current, name):
			if current == None:
				return None
			
			if current.name == name:
				return current
			
			if name > current.name:
				return self.__get(current.right, name)
			
			if name < current.name:
				return self.__get(current.left, name)

	memories = BST()
	memories.add(Node("First memory"))
	memories.add(Node("Second memory"))
	memories.add(Node("Third memory"))
	memories.add(Node("Fourth memory"))
	memories.add(Node("Fifth memory"))
	memories.add(Node("Sixth memory"))
	memories.add(Node("Seventh memory"))
	memories.add(Node("Eight memory"))
	memories.add(Node("Ninth memory"))
	memories.add(Node("Tenth memory"))

	print(memories.get("Sixth memory").get_name())

## Problem

Implement the remove() method to remove a memory from the tree.

## Solution

	class Node:
		def __init__(self, name):
			self.left = None
			self.right = None
			self.name = name

		def get_left(self):
			return self.left
		
		def get_right(self):
			return self.right
		
		def set_left(self, left):
			self.left = left

		def set_right(self, right):
			self.right = right
		
		def get_name(self):
			return self.name
		

	class BST:
		def __init__(self):
			self.root = None

		def add(self, new):
			self.__add(self.root, new)

		def __add(self, current, new):
			if self.root == None:
				self.root = new
				return
			if new.name > current.name and current.right == None:
				current.right = new
				return
			
			if new.name > current.name and current.right != None:
				self.__add(current.right, new)
				return

			if new.name < current.name and current.left == None:
				current.left = new
				return

			if new.name < current.name and current.left != None:
				self.__add(current.left, new)
				return

		def get(self, name):
			return self.__get(self.root, name)

		def __get(self, current, name):
			if current == None:
				return None
			
			if current.name == name:
				return current
			
			if name > current.name:
				return self.__get(current.right, name)
			
			if name < current.name:
				return self.__get(current.left, name)
			
		def remove(self, old):
			self.__remove(self.root, old)

		def __remove(self, current, old):
			if self.root == None:
				return
			
			if self.root != None and old.name == self.root.name:
				self.root = None
				return

			if old.name > current.name and current.right == None:
				return
			
			if old.name > current.name and current.right != None and old.name == current.right.name:
				current.right = None
				self.__reinsert_children(old)
				return
			
			if old.name > current.name and current.right != None and old.name != current.right.name:
				self.__remove(current.right, old)
				return

			if old.name < current.name and current.left == None:
				return

			if old.name < current.name and current.left != None and old.name == current.left.name:
				current.left = None
				self.__reinsert_children(old)
				return
			
			if old.name < current.name and current.left != None and old.name != current.left.name:
				self.__remove(current.left, old)
				return
		
		# be sure to remove parent from tree before calling this one
		def __reinsert_children(self, parent):
			if parent == None:
				return
			
			left = parent.left
			right = parent.right

			if parent.right != None:
				parent.right = None
				self.add(right)
				self.__reinsert_children(right)
			
			if parent.left != None:
				parent.left = None
				self.add(left)
				self.__reinsert_children(left)

	memories = BST()
	memories.add(Node("First memory"))
	memories.add(Node("Second memory"))
	memories.add(Node("Third memory"))
	memories.add(Node("Fourth memory"))
	memories.add(Node("Fifth memory"))
	memories.add(Node("Sixth memory"))
	memories.add(Node("Seventh memory"))
	memories.add(Node("Eight memory"))
	memories.add(Node("Ninth memory"))
	memories.add(Node("Tenth memory"))

	memory = memories.get("Sixth memory")
	memories.remove(memory)

	print(memories.get("Fifth memory").get_name())
	print(memories.get("Sixth memory"))
	print(memories.get("Seventh memory").get_name())

## Congratulations!

You've finished my tutorial on Stacks, Sets, and Trees in Python!
