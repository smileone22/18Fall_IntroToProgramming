print("This program will project how much you can earn by investing money in a high-yield savings account over a 3-month period. ")
print()


initial_amount = float(input("To begin, enter how much money you would like to initially invest (i.e.500): "))
interest_rate = float(input("Next, enter your projected annual interest rate. For example, enter 0.05 for 5% : "))
print()
print("Calculating . . .")
print()

#calcuating montly interest rate and fomatting it to 2 decimal point
monthly_interest_rate = float((interest_rate / 12))

#first month calculation
starting_bal1 = initial_amount
interest_a1 = initial_amount * monthly_interest_rate
ending_balance1 = initial_amount + interest_a1

#second month calculation
starting_bal2 = ending_balance1
interest_a2 = ending_balance1 * monthly_interest_rate
ending_balance2 = ending_balance1 + interest_a2

#third month calculation
starting_bal3 = ending_balance2
interest_a3 = ending_balance2 * monthly_interest_rate
ending_balance3 = ending_balance2 + interest_a3

#creating a chart
x = format("Month","<5s")
y = format("Starting Balance","<20s")
z = format("Interest","<15s")
w = format("Ending Balance","<20s")
print(x,y,z,w)

#first month line
m1=format(1,"<5")
a=format(initial_amount,"<20,.2f")
b=format(interest_a1,'<15,.2f')
c=format(ending_balance1,'<20,.2f')

print(m1,a,b,c)

#second month line
m2=format(2,"<5")
d=format(ending_balance1,"<20,.2f")
e=format(interest_a2,'<15,.2f')
f=format(ending_balance2,'<20,.2f')

print(m2,d,e,f)

#third month line
m3=format(3,"<5")
g=format(ending_balance2,"<20,.2f")
h=format(interest_a3,'<15,.2f')
i=format(ending_balance3,'<20,.2f')

print(m3,g,h,i)
