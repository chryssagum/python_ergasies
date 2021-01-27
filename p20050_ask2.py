import random

print("Please give the n for the nth term")
term=input()
count=2
f1=0
f2=1
fn=0
#print(f1)
#print(f2)
while(count<int(term)):
    fn=f1+f2
    f1=f2
    f2=fn
    #print(fn)
    count=count+1
print("The "+term+"th is "+str(fn))

isTrue=True
count=0
for i in range(0,20):
    current_int=random.randint(0,100)
    if(current_int**fn!=current_int//fn):
        isTrue=False
        print("-----")
        print(fn**current_int)
        print("\n")
        print("OK"+str(fn%current_int))
        count=count+1
        print(count)
        print("-----")
if(isTrue==True):
    print("It is prime")
else:
    print("H xrysa den xerei python")
