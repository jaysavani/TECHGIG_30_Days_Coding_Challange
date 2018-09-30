from statistics import mean

def odd_even_avg():

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
            
    print(int(mean(odd))+int(mean(even)))
    
odd_even_avg()
