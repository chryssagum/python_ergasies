import random

print("Δώστε τη διάσταση του τετραγώνου")
diastash=int(input())
s=0
for k in range(0,100):
    for k in range(0,1):
        lines=[]
        rows=[]
        count=0
        for i in range(0,int(diastash)):
            for j in range(0,int(diastash)):
                x=random.randint(0,1)
                if(x==1):
                    if (count<=(diastash*diastash)/2):
                        count=count+1
                    else:
                        x=0
                rows.append(x)
            lines.append(rows)
            rows=[]
        #print(lines)
        for i in range(0,len(lines)):
            for j in range(0,len(lines)):
                print(lines[i][j],end=" ")
            print("\n")
        count=0
        metr1=0
        for i in range(0,int(diastash)):
            for j in range(0,int(diastash)):
                if(lines[i][j]==1):
                    count=count+1
                    if(count==4):
                        metr1=metr1+1
                        count=0
            count=0
        #print(metr1)
        metr2=0
        for j in range(0,int(diastash)):
            for i in range(0,int(diastash)):
                if(lines[i][j]==1):
                    count=count+1
                    if(count==4):
                        metr2=metr2+1
                        count=0
            count=0
        #print(metr2)
        count=0
        mainDiagonal=0
        for x in range(0,len(lines)-1):
            for i in range(0,len(lines)-x):
                if(lines[i][i+x]==1):
                    count+=1
                    if(count==4):
                        mainDiagonal+=1
                        #print("OK")
        for x in range(1,len(lines)-1):
            for i in range(x,len(lines)):
            if(lines[i][i-x]==1):
                    count+=1
                    if(count==4):
                        mainDiagonal+=1
                        #print("OK")
        #print(mainDiagonal)
        count=0
        secondDiagonal=0
        for i in range(0,int(diastash)):
            if(lines[i][int(diastash)-i-1]==1):
                count=count+1
                if(count==4):
                    secondDiagonal=secondDiagonal+1
                    count=0
        #print(secondDiagonal)
        s=s+mainDiagonal+secondDiagonal+metr1+metr2
print("Ο μέσος όρος των τετράδων είναι:")
print(s/100)
