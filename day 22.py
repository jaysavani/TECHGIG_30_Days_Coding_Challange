def odd_even_war():

    n = int(input())
    a = input().split()
    list = []
    odd = []
    even = []
    
    for i in range(n):
        list.append(int(a[i]))
    
    for i in range(0,len(list)):
        if i%2 == 0:
            even.append(list[i])
        else:
            odd.append(list[i])

    sum_odd = sum(odd)
    sum_even = sum(even)
    
    if sum_even > sum_odd:
        print(int(sum_even - sum_odd))
    else:
        print(int(sum_odd - sum_even))
    
odd_even_war()
