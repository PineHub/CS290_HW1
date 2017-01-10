#Clarence Pine
#CS 344_400
#11/18/16
#Assignment 4 Python Exploration

#!/usr/bin/env python

for j in range(1, 4):

	filename = "file_" + str(j)

	target = open(filename, 'w')#, encoding='utf-8')
	
#code adapted from http://stackoverflow.com/questions/18319101/whats-the-best-way-to-generate-random-strings-of-a-specific-length-in-python

	from random import choice
	from string import ascii_lowercase

	target.write(''.join(choice(ascii_lowercase) for i in range (10))+'\n')


	target.close()

	
	target = open(filename, 'r')

	data = target.read()

	print data 

	target.close()

import random

rand1 = (random.randint(1, 42))
rand2 = (random.randint(1, 42))

rand1str = str(rand1)
rand2str = str(rand2)

product = str(rand1 * rand2)

print("your first number:"+rand1str+"\nsecond number: "+rand2str+"\nproduct: "+product)
	
