s=open("two.txt","r")
text=s.read()
words=text.split()
length=[]
pair=[]
for i in words:
    length.append(len(i))
    pair.append(False)
for i in range(0,len(words)):
    if(pair[i]!=True):
        size=len(words[i])
        pairSize=20-size
        if(pairSize in length):
            for j in range(0,len(words)):
                if(length[j]==pairSize and pair[j]==False and i!=j):
                    print(words[i]+"\t"+words[j])
                    pair[i]=True
                    pair[j]=True
                    break
