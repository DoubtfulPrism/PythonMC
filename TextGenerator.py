import random
import string

vowels ='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'

letters=string.ascii_lowercase

letterInput1=input("what letter do you want to? enter 'v' for vowels, 'c' for consonants, 'l for any letter:  ")
letterInput2=input("what letter do you want to? enter 'v' for vowels, 'c' for consonants, 'l for any letter:  ")
letterInput3=input("what letter do you want to? enter 'v' for vowels, 'c' for consonants, 'l for any letter:  ")

def plot():
    if letterInput1=='v':
        l1=random.choice(vowels)
    elif letterInput1=='c':
        l1=random.choice(consonants)
    elif letterInput1 == 'l':
        l1=random.choice(letters)
    else:
        l1=letterInput1

    if letterInput2 == 'v':
        l2 = random.choice(vowels)
    elif letterInput2 == 'c':
        l2 = random.choice(consonants)
    elif letterInput2 == 'l':
        l2 = random.choice(letters)
    else:
        l3 = letterInput3

    if letterInput3 == 'v':
        l3 = random.choice(vowels)
    elif letterInput3 == 'c':
        l3 = random.choice(consonants)
    elif letterInput3 == 'l':
        l3 = random.choice(letters)
    else:
        l3 = letterInput3

    name=l1+l2+l3
    return (name)

for i in range(10):
    print(plot())