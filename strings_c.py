import random

def add_letters(word, number):
    encoded = ""
    for a in word:
        adding = ""
        for b in range(0, number):
            n1 = random.randint(65,90)
            n2 = random.randint(97,122)
            rand_n = random.randint(1,2)
            if rand_n == 1:
                n1 = 0
                letter = chr(n2)
            else:
                n2 = 0
                letter = chr(n1)
            adding += letter
        encoded += a + adding
    return encoded

def remove_letters (word,number):
  decoded = word[0:len(word) + 1:number + 1]
  return decoded

def shift_characters(word, number):
    shifted = ""
    for a in word:
        shift = chr(ord(a) + number)
        shifted += shift
    return shifted

option = input("(e)ncode, (d)ecode or (q)uit: ")
while option != "q":
    num = int(input("Enter a number between 1 and 5: "))
    while num > 5 or num < 0:
        num = int(input("Enter a number between 1 and 5: "))
    phrase = input("Enter a phrase to encode: ")
    if option == "e":
        print("Your encoded word is:", shift_characters(add_letters(phrase, num), num))
    if option == "d":
        print("Your decoded word is:", shift_characters(remove_letters(phrase, num), -num))
    print()
    option = input("(e)ncode, (d)ecode or (q)uit: ")
