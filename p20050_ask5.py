import random

print("Δώστε τη διάσταση της κάθετης γραμμής του ορθογωνίου.")
h=int(input())
print("Δώστε τη διάσταση της οριζόντιας γραμμής του ορθογωνίου.")
b=int(input())
lines=[]
rows=[]
char=['S','O']
for k in range(0,100):
    for i in range(0,int(h)):
        for j in range(0,int(b)):
            x=random.choice(char)
            rows.append(x)
        lines.append(rows)
        rows=[]
    #print(lines)
    metr1=0
    for i in range(0,h):
        for j in range(0,b-3):
            if(lines[i][j]=='S' and lines[i][j+1] == 'O' and lines[i][j+2]=='S'):
                metr1=metr1+1
    #print(metr1)
    metr2=0
    for j in range(0,b):
        for i in range(0,h-3):
            if(lines[i][j]=='S' and lines[i+1][j] == 'O' and lines[i+2][j]=='S'):
                metr2=metr2+1
    #print(metr2)
    diag1=0
    i = 0 
    while i < h-2 :
        if i==0 :
            j = 0
            while j < b-3 :
                k = 0
                while j+k < b-2 and k < h-2 :
                    if  (lines[k][j+k] == 'S') and (lines[k+1][j+k+1] == 'O') and (lines[k+2][j+k+2] == 'S') :
                        diag1 += 1
                        k = k + 2
                    k +=1
                j +=1
        else :
            k = 0
            while i + k < h-2 and k < b-2:
                if  (lines[i+k][k] == 'S') and (lines[i+k+1][k+1] == 'O') and (lines[i+k+2][k+2] == 'S') :
                     diag1 += 1
                     k = k + 2
                k +=1   
        i += 1
    #print('Diagonia1', diag1)
    diag2=0
    i = 0 
    while i < h-2 :
        if i==0 :
            j = b-1
            while j > 1 :
                k = 0
                while j-k > 1 and k < h-2:
                    if  (lines[k][j-k] == 'S') and (lines[k+1][j-k-1] == 'O') and (lines[k+2][j-k-2] == 'S') :
                        diag2 += 1
                        k = k + 2
                    k +=1
                j = j - 1
        else :
            k = 0
            while i + k < h-2  and k < b-2:
                if  (lines[i+k][b-1-k] == 'S') and (lines[i+k+1][b-1-k-1] == 'O') and (lines[i+k+2][b-1-k-2] == 'S') :
                     diag2 += 1
                     k = k + 2
                k +=1    
        i += 1
    #print('Diagonia2', diag2)
        
    s=metr1+metr2+diag1+diag2
print("Ο μέσος όρος των τριάδων SOS είναι:")
print(s/100)
