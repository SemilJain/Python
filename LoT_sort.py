from ast import literal_eval

#cns = literal_eval(input("Please enter the data: "))

def main():
	
	in_list = literal_eval(input("Please enter the data as List of Tuples: "))
	# BA = ('Akash','Zampa','Souresh','GitSample')
	# DE = ('Pranit', 'Mihir','Sitanshu','Darshan','Sanmid')
	# PE = ('Rahul','Semil','Sid','Hemant','Sakshi','Pavan','Lavesh')
	# SD = ('Aakanksha','Harsh','Riya','Nishita','Yashraj')
	# ML = ('Priyank',)
	
	#list = [BA,DE,PE,ML,SD]

	sortList = sorted(in_list,key = lambda x:x[-1])
	print("The sorted list of tuples based on last element: \n")
	print(sortList)


if __name__ == '__main__':
	main()

'''
Please enter the data as List of Tuples: [('Akash','Zampa'),('Pranit','Mihir','Sitanshu','Darshan','Sanmid'),('Rahul','Semil','Sid','Hemant','Sakshi','Pavan','Lavesh'),('Aakanksha','Harsh','Riya','Nishita','Yashraj'),('Priyank',)]
The sorted list of tuples based on last element:

[('Rahul', 'Semil', 'Sid', 'Hemant', 'Sakshi', 'Pavan', 'Lavesh'), ('Priyank',), ('Pranit', 'Mihir', 'Sitanshu', 'Darshan', 'Sanmid'), ('Aakanksha', 'Harsh', 'Riya', 'Nishita', 'Yashraj'), ('Akash', 'Zampa')]
'''