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
		list.append(int(input('Enter the element')))

	list.sort()

	item = int(input('Enter the item to be searched - '))
	
	index = binary_Search(list,0,n-1,item)

	if index == -1:
		raise Exception('Element not found.')
	else:
		print('The item was found at index',(index+1))

if __name__ == '__main__':
	main()