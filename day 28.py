def big_digit():

    m,n = input().split()
    a = [int(i) for i in str(m)]
    b = [int(j) for j in str(n)]
    
    if (sum(a) > sum(b)):
        print(m)
    else:
        print(n)
    
big_digit()
