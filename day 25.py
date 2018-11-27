def consicutive_num():

    n = int(input())
    flag= False
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n-1):
        if arr[i+1]-arr[i] ==1:
            flag = True
            break
    if flag:
        print("True")
    else:
        print("False")

consicutive_num()
