import sys
import math

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
'''
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
'''
recursively divides and sorts half of list
merges the list into a sorted list in the end
'''
def mergeSort(lst, first, last):
	ct = 0
	if last - first <= 1:
		return lst
	mid = (first+last)//2

	a = mergeSort(lst, first, mid)
	b = mergeSort(lst, mid, last)


	return _merge(a, b)

def _merge(a, b):
	mergedlst = []
	act = 0
	bct = 0

	for i in range(min(len(a), len(b))):
		if a[i] < b[i]:
			mergedlst.append(a[i])
			act += 1
		else:
			mergedlst.append(b[i])
			bct += 1
	
	if len(a) < len(b):
		while bct <= len(b)-1:
			mergedlst.append(b[bct])
			bct += 1
	else:
		while act <= len(a)-1:
			mergedlst.append(a[act])
			act += 1
	return mergedlst

#O(nlogn)
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
	

# def radixSort(lst):

def _swap(lst, indexA, indexB):
	temp = lst[indexA]
	lst[indexA] = lst[indexB]
	lst[indexB] = temp

'''
takes CLA as input for testing or supplies default list
'''
def main(argv):
	if len(sys.argv) > 1:
		lst = sys.argv[1:]
	else:
		lst = [1,8,6,3,6,8,3,9,0,4,2,6,27,32,10,23,56,21,36,74]

	# print("bubble sort: ", bubbleSort(lst))
	# print("insertion sort: ", insertionSort(lst))
	# print("selection sort: ", selectionSort(lst))
	# print("merge sort: ", mergeSort(lst, 0, len(lst)))
	print("quick sort: ", quickSort(lst))


if __name__ == "__main__":
	main(sys.argv)
