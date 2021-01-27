import random
import sys

print("Please enter the nth term of fib")
s=int(input())
count=2
fn=0
fn1=1
fn2=0
while(count<=s):
    fn=fn1+fn2
    fn2=fn1
    fn1=fn
    count=count+1
print(fn)
random.seed()
p=fn
isfound=True
for i in range(0,20):
    a=random.randint(0,sys.maxsize)
   # print(a)
   # print((a**p)%p)
   # print(a%p)
    if(((a**p)%p)!=a%p):
        print("it is not prime")
        isfound=False
        break
if(isfound==True):
    print("it is prime")
