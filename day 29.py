def cmp_diag():

    a,b = list(map(int,input().split( )))
    b = 0
    c=0
    for i in range(a):
        d = input()
        b = b+int(d.split( )[i])
        c = c+int(d.split( )[a-i-1])
    if b>c:
        print("Diagonal 1")
    elif b<c:
        print("Diagonal 2")
    else:
        print("Equal")
        
cmp_diag()
