import os
# import rsa
import random

def isprime(n:int,t:int=10):
    assert n>1
    if n==2:
        return True
    if not n&1:
        return False

    s=0
    d=n-1
    while not d&1:
        d>>=1
        s+=1
    assert (1<<s)*d==n-1 

    def try_composite(a):
        if pow(a,d,n)==1:
            return False
        for i in range(s):
            if pow(a,(1<<i)*d,n)==n-1:
                return False
        return True

    for i in range(t):
        if try_composite(random.randrange(2,n)):
            return False

    return True

def getnum(n):
    z=n&7
    return bytes_to_long(os.urandom(n//8))<<z|1|(1<<(n-1))|random.randint(0,((1<<z)-1))

def getprime(b):
    a=getnum(b)
    while not isprime(a):
        print('z',end='')
        a+=2
    return a

# for i in range(10):
#     print(getprime(6))

from Crypto.Util.number import *

e=65537

def getpq(b):
    qs=b>>1
    q=getprime(b-qs)
    while not (q-1)%e:
        print('q',end='')
        q=getprime(b-qs)
    p=getprime(qs)
    while p==q or not (p-1)%e:
        print('p',end='')
        p=getprime(qs)
    assert (p-1)*(q-1)%e
    return p,q

p,q=getpq(4096)

print()
print('e =',e)
print('p =',p)
print('q =',q)
n=p*q

m='Hello world!'
c=pow(bytes_to_long(m.encode('utf-8')),e,n)
print(long_to_bytes(c))

phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m).decode('utf8'))
