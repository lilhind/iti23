# 1. Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'O', 'E', 'I', 'U']
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

#print(count_vowels("ShAmed mo ea"))


# 2. Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.

def sort_array():
    elements = []

    for i in range(5):
        element = input()
        elements.append(element)

    elements.sort(reverse=True)
    print("Descending order:", elements)

    elements.sort()
    print("Ascending order:", elements)

#sort_array()

# 3. Write a program that prints the number of times the string 'iti' occurs in anystring.

def count_iti(str):
    return str.count("iti")
    
#print(count_iti("itiahmeditiaaiti"))

# 4. Write a program that remove all vowels from the input word and generate a brief version of it.

def remove_vowels(word):
    vowels = ['a','o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
    new_word = ""
    for char in word:
        if char not in vowels:
            new_word += char
    return new_word

#print(remove_vowels("ahmed"))

# 5. Write a program that prints the locations of "i" character in any string you added

def print_locations(str):
    for i in range(len(str)):
        if str[i] == "i":
            print(i)

#print_locations("ahmiedi")

# 6. Write a program that generate a multiplication table from 1 to the number passed.

def multiplication_table(n):
    l = []
    for i in range(1,n+1):
        current_num = []
        for j in range(1,i+1):
                current_num.append(i*j)
        l.append(current_num)
    return l
            
#print(multiplication_table(5))


# 7. mario

def mario(n):
    for i in range(n):
        space = " " * (n - i - 1)
        star = "*" * (i + 1)
        print(space + star)

#mario(5)