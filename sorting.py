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
	for i in range(1, len(lst)):
		check = lst[i]
		if check < lst[i-1]:
			while check < lst[i-1] and i >= 0:
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
	min = lst[0]
	for i in range(1, len(lst)):
		if lst[i] < min:
			min = lst[i]
			#shift everything over
			for j in range(i, 0):
				temp = lst[j]
				lst[j] = lst[j-1]
				lst[j-1] = temp
			lst[0] = min
	return lst

#O(nlogn)
'''
recursively divides and sorts half of list
merges the list into a sorted list in the end
'''
def mergeSort(lst):
	if lst <= 1:
		return
	mid = floor(len(lst)/2)
	a = lst[:mid]
	b = lst[mid:]
	mergeSort(a)
	mergeSort(b)

# def quickSort(lst):

# def radixSort(lst):

'''
takes CLA as input for testing or supplies default list
'''
def main(argv):
	if len(sys.argv) > 1:
		lst = sys.argv[1:]
	else:
		lst = [1,8,6,3,6,8,3,9,0,4,2,6,27,32,10,23,56,21,36,74]

	print("bubble sort: " + bubbleSort(lst))
	print("insertion sort: " + insertionSort(lst))
	print("selection sort: " + selectionSort(lst))


if __name__ == "__main__":
	main(sys.argv)
