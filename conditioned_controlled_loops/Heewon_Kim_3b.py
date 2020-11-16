sides = int(input('How many sides on your dice (4-20)? '))

while sides < 4 or sides >20:
    print("Sorry, that's not a valid number of sides. Please choose a positive number between 4 and 20.")
    print()
    sides =int(input('How many sides on your dice (4-20)? '))

if sides >= 4 and sides <=20:
    print("Ok, here we go . . .")

import random
first_die = random.randint(1,sides)
second_die = random.randint(1,sides)

roll_num= 1
double_roll= 0
total_roll = 0
total_f_die = 0
total_s_die =0

while first_die != second_die:
    print(roll_num,". The first die is",first_die,"and the second die is",second_die)
    total_roll +=1
    roll_num +=1
    total_f_die += first_die
    total_s_die += second_die
    first_die = random.randint(1,sides)
    second_die = random.randint(1,sides)
    
       
while first_die == second_die and first_die !=1:
    print(roll_num,". The first die is",first_die,"and the second die is",second_die)
    total_roll +=1
    roll_num +=1
    double_roll +=1
    total_f_die += first_die
    total_s_die += second_die
    first_die = random.randint(1,sides)
    second_die = random.randint(1,sides)
    
else:
    print(roll_num,". The first die is 1 and the second die is 1")
    total_roll +=1
    double_roll +=1
    total_f_die += first_die
    total_s_die += second_die
        
    
first_avg = format(total_f_die / total_roll,'.1f')
second_avg = format(total_s_die / total_roll,'.1f')

print()
print("You got snake eyes on try number",roll_num,"!")
print("Along the way you rolled doubles",double_roll,"times.")
print("The average roll for the first die was:",first_avg)
print("The average roll for the second die was:",second_avg)
