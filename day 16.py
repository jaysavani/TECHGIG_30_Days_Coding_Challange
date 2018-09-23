def gcd():
    n1,n2 = map(int, input().split())
    if n1==n2:
        print(n2)
    else:
        n1=n2%n1
        n2=n1
        print(n1)
gcd()
