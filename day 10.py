def slarge():
    n=int(input())
    arrayList=list(map(int, input().split(' ')[:n]))
    arrayList.sort(reverse=True)
    print(arrayList[1])
slarge()
