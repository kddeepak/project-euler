
n=int(raw_input())

for z in range(n):
    num=int(raw_input())
    i = 2  
    max=-1
    temp=num
    while i * i <= temp:  
        while num % i == 0:
            
            max=i
            num = num // i  
        i = i + 1 
    if num>2:
        print(num) 
    else:
        print(max)
