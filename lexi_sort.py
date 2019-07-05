import functools

def func(X,Y):
	l = len(X) if (len(X)<len(Y)) else len(Y)
	for i in range(l):
		if(X[i] != Y[i]):
			return (lex_list.index(X[i]) - lex_list.index(Y[i]))
	return (len(X)-len(Y))

def lex(A,B):
	#srt = {b: i for i, b in enumerate(B)}
	print(sorted(A, key=functools.cmp_to_key(func)))

in_list = []
n = int(input('Enter no. of strings in the list - '))
for x in range(n):
	in_list.append(input('Enter the string - '))

lex_list = []
n = int(input('Enter no. of elements in the lex list - '))
for x in range(n):
	lex_list.append(input('Enter the lex char: '))

lex(in_list,lex_list)

'''
Output
Enter no. of strings in the list - 6
Enter the string - cat
Enter the string - catf
Enter the string - fat
Enter the string - car
Enter the string - cat
Enter the string - taf
Enter no. of elements in the lex list - 5
Enter the lex char: f
Enter the lex char: r
Enter the lex char: c
Enter the lex char: t
Enter the lex char: a
['fat', 'car', 'cat', 'cat', 'catf', 'taf']

'''

