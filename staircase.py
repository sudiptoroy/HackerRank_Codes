#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i=1
    j=1
    while i<=n:
        while j<=i:
            print("#",end="")
            j+=1
        i+=1


if __name__ == '__main__':
    n = int(input())

    staircase(n)
