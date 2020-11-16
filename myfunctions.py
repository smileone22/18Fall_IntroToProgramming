def horizontal_line(w):
    print("*"*w)

def vertical_line(s,h):
    for h in range(1,h+1):
        print((" "*s)+"*")

def two_vertical_lines(h,w):
    s=''
    for h in range(1,h+1):
        print("*"+((" ")*(w-2))+"*")
    

#DEFINING NUMBERS
def number_0(w):
    horizontal_line(w)
    two_vertical_lines(3,w)
    horizontal_line(w)
    
def number_1(w):
    vertical_line(w-1, 5)

def number_2(w):
    horizontal_line(w)
    vertical_line(w-1,1)
    horizontal_line(w)
    horizontal_line(1)
    horizontal_line(w)

def number_3(w):
    horizontal_line(w)
    vertical_line(w-1,1)
    horizontal_line(w)
    vertical_line(w-1,1)
    horizontal_line(w)
    
def number_4(w):
    two_vertical_lines(2,w)
    horizontal_line(w)
    vertical_line(w-1,2)

def number_5(w):
    horizontal_line(w)
    horizontal_line(1)
    horizontal_line(w)
    vertical_line(w-1,1)
    horizontal_line(w)

def number_6(w):
    horizontal_line(w)
    horizontal_line(1)
    horizontal_line(w)
    two_vertical_lines(1,w)
    horizontal_line(w)
    
def number_7(w):
    horizontal_line(w)
    vertical_line(w-1,4)
    
def number_8(w):
    horizontal_line(w)
    two_vertical_lines(1,w)
    horizontal_line(w)
    two_vertical_lines(1,w)
    horizontal_line(w)

def number_9(w):
    horizontal_line(w)
    two_vertical_lines(1,w)
    horizontal_line(w)
    vertical_line(w-1,2)

#DEFINING OPERATORS
def plus(w): 
    vertical_line(w//2,2)
    horizontal_line(w)
    vertical_line(w//2,2)

def minus(w):
    print()
    print()
    horizontal_line(w)
    print()
    print()

#PART 4
def check_answer(n1,n2,answer,operator):
    if operator=='+':
        if n1+n2==answer:
            return True
        else:
            return False
    elif operator=="-":
        if n1-n2==answer:
            return True
        else:
            return False
