#import the necessary mods

import random
import string

print('Hello, Welcome to the password generator!')

#user inputs length of password
length = int(input('\nEnter the length of password:'))

#defines the data used
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combines the data used
all = lower + upper + num + symbols

#creates random sets
temp = random.sample(all,length)

#creates the password
password = "".join(temp)
print(password) 
