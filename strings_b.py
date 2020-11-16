

name = str(input("Enter your name: "))

def cal_firsttotal(name):
    ftotal=0
    for c in name.upper():
        if c=="A" or c=="J" or c=="S":
            ftotal+=1
        elif c=="B" or c=="K" or c=="T":
            ftotal+=2
        elif c=="C" or c=="L" or c=="U":
            ftotal+=3
        elif c=="D"or c=="M" or c=="V":
            ftotal+=4
        elif c=="E"or c=="N"or c=="W":
            ftotal+=5
        elif c=="F"or c=="O"or c=="X":
            ftotal+=6
        elif c=="G" or c=="P" or c=="Y":
            ftotal+=7
        elif c=="H"or c=="Q"or c=="Z":
            ftotal+=8
        elif c=="I" or c=="R":
            ftotal+=9
        
    return ftotal

def check_person(total):
    if total==1:
        person="initiating action, pioneering, leading, independent, attaining, individual"
    elif total==2:
        person="cooperation, adaptability, consideration of others, partnering, mediating"
    elif total==3:
        person="expression, verbalization, socialization, the arts, the joy of living"
    elif total==4:
        person="a foundation, order, service, struggle against limits, steady growth"
    elif total==5:
        person="expansiveness, visionary, adventure, the constructive use of freedom"
    elif total==6:
        person="responsibility, protection, nurturing, community, balance, sympathy"
    elif total==7:
        person="analysis, understanding, knowledge, awareness, studious, meditating"
    elif total==8:
        person="practical endeavors, status oriented, power seeking, material goals"
    elif total==9:
        person="humanitarian, giving nature, selflessness, obligations, creative expression"
    elif total==11:
        person="higher spiritual plane, intuitive, illumination, idealist, a dreamer"
    elif total==22:
        person="the Master Builder, large endeavors, powerful force, leadership"
    print(person)

def reduce(ftotal):
    ntotal=0
    for i in str(ftotal):
        ntotal+=int(i)
    return ntotal
    
print()
ftotal =cal_firsttotal(name)
while (ftotal>=12  or ftotal==10) and ftotal!=22:
    ftotal =reduce(ftotal)

if (ftotal>=1 and ftotal<=11 and ftotal!=10)or ftotal==22: 
    print("Your personality number: ",ftotal)
    print()
    print("Your personality associations are: ")
    check_person(ftotal)

    
