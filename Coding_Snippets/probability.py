
import random
from You_Exist_Imports import *

#def rng(boundary):
    #chance = random.random()
    #global first_path
    #if chance < boundary:
        #first_path = True
    #elif chance >= boundary:
        #first_path = False

count = 0

while count < 100:

    rng(0.1)
    if first_path == True:
        print("First path")
        # continue journey here

    elif first_path == False:
        print("Second path")
        # continue journey here

    count += 1

#Lower_half = 0
#Upper_half = 0
#count = 0
#while count < 100:
    #chance = random.random()
    #if chance < 0.7:
        #Lower_half += 1

    #elif chance >= 0.7:
        #Upper_half += 1

    #count += 1


#print("Lower half: " + str(Lower_half))
#print("Upper half: " + str(Upper_half))