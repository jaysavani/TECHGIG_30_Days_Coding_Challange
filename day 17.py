def pair():
    n = int(input())
    arr = input().split()
    list = []
    for i in range(0, n):
        list.append(int(arr[i]))
    
    num = int(input())
    
    for i in range(0,len(list) - 1):
        for j in range(i+1, len(list)):
            temp = list[i] + list[j]
            
            if temp == num:
                print("True")
                return
    print("False")
 
pair()
