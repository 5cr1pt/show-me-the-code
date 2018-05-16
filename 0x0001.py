# encoding: utf-8
# Generating a random code

import random

sstring = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

def genCode(sstring, length):
    return "".join(random.sample(sstring, length))

if __name__ == '__main__':
    length = input("Please input the length of the code: ") # code length
    total = input("How many do you want? ") # The total number of the code
    for i in range(int(total)):
        print(genCode(sstring, int(length)))