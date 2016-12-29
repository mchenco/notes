import sys
import math
import queue

#O(n^2)
#bubbles each element to the correct spot
#only one elem guaranteed correct after each iteration
def bubbleSort(lst):
	for i in range(len(lst)):
		for j in range(len(lst) - 1):
			if lst[j] > lst[j+1]:
				temp = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = temp
	return lst

#O(n^2)
#stable
'''
use when n is guaranteed to be small

if next element is smaller than current
bubbles it down through list until correct spot
left side of list will always be sorted
'''
def insertionSort(lst):
	for i in range(1, len(lst)-1):
		check = lst[i]
		if check < lst[i-1]:
			while check < lst[i-1] and i > 0:
				lst[i] = lst[i-1]
				lst[i-1] = check
				i -= 1
	return lst

#O(n^2)
'''
iterates through and if it finds a smaller element than first
places it at the first index
outputs a sorted list
'''
def selectionSort(lst):
	for i in range(len(lst)-1):
		min_ind = i
		for j in range (i+1, len(lst)-1):
			if lst[j] < lst[min_ind]:
				min_ind = j
		_swap(lst, i, min_ind)
	return lst

#O(nlogn)
#stable
'''
uses a lot of memory

recursively divides and sorts half of list
merges the list into a sorted list in the end
'''
def mergeSort(lst):
	if len(lst) <= 1:
		return lst
	mid = len(lst)//2

	a = mergeSort(lst[:mid])
	b = mergeSort(lst[mid:])

	return _merge(a, b)

def _merge(a, b):
	mergedlst = []
	act = 0
	bct = 0

	#while still elements to be sorted
	while act < len(a) and bct < len(b):
		if a[act] < b[bct]:
			mergedlst.append(a[act])
			act += 1
		else:
			mergedlst.append(b[bct])
			bct += 1
	
	#if elements leftover in array,
	#fill sorted array
	while bct <= len(b)-1:
		mergedlst.append(b[bct])
		bct += 1

	while act <= len(a)-1:
		mergedlst.append(a[act])
		act += 1

	return mergedlst

#O(nlogn)
#unstable
'''
as lst is more ordered, quicksort is less efficient, worst-case O(n^2)
Introsort is alternative if this ^ is the case.

works by choosing a pivot, swaps elements until left side of list <pivot
right side of list >pivot
'''
def quickSort(lst):
	if len(lst) <= 1:
		return lst

	pivot = lst[len(lst)-1]
	left = [x for x in lst if x < pivot]
	same = [x for x in lst if x == pivot]
	right = [x for x in lst if x > pivot]
	return quickSort(left) + same + quickSort(right)

#O(n+w)
'''
w is the range of numbers
the smaller the range, the better
works best when w < n ; takes a lot of time/space if w is large
better than comparison sorts which have lowerbound O(nlogn)

uses a count array to count the elements that are repeated
modify count array with the preceding sums
there are count[i] elems preceding the current elem in list
by placing according to how many preceding elements there are,
results in a sorted list
'''
def countingSort(lst):
	count = [0] * max(lst)
	#increment counter array
	for i in range(len(lst)-1):
		count[lst[i]] += 1
	#modify count array to include sum
	for i in range(1, len(count)-1):
		count[i] = count[i-1] + count[i]

	sorted = [0] * len(lst)
	#place first element at counted index
	for i in range(len(lst)-1):
		sorted[count[lst[i]]] = lst[i]
		count[lst[i]] -= 1
	return sorted

#O(kn)
#stable
'''
k is number of digits
use when logn is much larger than k OR 
use when the longest integer is shorter than logn
if k is logn —— O(nlogn), then you should just use quickSort/countingSort

linear time because we traverse the dataset k (# of digits) times
as the input grows, the amount of time needed grows linearly

sort based on sigfigs
empty buckets into a 'ordered' list
repeat for max #of digits
'''
def radixSort(lst):
	#find number with most digits x
	digits = len(str(max(lst)))
	buckets = [queue.Queue() for x in range(10)] #array of queues
	#sort by last digits into buckets
	for i in range(digits):
		for num in lst:
			digit = (num // 10**i) % 10
			buckets[digit].put(num)

		#empty buckets in order of a queue
		lst = []
		for bucket in buckets:
			while not bucket.empty():
				lst.append(bucket.get())
	return lst

def _swap(lst, indexA, indexB):
	temp = lst[indexA]
	lst[indexA] = lst[indexB]
	lst[indexB] = temp

'''
takes CLA as input for testing or supplies default list
must specify what sorting algorithm to use as argv[2]

`python3 sorting.py bubble 9 1 3 48 123`
'''
def main(argv):
	if len(sys.argv) > 2:
		lst = [int(x) for x in sys.argv[2:]]
	else:
		lst = [1,8,6,3,6,8,3,9,0,4,2,6,27,32,10,23,56,21,36,74]

	if sys.argv[1] == "bubble":
		print("bubble sort: ", bubbleSort(lst))
	if sys.argv[1]  == "insertion":
		print("insertion sort: ", insertionSort(lst))
	if sys.argv[1]  == "selection":
		print("selection sort: ", selectionSort(lst))
	if sys.argv[1]  == "merge":
		print("merge sort: ", mergeSort(lst))
	if sys.argv[1]  == "quick":
		print("quick sort: ", quickSort(lst))
	if sys.argv[1] == "counting":
		print("counting sort: ", countingSort(lst))
	if sys.argv[1] == "radix":
		print("radix sort: ", radixSort(lst))

if __name__ == "__main__":
	main(sys.argv)
