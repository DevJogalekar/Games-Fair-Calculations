'''
Trial Calculator
Author: Dev Jogalekar
Date Written: 4-11-2022
This is a simple program that looks at a list full of data, runs through it twice to select a random index and
then outputs these 2 numbers to a 2nd list

Yes, I did have to run this code 100 times since I could not get nested loops to work

#1 = Hall OF FAMER
#3 = All Star
#4  Gold
#5 = Silver
#6 = Bronze
#0 = Subreplacement
'''

import random

resultant_list = []
initial_list = [1,1,3,3,3,3,4,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

starting_range,ending_range = 0,38


for i in range(2):
    random_number = random.randint(starting_range,ending_range)
    resultant_list.append(initial_list[random_number])
    initial_list.pop(random_number)
    ending_range-=1
    
print(resultant_list)



