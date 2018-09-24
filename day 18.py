from sys import stdin

n=int(stdin.readline())
arr=list(map(int,stdin.readline().split(' ')))

ar1=arr[:];flagst=-1;flagen=-1;st=-1;en=-1

arr.sort()

for i in range(len(ar1)):
    if(flagst==-1):
        if(ar1[i]!=arr[i]):
            flagst=1;st=i
            break
            
for i in range(len(ar1)):
    if(ar1[n-1-i]!=arr[n-1-i]):
        en=n-1-i
        break
        
for i in range(st,en+1):
    if(i!=en):
        print(ar1[i],end=' ')
    else:
        print(ar1[i])
