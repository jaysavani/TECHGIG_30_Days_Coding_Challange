def lowup():
    string = str(input())
    upcount=0
    lowcount=0
    for i in x:
        if (i.isupper()):
            upcount+=1
        elif(i.islower()):
            lowcount+=1
        else:
            pass
    print(upcount)
    print(lowcount)

lowup()
