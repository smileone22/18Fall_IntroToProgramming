

nrange = int(input("Enter a number range: "))
allnum =["P"]*nrange

#Index N
allnum[0]="N"
allnum[1]="N"

for n in range (2,len(allnum)):
    for m in range (2,n):
        if n%m==0:
            allnum[n]="N"
print()
print("All prime numbers from 0 to",nrange)
print()

i=0
while i<len(allnum):
    if allnum[i]=="P":
        print(format(i,"<5"),end='')
    i+=1
