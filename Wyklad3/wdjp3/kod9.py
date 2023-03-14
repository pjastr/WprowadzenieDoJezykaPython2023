import string

n1 = "ąśuww"
print(n1.upper())
for elem in n1:
    if elem in string.ascii_lowercase:
        print(elem)