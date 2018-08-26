#!/bin/python3

import math
N = int(input("Enter the number"))
if (N % 2 != 0):
    print ("Weird")
if (N<2 and N<5):
    if (N % 2 == 0):
        print ("Not Weird")
if (N<6 and N<20):
    if (N % 2 == 0):
        print ("Weird")
if (N % 2 == 0 and N>20):
    print("Not Weird")
