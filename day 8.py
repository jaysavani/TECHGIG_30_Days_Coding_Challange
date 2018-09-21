def armstrong():

    list2=[]
    x=int(input("enter the number"))
    list = [int(i) for i in str(x)]
    print(list)

    if len(list)>2:
        for i in range(len(list)):
            c=list[i]**3
            list2.append(c)
    print(list2)

    add = sum(list2)
    print(add)

armstrong()
