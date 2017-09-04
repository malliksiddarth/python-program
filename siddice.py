#!/usr/bin/python3
#guess what this program does?
import random 
mpos=0
while mpos<101:
dice=random.randint (1,6) #give random number 
print(dice)
name="dice"
print(name)
while dice<3: dice=2
print("get on ladder")
if dice<2: dice=6
print