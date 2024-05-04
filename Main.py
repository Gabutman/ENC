import  numpy as np
import math as m
import os
from itertools import cycle

def encrypt(__m,key0,iv="",n=10):
	cv = cycle(iv)
	
	table = np.array([next(cv) if len(iv)>0 else 0 for _ in range(m.ceil(len(iv)/256)*256)]).reshape((-1,16,16))
	
	for iter in range(n):
	    for i in range(len(table)):
	        box = lambda x: table[i]["0123456789abcdef".index(x[1])]["0123456789abcdef".index(x[0])]
	        
	        key = cycle(key0)
	        key0 =[box(format(box(format(k1,"02x"))^next(key),"02x")) for k1 in key0]
	        key = cycle(key0)
	        __m = [m2^next(key) for m2 in __m]
	        key = cycle(key0)
	        
	        table[i] = [[(table[i][o][(o+i1-1)%16]^table[i][o][(i1+1+o)%16]&table[i][o][(i1+o)%16])^next(key) for i1 in range(16)] for o in range(16)]
	        
	    print("".join(map(chr,__m)).lower().encode(),iter)
	    if "".join(map(chr,__m)).lower().encode() == b"hello":
	        break
	
	return bytearray(__m)
	
encrypt(b"hello",b"yanuar",iv=list(os.urandom(256)))
