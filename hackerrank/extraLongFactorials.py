#https://www.hackerrank.com/challenges/extra-long-factorials/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    
    for i in range(1,n+1): 
        myFact = myFact * i 

    return myFact


if __name__ == '__main__':
    n = int(input())

    result = extraLongFactorials(10)
    print(result)

