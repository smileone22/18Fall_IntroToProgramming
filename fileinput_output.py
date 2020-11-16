
try:
    filename=input("Enter a file name(i.e. class1 for class1.txt): ")
    filecontent=open(filename+".txt","r")
    alldata=filecontent.read()

except:
    print("File cannot be found.")
    

else:
    print("Successfully opened",filename+".txt")


    print()
    print("*"*4,"ANALYZING","*"*4)
    print()
        
    #Reporting the total number of lines of data stored in the file
    split_lines=alldata.split("\n")
    total_lines=len(split_lines)
        
    #ANSWERS FOR Grading
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    eachanswer=answer_key.split(",")

    #Creating a new empty list of students' grades for grading
    class_scores=[]

    #Analyzing each line
    validstudents=0
    invalidstudents=0
    allvalidlines=[]
    for students in split_lines:
        """To be a valid line:contain 26 commas,
                            begin with N followed by 8 numeric characters"""
        studentdata=students.split(",")
        if len(studentdata)==26:
            nnumber=studentdata[0]
            if len(studentdata[0])==9 and nnumber[0]=="N" and nnumber[1::].isdigit()==True:
                validstudents+=1
                allvalidlines+=studentdata
                points=0
                for i in range(0,25):
                    if eachanswer[i]==studentdata[i+1]:
                        points+=4
                    elif studentdata[i+1]=="":
                        points+=0
                    elif eachanswer[i]!=studentdata[i+1]:
                        points-=1
                class_scores.append(points)            
                
            else:
                print("Invalid line of data: N# is invalid")
                print(students)
                print()
                invalidstudents+=1
                    
        else:
            print("Invalid line of data: does not contain exactly 26 values: ")
            print(students)
            print()
            invalidstudents+=1
    if invalidstudents==0:
        print("No errors found!")
                
    #Reporting the number of valid and invalid lines
    print()
    print("*"*4,"REPORT","*"*4)
    print()
    print("Total valid lines of data: ",validstudents)
    print("Total invalid lines of data: ",invalidstudents)

    #Saving the data of score as a file-part 4
    scorefile=open(str(filename)+"_grades"+".txt","w")
    score_i=0
    allnnum=allvalidlines[::26]
    while score_i< len(allnnum):
            scorefile.write(allnnum[score_i])
            scorefile.write(",")
            nscore=class_scores[score_i]
            scorefile.write(str(nscore))
            score_i+=1
    scorefile.close()
    
    #Setting to calculate STATISTICS
    class_scores.sort()

    total_score=0
    for each_score in class_scores:
        total_score+=each_score

    if len(class_scores)%2==0:
        median=(class_scores[int(len(class_scores)/2)]+class_scores[int((len(class_scores)/2)-1)])/2
    elif len(class_scores)%2==1:
        median=class_scores[len(class_scores)//2]

    #PRINTING STATISTICS
    print()
    print("Mean (average) score: ",format(total_score/validstudents,'.2f'))
    print("Highest score: ",max(class_scores))
    print("Lowest score: ",min(class_scores))
    print("Range of scores: ",max(class_scores)-min(class_scores))
    print("Median score: ",median)
