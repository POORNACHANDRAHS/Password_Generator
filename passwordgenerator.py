import string
import random

n=int(input("Enter The Size of Your password:  "))

s=string.ascii_letters+string.octdigits+string.hexdigits+string.punctuation

password="".join(random.choice(s) for i  in range(n))

print(password)