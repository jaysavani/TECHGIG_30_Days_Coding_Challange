def mat_sum():

    r1,c1=map(int,input().split());
    a1=[];
    for i in range(r1):
        a1.append(list(map(int,input().split())));
    r2,c2=map(int,input().split());
    a2=[];
    for i in range(r2):
        a2.append(list(map(int,input().split())));
    for i in range(r1):
        for j in range(c1-1):
            print(a1[i][j]+a2[i][j],end=" ");
        print(a1[i][c1-1]+a2[i][c1-1]);
        
mat_sum()
