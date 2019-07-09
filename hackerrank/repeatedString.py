#https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #special case
    #if (s == "a"):
    #    return n

    #other cases
    numbSubString = math.ceil(n/len(s))
    newString = s * numbSubString
    
    totalA = 0
    for i in newString:
        if (i == "a"):
            totalA +=1
    
    #newString = newString[:n]                   #concatenate new string
    return totalA
    #return newString.count('a')

if __name__ == '__main__':

    s = "a"
    n = 1000000000000

    #kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm
    #736778906400

    #out: 51574523448

    result = repeatedString(s, n)
    print(result)

