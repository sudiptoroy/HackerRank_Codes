#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    app = 0   # Counts the apples falls in between s and t (House range)
    org = 0   # Counts the oranges falls in between s and t (House range)
    
    for i in apples:
        i = i + a              # Adding each apple distance to the position of the tree
        if i >= s and i <=t:   # Comparing if the fallen apple is in the range of house
            app += 1
        else:
            pass


    for j in oranges:
        j = j + b              # Adding each orange distance to the position of the tree
        if j >= s and j <= t:  # Comparing if the fallen orange is in the range of house
            org += 1
        else:
            pass

    # Prints the occurrence
    print(app)
    print(org)


        




if __name__ == '__main__':

    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
