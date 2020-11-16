
text = input('Enter a text to analyze: ')
ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
total_character = len(text)
total_ASCII = 0

for a in text:
    for A in ASCII:
        if a == A:
            total_ASCII += 1

total_non_ASCII = total_character - total_ASCII

print("Total number of characters:", total_character)
print("Total number of ASCII characters:", total_ASCII)
print("Total number of non-ASCII characters:", total_non_ASCII)
