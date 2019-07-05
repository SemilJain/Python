def binary_Search(list,l,r,item):
	if r >= l: 
  		mid = int(l+(r-l)/2)
  		
  		if list[mid] == item:
  			return mid

  		elif list[mid] > item:
  			return binary_Search(list, l, mid-1, item)

  		else:
  			return binary_Search(list, mid + 1, r, item)
	else:
  		return -1


def main():
	list = []
	n = int(input('Enter no. of elements in the list - '))
	for x in range(n):
		list.append(int(input('Enter the element - ')))

	list.sort()

	item = int(input('Enter the item to be searched - '))
	
	index = binary_Search(list,0,n-1,item)

	if index == -1:
		raise Exception('Element not found.')
	else:
		print('The item was found at index',(index+1))

if __name__ == '__main__':
	main()


'''Output
Enter no. of elements in the list - 5
Enter the element - 1
Enter the element - 8
Enter the element - 13
Enter the element - 15
Enter the element - 17
Enter the item to be searched - 13
The item was found at index 3

Enter no. of elements in the list - 5
Enter the element - 1
Enter the element - 8
Enter the element - 13
Enter the element - 15
Enter the element - 17
Enter the item to be searched - 2
Traceback (most recent call last):
  File "bin_search.py", line 35, in <module>
    main()
  File "bin_search.py", line 30, in main
    raise Exception('Element not found.')
Exception: Element not found.

'''
