#!/usr/bin/python3
# guess what this program does?
import random
r=random.randint (1,6) #give random number
print(r)   
if r<35:
	print(r)
	print(":is less than 35")
elif r==30:
	print("30 is multiple of 10 and 3, both")
elif r>=35:
	print(r,"is greater than 35")
else:
	print("your number is:",r)