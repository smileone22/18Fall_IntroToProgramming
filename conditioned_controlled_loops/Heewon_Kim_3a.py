a = 1
b = 1

while a <= 9:
    while b <= 9:
        c= a*b
        output= format(c,'3.0f')
        print(output, end= "  ")
        b += 1
    a += 1
    b = 1
    print()
