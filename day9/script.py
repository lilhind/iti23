# 1. Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start.


def return_arr(length, start):
    arr = []
    for i in range(length):
        arr.append(start + i)
    return arr


#print(return_arr(5, 2))

# write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"


def fizz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"

#print(fizz(10))


# Write a function which has an input of a string from user then it will return the same string reversed

def reverse_string(string):
    return string[::-1]

#print(reverse_string("hello"))

# Ask the user for his name then confirm that he has entered his name(not an empty string/integers). then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not

def user_info():
    name = input("Enter your name: ")
    while name == "" or name.isalpha():
        name = input("Enter your name: ")
    email = input("Enter your email: ")
    while email == "":
        email = input("Enter your email: ")
    if "@" not in email or "." not in email:
        print("Invalid email")
        email = input("Enter your email again: ")
    
    return f"Name: {name}, Email: {email}"

# Write a function that takes a string and prints the longest alphabetical ordered substring occurred For example, if the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu

def longest_substring(string):
    
    if len(string)==0:
        return ""
    s,e=0,1
    current_record = ""
    longest = ""
    longest += string[s]
    while e < len(string):
        if string[s] < string[e]:
            s += 1
            longest += string[e]
        else:
            if len(current_record) < len(longest):
                current_record = longest
                longest = ""
                s = e
        e += 1
    return current_record

#print(longest_substring("abdulrahman"))

"""
● Write a program which repeatedly reads numbers until the user 
enters “done”.
○ Once “done” is entered, print out the total, count, and 
average of the numbers.
○ If the user enters anything other than a number, detect their 
mistake, print an error message and skip to the next number.
"""

def get_numbers(*args):
    total = 0
    count = 0
    current = 0
    for i in args:
        try:
            current = int(i)
        except ValueError:
            print("Invalid input")
            continue
        if i == "done":
            break
        else:
            total += int(i)
            count += 1
    return f"Total: {total}, Count: {count}, Average: {total/count}"


#print(get_numbers(1,2,3,4,5,6,7,8,9,10,"done"))

"""
Word guessing game (hangman)
○ A list of words will be hardcoded in your program, out of 
which the interpreter will
○ choose 1 random word.
○ The user first must input their names
○ Ask the user to guess any alphabet. If the random word 
contains that alphabet, it
○ will be shown as the output(with correct placement)
○ Else the program will ask you to guess another alphabet.
○ Give 7 turns maximum to guess the complete word.
"""

import random

def hangman():
    words = ["ahmed", "mohamed", "reda", "nada", "ibrahim", "moaz"]
    word = random.choice(words)
    guessed_word = ""
    for i in range(len(word)):
        guessed_word += "_"
    print("current word: ", guessed_word)
    username = input("enter your name: ")
    turns = 7
    guessed = []
    while turns > 0:
        guess = input("Guess a letter: ")
        if guess in word:
            print("You guessed this litter correctly!")
            index = word.index(guess)
            guessed_word = guessed_word[:index] + guess + guessed_word[index+1:]
            print("current word: ", guessed_word)
            continue
        else:
            turns -= 1
            print(f"Incorrect! You have {turns} turns left")
    else:
        print("You lose!")

hangman()