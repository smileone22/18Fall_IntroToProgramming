s_num = int(input("Start number: "))
e_num = int(input("End number: "))

while s_num<=0 or e_num<=0:
    print("Start and end must be positive. ")
    print()
    s_num = int(input("Start number: "))
    e_num = int(input("End number: "))

while s_num>=e_num:
    print("End number must be greater than start number. ")
    print()
    s_num = int(input("Start number: "))
    e_num = int(input("End number: "))
print()

while s_num<=e_num:
    for divisors in range(2,s_num+1):
        if s_num==divisors:
            print(s_num)
            s_num+=1
        elif (s_num%divisors)==0:
            s_num+=1
