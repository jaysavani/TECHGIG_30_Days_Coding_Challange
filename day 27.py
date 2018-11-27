def big_digit():

    n = int(input())
    a = [int(i) for i in str(n)]
    odd = []
    even= []
    for i in range(len(a)):
        if(a[i]%2==0):
            even.append(a[i])
        else:
            odd.append(a[i])
    if (sum(even) > sum(odd)):
        print(sum(even)-sum(odd))
    else:
        print(sum(odd)-sum(even))
    
big_digit()
