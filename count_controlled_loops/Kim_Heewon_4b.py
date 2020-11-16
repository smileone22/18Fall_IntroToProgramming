
studnum=int(input("How many students are in your class? "))
#Asking for student number + Ensuring that number of students are positive
while studnum<=0:
    print("Invalid number of students, try again.")
    studnum=int(input("How many students are in your class? "))
print()    
#Asking for test number + Ensuring that number of tests are positive
testnum=int(input("How many tests in this class? "))
while testnum<=0:
    print("Invalid number of tests, try again.")
    testnum=int(input("How many tests in your class? "))
print()
print("Ok, let's begin . . .")
print()
allavg=0

for student in range(0,studnum):
    print("**** Student #",student+1,"  ****",sep='')
    total_score=0
    for test in range(testnum):
        score=float(input("Enter a score for test #"+str(test+1)+": "))
        while score<=0:
            print("Invalid score, try again.")
            score=float(input("Enter a score for test #"+str(test+1)+": "))
        total_score +=score
    avg=total_score/testnum
    allavg+=avg
    print("Average score for student #",student+1,"is",format(avg,'.2f'))
    print()

classavg= allavg/studnum
print("Avgerage score for all students is:",format(classavg,'.2f'))
 

