#Asking for the file size in kilobytes
kilo_size = float(input("Enter a file size in kilobytes (KB): "))

print()
print(kilo_size,"KB ...")
print()

#Calculations for converting into other size values
bytes_size = kilo_size * 1024
bits_size = bytes_size * 8
mega_size = float(kilo_size / 1024)
giga_size = float(mega_size / 1024)

#Formatting for a chart
a = format("... in bits","<20s")
b = format("... in bytes","<20s")
c = format("... in megabytes","<20s")
d = format("... in gigabytes","<20s")

#Formatting to print converted values
x = format(bits_size,">15,.1f")
y = format(bytes_size,">15,.1f")
z = format(mega_size,">15,.1f")
w = format(giga_size,">15,.1f")

#Printing the final result
print(a,x,'bits')
print(b,y,'bytes')
print(c,z,'MB')
print(d,w,'GB')


#LISTS OF WAYS TO CRASH THE PROGRAM

#the following line would cause a syntax error because I forgot to put a parentheses in the end
#age =15
#print('I am',age,'years old'

#the following line would cause a syntax error because I did not match the quotes
#print("Hello world')

#the following line would cause a logic error because string and the calculation in the printed line will not make sense although it can run. 
#num1= int(input("Enter a number:"))
#num2= int(input("Enter another number"))
#print("The multiplication of these numbers would be",num1+num2)

#the following line would cause a run-time error because the program will crash although the code itself is fine
#100/0

#the following line would cause a syntax error because a keyword is misused
#print = 3*4-2
#print(print)
