num=2
while num<=1000:
    for divisor in range(2,num+1):     
        if num==divisor:
            print(num,'is a prime number!')
            num+=1
        elif (num%divisor)==0:
            num+=1
    
            
