# a=[1,3,4,16,32,8,64,4,128,2,256,32]
a=[16,2,4,2,128,64,7,1,64,32,16,5,8]
def timmax(b):
    i=b[0];
    for j in range(1,len(b)):
        if b[j]>i:
            i=b[j];
    return i

print(timmax(a))
dadung=[]
for i in range(timmax(a)+1):
    dadung.append(False)

for i in range(0,len(a)):
    for j in range(0, len(a)):
        if a[i]*a[j]==256 and dadung[a[i]]==False and dadung[a[j]]==False and i != j:
            print(a[i],a[j],i,j)
            dadung[a[i]]=True
            dadung[a[j]]=True


