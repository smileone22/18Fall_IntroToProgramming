

v_name=input("Enter your Python variable name: ")


def keyword(v_name):
    if v_name[0].isnumeric():
        return False
    import keyword
    if keyword.iskeyword(v_name)==True:
        return False
    for characters in v_name:
        if (ord(characters)>=65 and ord(characters)<=90) or (ord(characters)>=97 and ord(characters)<=122) or (ord(characters)>=48 and ord(characters)<=57) or ord(characters)==95:
            return True
        
def main():
    if keyword(v_name)==True:
        print("This is a valid variable name")
    else:
        print("This is not a valid variable name")

main()
