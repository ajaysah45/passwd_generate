#! /usr/bin/python3

import random
import string
print("Welcome to Password Generator")
length=int(input("enter the length of password: "))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digit
total=lower+upper+digit

temp=random.sample(total,length)
password="".join(temp)
print(password)

