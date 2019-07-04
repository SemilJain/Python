def main():
	BA = ('Akash','Zampa','Souresh')
	DE = ('Pranit', 'Mihir','Sitanshu','Darshan','Sanmid')
	PE = ('Rahul','Semil','Sid','Hemant','Sakshi','Pavan','Lavesh')
	SD = ('Aakanksha','Harsh','Riya','Nishita','Yashraj')
	ML = ('Priyank',)
	
	list = [BA,DE,PE,ML,SD]

	sortList = sorted(list,key = lambda x:x[-1])

	print(sortList)


if __name__ == '__main__':
	main()
