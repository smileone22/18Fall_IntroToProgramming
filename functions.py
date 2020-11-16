

problem_n = int(input("How many problems would you like to attempt? "))

while problem_n<=0:
    print("Invalid number, try again ")
    print()
    problem_n = int(input("How many problems would you like to attempt? "))

w = int(input("How wide do you want your digits to be? 5-10: "))

while w < 5 or w>10:
    print("Invalid width, try again")
    print()
    w = int(input("How wide do you want your digits to be? 5-10: "))


print("Here we go!")
print()



import random
import myfunctions
question_n=1
total_right =0
while problem_n>=question_n:
    print("What is . . .")
    print()
    a= random.randint(0,9)
    if a==0:
        myfunctions.number_0(w)
    elif a==1:
        myfunctions.number_1(w)
    elif a==2:
        myfunctions.number_2(w)
    elif a==3:
        myfunctions.number_3(w)
    elif a==4:
        myfunctions.number_4(w)
    elif a==5:
        myfunctions.number_5(w)
    elif a==6:
        myfunctions.number_6(w)
    elif a==7:
        myfunctions.number_7(w)
    elif a==8:
        myfunctions.number_8(w)
    elif a==9:
        myfunctions.number_9(w)
    print()

    op = random.choice(["+","-"])
    if op=="+":
        myfunctions.plus(w)
    elif op=="-":
        myfunctions.minus(w)
    print()
    
    b= random.randint(0,9)
    if b==0:
        myfunctions.number_0(w)
    elif b==1:
        myfunctions.number_1(w)
    elif b==2:
        myfunctions.number_2(w)
    elif b==3:
        myfunctions.number_3(w)
    elif b==4:
        myfunctions.number_4(w)
    elif b==5:
        myfunctions.number_5(w)
    elif b==6:
        myfunctions.number_6(w)
    elif b==7:
        myfunctions.number_7(w)
    elif b==8:
        myfunctions.number_8(w)
    elif b==9:
        myfunctions.number_9(w)

    entered_answer = int(input("= "))
    if myfunctions.check_answer(a,b,entered_answer,op)==True:
        print("Correct! ")
        total_right+=1
    elif myfunctions.check_answer(a,b,entered_answer,op)==False:
        print("Sorry, that's not correct. ")
    print()
    print()    
    if question_n==problem_n:
        print("You got",total_right,"out of",problem_n,"correct!")
    question_n+=1
    print()
    print()
    
