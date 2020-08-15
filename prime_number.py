# CODED BY GHz199
import math
from numba import jit
file = open("prime_number.txt","w")     #comment to speed up
@jit(parallel = True, fastmath = True)
def nombrepremier(n:int,l:int):
    while n<=l:
        i=2
        while i*i<=n and n%i!=0:
            i=i+1
        if i*i>n and n>1:
            #print(n)   #uncomment to get console output
            file.write("%d\n" %n)   #comment to speed up
        n=n+1
nombrepremier(2,5000000)    #5000000 is default limit, change it to get higher range
file.close()    #comment to speed up
