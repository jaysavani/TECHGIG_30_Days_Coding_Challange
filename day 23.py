def min_vs_max():

    n = int(input())
    a = input().split()
    list = []
    
    for i in range(n):
        list.append(a[i])

    
    print(int(min(list))*int(max(list)))
        
min_vs_max()
