# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Step 1; Generate a list
import random

#Assumption made that 1 and 100 count in the list, and that all numbers are integers.
randomList=random.sample(range(1,100),10)
  
#Sorting the list in descending numerical order
sortedList= sorted(randomList, reverse=True)
 
   
results=[]
#Filtering the sorted list for duplicate numbers. 
for num in sortedList:
   if num not in results:
      results.append(num)

print(results)
 