def odd_even_mul():

    n = int(input())
    arr = input().split()
    list=[]
    odd =[]
    even =[]
    
    for i in range(n):
        list.append(int(arr[i]))
    
    for i in range(len(list)):
        if (list[i]%2==0):
            even.append(list[i])
        else:
            odd.append(list[i])
    
    odd_sum = sum(ele for ele in odd)
    even_sum = sum(val for val in even)
    
    print(int(odd_sum*even_sum))

odd_even_mul()
