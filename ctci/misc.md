# General
## Find the most frequent integer in an array
- dict[word] = 1

```python
def frequent(lst):
	d = {}
	max_num = 0
	max_elem = None
	for elem in lst:
		if d[elem] is None:
			d[elem] = 1
			if max_num > d[elem]:
				max_num = d[elem]
				max_elem = elem
		else:
			d[elem] += 1
			if d[elem] > max_num:
				max_num = d[elem]
				max_elem = elem
	return max_elem

```

## Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
**input**: list
**output**: list of pairs (x,y) whose sum equals 10

- compare each element to the rest of the array, O(n^2)
- sort the array, add the first elem and last elem. if it equals 10, add to pair, move towards middle.

1 2 3 6 8


```python
def sums_to_ten(lst):
	first = 0
	last = len(lst) - 1
	pairs = []
	i = 0

	while first > last:
		summation = first + last
		if summation == 10:
			pairs[i] = (first, last)
		else:
			if summation > 10:
				last -= 1
			else:
				first += 1
	return pairs

```

## Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array. Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}

len(lst1) = 7
len(lst2) = 7

in b, 5 is index 0. 6 is index 1. 1 is index 4. 
in a, 5 is index 3. 6 is index 4. 1 is index 0.

```python
def is_rotated(a, b):
	first, index = 0, 0
	while a[index] != b[first]: #find start of rotated array
		index += 1

	while a[index] == b[first]:
		if first == len(b)-1:
			return True
		if index == len(a)-1:
			index = 0
		else:
			index +=1
		first += 1

	return False
```

## Write fibbonaci iteratively and recursively (bonus: use dynamic programming)
- f(n) = f(n-1) + f(n-2)
- n >= 0

```python
def fibonacci(n)
	if n <= 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)
```

## Find the only element in an array that only occurs once.
- map to dictionary, with values
- O(n)

```python
def single(lst):
	d = {}
	singles = []
	for elem in lst:
		if d[elem] is None:
			d[elem] = 1
			singles.append(elem)
		else:
			d[elem] += 1
			singles.remove(elem)

	return singles[0]
```

## Find the common elements of 2 int arrays
- brute force: iterate through each array and compare each element in the arrays. O(n^2)
- Hash table: O(n)

```python
def common_elements(a, b):
	commons = [x for x in a if x in b]

def common_elements(a,b):
	return list(set(a) and set(b))

def common_elements(a,b):
	commons = set()

	for elem in a:
		if elem in b:
			commons.add(elem)
	return commons

```

## Implement binary search of a sorted array of integers
- compare the middle element to value
- recursive compare middle element of subarray

**Input**: target and list
**Output**: index of target in list or -1 if not in list

- iterative binary search is better than recursive for python because python does not use tail-recursion, so each recursive call gets added onto the call stack. This means that for large amounts of data, we would hit our recursive limit. As well, the recursive BS uses splice, which copies the array each time, making it inefficient for memory. 

```python
def binary_search(target, lst):
	mid = len(lst)//2

	if not len(lst): #not in list
		return -1

	if lst[mid] == target: #if found
		return mid
	elif lst[mid] < target: #search in second half
		return mid + binary_search(target, lst[mid+1:])
	else: #search in first half
		return binary_search(target, lst[:mid-1])

def binarySearch(target, lst):
	first = 0
	last = len(lst) -1
	mid = first + last

	while first <= last:
		if target < lst[mid]:
			last = mid - 1
		elif target > lst[mid]:
			first = mid + 1
		else:
			return mid
	return None

```

## Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})
- modified because can't tell where element is after rotation
- we must find what part of the array the pivot point is in by comparing it to the first element: first half or second half
 - then, binary search on the proper half

```python
def rotate_binary_search(target, lst):
	first = 0
	last = len(lst) - 1
	mid = first + last

	if lst[first] < lst[mid]: #pivot in second half
		if value >= lst[first] and value <= lst[mid]:
			return rotate_binary_search(target, lst[:mid-1])
		else:
			return rotate_binary_search(target, lst[mid+1:])

	elif lst[mid] < lst[last]: #pivot in first half
		if value >= lst[mid] and value <= lst[last]:
			return rotate_binary_search(target, lst[mid+1:])
		else:
			return rotate_binary_search(target, lst[:mid-1])


```

## Use dynamic programming to find the first X prime numbers
- sieve of erasthothenes
- delete each multiple of primes 1-10 in 1-n

```python
def sieve(n):
	d = {}
	for i in range(2, n+1):
		d[i] = True
	for i in primes:
		factors = range(i*i, n+1, i)
		if multiple in factors:
			d[i] = False
	return [prime for prime in d if d[prime] == True]

```

## Write a function that prints out the binary form of an int
##Implement parseInt
- takes a string (that represents integers) and returns the integer value of the string

```python
def parseInt(strng):
	result = 0

	for i in range(len(string)):
		result = result*10 + (ord(string[i]) - ord('0'))
		#shifts numbers over one digit, adds the (unicode value of character - unicode value of 0)
	return result
```

## Implement squareroot function
- squareroot of n is where i*i = n. or n^(0.5)

```python
def sqrt(n):
	return n**(0.5)

```

## Implement an exponent function (bonus: now try in log(n) time)
- x^3 = x\*x*x

```python
def exp(x, n): #x^n
	result = x
	for i in range(n-1):
		result = result * x
	return result
```

## Write a multiply function that multiples 2 integers without using *
- multiplication is repeated addition
- 5*3 == 15 == 5+5+5

```python
def mult(x,n):
	result = x
	for i in range(n-1):
		result += x
	return result
```

## HARD: Given a function rand5() that returns a random int between 0 and 5, implement rand7()
- use time*time, mod 5

```python
import time
def rand7():
	return time.time() + 
```

## HARD: Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)

# Strings
## Find the first non-repeated character in a String
- iterate through the string, adding each chr to a dictionary. if the chr is already not in the dictionary, we return that character
- strip the string of whitespace
 - does punctuation count?
- sort the string, but then we would not find the FIRST non-repeated character
- create a set of characters, but we would not find FIRST non-repeated character

```python
def non_repeated(strng):
	dictionary = {}
	strng.replace(" ", "")
	for i in range(len(strng)):
		char = strng[i]
		if char not in dictionary:
			return char
		else:
			if dictionary[char] is None:
				dictionary[char] = 1
			else:
				dictionary[char] += 1
```

## Reverse a String iteratively and recursively
- iterate through the string from the end, swap first and last characters
- 

```python
def iterative_reverse(strng):
	for i in range(len(strng)//2):
		first = strng[i]
		strng[i] = strng[-1-i]
		strng[-1-i] = first
	return strng
```

## Determine if 2 Strings are anagrams
- an anagram is a word tha can be made by rearranging the characters in a word
- to determine if 2 strings are anagrams, we can sort the strings. If the strings are the same, they are anagrams.
- we can use different sorting algorithms, however something like counting sort can be completed in O(n) time instead of O(nlogn) like quicksort. As well, for counting sort if the lists are the same we can say they are anagrams.

```python
def is_anagram(strng1, strng2):
	#boolen True if anagram, False otherwise
	if counting_sort(strng1) == counting_sort(strng2):
		return True
	return False

def counting_sort(strng): #return buckets list
	buckets = {}

	for i in range(len(strng)):
		char = strng[i]
		if buckets[char] is None:
			buckets[char] = 1
		else:
			buckets[char] +=1

	return buckets
```

## Check if String is a palindrome
- a palindrome has same characters forwards and backwards
- compare first and last characters without whitespace

```python
def is_palindrome(strng):
	strng = strng.replace(" ", "")

	for i in range(len(strng)//2):
		if strng[i] != strng[-i-1]:
			return False
	return True
```

## Check if a String is composed of all unique characters
- construct a dictionary of characters in string
- if character is already in the dictionary, return false
- create a list and set of the string, if the len(list) == len(set) then it is all unique characters

```python
def is_unique(strng):
	if len(list(stnrg)) == len(set(strng)):
		return True
	return False

def is_unique(strng):
	d = {}
	for i in range(len(strng)//2):
		if strng[i] not in d.keys():
			d[string[i]] = 1
		else:
			return False
	return True

```

## Determine if a String is an int or a double
- a double has a decimal place
- an int is a whole number
- look for a decimal

## HARD: Find the shortest palindrome in a String

## HARD: Print all permutations of a String
- take each character of a string and add it to all possible permutations of the string before the new character
- recursively do it until you hit just 1 character
- a: a
- ab: ab, ba
- abc: abc, acb, cab, cba, bca, bac
- abcd: abcd, acbd, cabd, cbad, bcad, bacd 

```python
def permutations(prefix, char):
	if len(strng) <= 1:
		return strng

	for i in range(len(prefix)**):



```

## HARD: Given a single-line text String and a maximum width value, write the function 'String justify(String text, int maxWidth)' that formats the input text using full-justification, i.e., extra spaces on each line are equally distributed between the words; the first word on each line is flushed left and the last word on each line is flushed right

# Trees

## Implement a BST with insert and delete functions
- BST: for a node, every element in right subtree is larger than elements in left subtree
- insert: make sure is inserting in correct position
- delete: point to remaining subtree

  6
 / \
3   8
    /\
   7  9

```python
class Node():
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

class BST():
	def __init__(self):
		self.root = Node(None)

	def insert(self, value):
		if self.root.val is None:
			self.root.val = value
		else:
			insert_node = Node(value)
			rec_insert(insert_node)

	def rec_insert(self, insert_node):
		node = self.root
		while node is not None:
			if node.val < value:
				node = node.right
			elif node.val > value:
				node = node.left
		node = insert_node

	def delete(self, value):
		node = self.root
		parent = None
		while node.val is not value:
			if node.val < value:
				parent = node
				node = node.right
			elif node.val > value:
				parent = node
				node = node.left

		if node is None:
			return -1

		elif not node.left and not node.right: #if leaf node
			if parent.left == node:
				parent.setLeft(None)
			else:
				parent.setRight(None)
		
		#find successor to node in subtree
		elif node.right and node.left:
			psucc = node
			successor = node.right
			while successor.left is not None:
				psucc = successor
				successor = successor.left
			node.val = successor.val
			if psucc.left == successor:
				psucc.setLeft(None)
			else:
				psucc.setRight(None)
		elif node.right:
			if parent.left == node:
				parent.setLeft(node.right)
			else:
				parent.setRight(node.right)
		elif node.left:
			if parent.left == node:
				parent.setLeft(node.left)
			else:
				parent.setRight(node.left)
```

## Print a tree using BFS and DFS
- DFS: recursive, goes all the way down one node until it hits Null, then goes to next neighbour
- BFS: iterative, queue, goes through all the neighbours at one level before going to levels of next neighbour

```python
def DFS_print(root):
	if root is None:
		return
	DFS_print(root.left)
	print(root)
	DFS_print(root.right)

def BFS_print(root):
	q = Queue()
	q.enqueue(root)
	while not queue.isEmpty():
		current = q.dequeue()
		print(current)
		if root.left:
			q.enqueue(root.left)
		if root.right:
			q.enqueue(root.right)
```

## Write a function that determines if a tree is a BST
- BST has property where elements in left subtree are smaller than root. Elements in right subtree are larger than root. Repeat with all subtrees.

```python
def is_BST(root):
	if root is None:
		return True

	if root.left and root.left < root:
		is_BST(root.left)
	if root.right and root.right > root:
		is_BST(root.right)

	return False
```

## Find the smallest element in a BST
- smallest element is always leftmost child

```python
def smallest_BST(root):
	while root.left is not None:
		root = root.left
	return root
```

## Find the 2nd largest number in a BST

```python
def nth_largest(root, n):
	if root is None:
		return
	nth_largest(root.right)
	n -=1
	if n == 0:
		return root
	nth_largest(root.left)
```
## Given a binary tree which is a sum tree (child nodes add to parent), write an algorithm to determine whether the tree is a valid sum tree
- check if children add up to root

	    7
	   / \
	  3   4
	 / \   \
	1   2   5

```python
def is_sumtree(root):
	#if leaf node
	if root.left is None and root.right is None:
		return True

	if root.left and not root.right and root.left.val == root.val:
		return is_sumtree(root.left)
	if root.right and not root.left and root.right.val == root.val:
		return is_sumtree(root.right)

	if root.left and root.right and root.left.val + root.right.val == root.val:
		return is_sumtree(root.left) and is_sumtree(root.right)

	return False
```

## Find the distance between 2 nodes in a BST and a normal binary tree
- from root, find first node
- from first node, find left node, counting number of nodes we traverse to get there

```python

```

## Print the coordinates of every node in a binary tree, where root is 0,0
## Print a tree by levels
-level order traversal is BFS

```python
def BFS_print(root):
	q = Queue()
	q.enqueue(root)
	while not q.isEmpty():
		curr = q.dequeue()
		print(curr)
		if curr.left:
			q.enqueue(curr.left)
		if curr.right:
			q.enqueue(curr.right)
```

Given a tree, verify that it contains a subtree.
HARD: Find the max distance between 2 nodes in a BST.
HARD: Construct a BST given the pre-order and in-order traversal Strings

# Stacks, Queues, and Heaps
## Implement a stack with push and pop functions

```python
class Stack():
	def __init__(self):
		self.stack = []

	def push(self, val):
		if len(self.stack) < 1:
			self.stack.append(val)
		else:
			self.stack.append(val)

	def pop(self, val):
		if len(self.stack) < 1:
			raise IndexError("Empty stack")
		else:
			return self.stack.pop()
```

## Implement a queue with queue and dequeue functions

```python
class Queue():
	def __init__(self):
		self.queue = Node(None)

	def enqueue(self, insert_val):
		if self.queue.val is None:
			if type(insert_val) is Node:
				self.queue = insert_val
			else:
				self.queue.val = insert_val
		else:
			if insert_val is not Node:
				insert_val = Node(insert_val)
			self.queue._enqueue(insert_val)

	def _enqueue(self, insert_node):
		node = self.queue
		while node.next is not None:
			node = node.next
		node.next = insert_node

	def dequeue(self):
		if len(self.queue) < 1:
			raise IndexError("Empty Queue")

		node = self.queue
		self.queue = node.next
		return node.val
```
## Find the minimum element in a stack in O(1) time
##Write a function that sorts a stack (bonus: sort the stack in place without extra memory)

## Implement a binary min heap. Turn it into a binary max heap

## HARD: Implement a queue using 2 stacks
- queue: can remove from beginning and add elements at the end
- stack: can remove and add from end
- 


# Linked Lists
## Implement a linked list (with insert and delete functions)

## Find the Nth element in a linked list
3 -> 5 -> (1) -> 4

```python
def find_nth(n, head):
	node = head
	while node.next is not None:
		node = node.next
		n-=1
		if n == 1:
			return node

def find_nth(n, head):
	if head is None:
		return
	find_nth(n, head.next)
	n -= 1
	if n == 0:
		return head
```

Remove the Nth element of a linked list
## Check if a linked list has cycles

```python
def has_cycle(head):
	slow = head
	fast = head

	while fast:
		fast = fast.next
		slow = slow.next
		if fast:
			fast = fast.next
			if fast == slow:
				return True

	return False

def met_at(head):
	slow = head
	fast = head

	while fast:
		fast = fast.next
		slow = slow.next
		if fast:
			fast = fast.next
			if fast == slow:
				return fast
	return None

def cycle_start(head, fast):
	if has_cycle(head):
		fast = met_at(head)
	slow = head
	if fast:
		fast = fast.next
		slow = slow.next
		if fast == slow:
			return fast
	return None
```
## Given a circular linked list, find the node at the beginning of the loop. Example: A-->B-->C --> D-->E -->C, C is the node that begins the loop
##Check whether a link list is a palindrome
- use a stack, fast and slow runner
- iterate through LL, pushing elements onto the stack until the fast hits end of list
- when fast hits end of list, begin popping elements off the stack and checking if they are the same as the second half of lL

## Reverse a linked list iteratively and recursively
NULL <- 3 <- 5 <- 1 <-NULL

```python
def reverse_iter(head):
	curr_node = head
	next_node = None
	prev_node = None

	while curr_node is not None:
		next_node = curr_node.next
		curr_node.next = prev_node
		prev_node = curr_node
		curr_node = next_node
	head = prev_node

def reverse_recur(head):
	if head is None:
		return None
	if head.next is None:
		return head

	second = head.next #5
	head.next = None 
	rev_list = reverse_recur(second)
	second.next = head

	return rev_list
```
# Sorting
Implement bubble sort
Implement selection sort
Implement insertion sort
Implement merge sort
Implement quick sort