

num=int(input("Enter a positive number to test: "))
while num<=0:
    print("Invalid number, please enter a positive number.")
    num=int(input("Enter a positive number to test: "))

print()
    
for divisor in range (2,num+1):
    if (num%divisor)!=0:
        print(divisor,"is not a divisor of",num,"... continuing")
    if num==divisor:
        print()
        print(num,"is a prime number!")
        break
    elif (num%divisor)==0:
        print(divisor,"is a divisor of",num,"... stopping")
        print()
        print(num,"is not a prime number!")
        break
    
