def nar():

    x=str(input("enter the number"))
    y=len(x)
    list=[int(i) for i in str(x)]
    list2=[]
    print(list)

    for j in range(len(list)):
        c=pow(list[j],y)
        list2.append(c)
    print(list2)
    add = sum(list2)
    print(add)

    if add == int(x):
        print("true")
    else:
        print("false")
nar()
