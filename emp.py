import ast

emp_list = []
temp_list = []

n = int(input('Enter no. of employee pairs in the list - '))
for x in range(n):
	str1 = input('Enter employee pair: ')
	emp_list.append(set(str1.split()))

for set1 in emp_list:
	#print (emp_list)
	for set2 in emp_list:
		if set1 != set2 and not set1.isdisjoint(set2):
			emp_list.append(set1.union(set2))
			emp_list.remove(set1)
			emp_list.remove(set2)
			break

print ("No. of related groups are: " + str(len(emp_list)) + "\nGroups are: " + str(emp_list))

str2 = input('Enter employee pair to check if connected: ')
temp_list = str2.split()
flag = False
for set1 in emp_list:
	if (temp_list[0]) in set1 and (temp_list[1]) in set1:
		flag = True

if flag:
	print("They are connected")
else:
	print("They are not connected")
		

'''
Output
Enter no. of employee pairs in the list - 5
Enter employee pair: pr an
Enter employee pair: au pr
Enter employee pair: au me
Enter employee pair: vi ak
Enter employee pair: ra pa
No. of related groups are: 3
Groups are: [{'ak', 'vi'}, {'pa', 'ra'}, {'me', 'au', 'pr', 'an'}]
Enter employee pair to check if connected: pr me
They are connected

'''