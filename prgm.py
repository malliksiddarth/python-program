#!/usr/bin/python3
import random 
i=0
while(i<=100):
	 n=input("press r to roll the dice")
	 if(n=='r'):
	 	r=myroll()
	 	i=i+r
	 	print("new positionis",i)