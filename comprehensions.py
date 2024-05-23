#[list comprehension] Given two lists of integers, create a list that contains the product of each element of the first list with 
# the corresponding element in the second list using list comprehension.

def crossprod(list1,list2):
    product = [(list1[i]*list2[i]) for i in range(len(list1))]
    return product

list1 = [1, 2, 3]
list2 = [4, 5, 6]

product = crossprod(list1,list2)
print(product)

#[list comprehension] Given three lists list1, list2, and list3, each containing integers, 
# write a Python program using list comprehension to generate a new list of unique triplets (x, y, z) where x is from list1,
# y is from list2, and z is from list3, such that x + y + z = 0.

def zerosum(list1,list2,list3):
    sum = [(list1[i],list2[i],list3[i]) for i in range(len(list1)) if (list1[i]+list2[i]+list3[i] == 0)]
    return sum

list1 = [1, 2, 3,8]
list2 = [4, 5, 6, -12]
list3 = [-5, -7, 9, 4]

zerosum = zerosum(list1,list2,list3)
print(zerosum)

#[dictionary comprehension] Given a dictionary with students' names as keys and their respective scores as values, 
# create a new dictionary that contains only the students who scored more than 80 using dictionary comprehension.

def above80(student_scores):
    high_scorers = {name: score for name, score in student_scores.items() if score > 80}
    return high_scorers

student_scores = {
    'Armaan': 85,
    'Yeet': 75,
    'Charles': 92,
    'David': 88,
    'Eve': 72,
    'Frank': 90
}

print(above80(student_scores))

#[dictionary comprehension] Create a dictionary using dictionary comprehension to represent the ASCII values of lowercase alphabets (a-z) 
# where the keys are the alphabets, and the values are their corresponding ASCII values.
import string  

def ASCII():
    ascii = {char : ord(char) for char in string.ascii_lowercase}
    return ascii

print(ASCII())

#[set comprehension] Given a list of words, write a Python program to create a set using set comprehension that 
# contains all the unique characters present in the words.
def uniq(words):
    uniq = {char for word in words for char in word}
    return uniq

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(uniq(words))

#[set comprehension] Given two strings, write a Python program to create a set using set comprehension that 
# contains all the characters that are common in both strings.

def common(word1, word2):
    common = {char for char in set(word1) & set(word2)}
    return common

print(common("something","nothing"))