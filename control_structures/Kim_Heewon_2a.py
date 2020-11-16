print("Your Screen Printing Quote")
print()
#Asking for number of T-shirts and colors
num_shirt = int(input("How many T-shirts would you like to have printed? "))
num_col = int(input("How many colors will each shirt be printed with (1, 2, or 3)? "))

if num_col ==1:
    if num_shirt<100:
        p=num_shirt*8
    elif num_shirt<250:
        p=num_shirt*6
    elif num_shirt>=250:
        p=num_shirt*5

if num_col ==2:
    if num_shirt<100:
        p=num_shirt*9
    elif num_shirt<250:
        p=num_shirt*7
    elif num_shirt>=250:
        p=num_shirt*6

if num_col ==3:
     if num_shirt<100:
        p=num_shirt*10
     if num_shirt<250:
        p=num_shirt*8
     if num_shirt>=250:
        p=num_shirt*7
print()
total = float(p+p*8.875/100)
final = format(total,',.2f')
print(num_shirt," shirts screen printed with ",num_col," colors: $",final,sep="")



