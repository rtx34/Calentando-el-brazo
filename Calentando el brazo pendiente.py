# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:09:41 2021

@author: jorge
"""
import numpy as np
import re
from math import prod
from math import sqrt
from collections import Counter

#=================================1================================

class Solution:
   def solve(self, palabras):
      s = "".join(palabras[0].upper() + palabras[1:].lower() for palabras in palabras)
      return s[0].lower() + s[1:]
ob = Solution()
palabras = ["Hello", "World", "Python", "Programming"]
print(ob.solve(palabras))

#==================================2================================

def conversion(palabra):
    conversion = re.sub('([a-z][A-Z]+)(.)', r'\1_\2', palabra)
    
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2' , conversion).lower()

print(conversion('Hola Mundo'))

#==================================3================================

def kebab(s):
  return '-'.join(
   re.sub(r"(\s|_|-)+"," ",
   re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
print(kebab('Hola Mundo'))

#==================================4===============================

test_str = 'Hola Mundo'
print("The original string is : " + test_str)
res = test_str.replace("_", " ").title().replace(" ", "") 
print("Cambiado : " + str(res))

#==================================5===============================

def conversion(palabra):
    conversion = re.sub('([a-z][A-Z]+)(.)', r'\1_\2', palabra)
    
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2' , conversion).upper()

print(conversion('Hola Mundo'))

#==================================6===============================

s1 = '  abc  '

print(f'String =\'{s1}\'')

print(f'After Removing Leading Whitespaces String =\'{s1.lstrip()}\'')


#==================================7===============================

print(f'After Removing Trailing Whitespaces String =\'{s1.rstrip()}\'')

#==================================8===============================

print(f'After Trimming Whitespaces String =\'{s1.strip()}\'')

#==================================9===============================

list1 = [5, 6, 9]
list2 = [1, 2, 3]

  
vector1 = np.array(list1)
vector2 = np.array(list2)
reversed_arr = vector1[::-1]

  

addition = vector1 + vector2
print("Vector Addition       : " + str(addition))
  


#==================================10==============================

subtraction = vector1 - vector2
print("Vector Subtraction   : " + str(subtraction))

#==================================11===============================

print(addition * 2)

#==================================12===============================

print(vector1 * 2)

#==================================13=============================

print(reversed_arr)

#==================================14==============================
#==================================15==============================
#==================================16==============================

def calcularPersistenciaAditiva(numero, cont):
    if numero < 10:
        return 'Respuesta: %s' % cont
 
    cont += 1
    lista = []
    numero = str(numero)
    for i in numero:
        lista.append(int(i))
 
    numeronuevo = sum(lista)
    print(cont, numero, numeronuevo)
    if numeronuevo < 10:
        return 'Respuesta: %s' % cont
    else:
        return calcularPersistenciaAditiva(numeronuevo, cont)
 
print (calcularPersistenciaAditiva(5978, 0))

#==================================17==============================

n = 969

def primer_persistente(n):
    digitos = [int(i) for i in str(n)] # Lista con los digitos separados 
    persistencia = [prod(digitos)] # Lista con el producto de todos los digitos

    if len(digitos) != len(persistencia):
        print(persistencia[0])
        primer_persistente(persistencia[0])

primer_persistente(n)

#==================================18==============================

class Ecuaciones2Grado():
    def calcular(self, A, B, C):
        if ((B**2)-4*A*C) < 0:
            print("La solución de la ecuación es con números complejos")
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            print("""\
Las soluciones de la ecuación son:
x1 = {}
x2 = {} """.format(x1, x2))
ec1 = Ecuaciones2Grado()
ec1.calcular(1,-5,6)
ec2 = Ecuaciones2Grado()
ec2.calcular(2,-7,3)

#==================================19==============================

datos = [1,3,2,4,7,3,2,2,1,4]
result = []
for item in datos:
    if item not in result:
        result.append(item)
        
print(result)

#==================================20==============================

result = []
for item in datos:
    if item not in result:
        result.append(item)
        
print(result)


#==================================21==============================

# Python3 program for the above approach

 
# function to check if two strings are
# anagram or not
def check(s1, s2):
   
    # implementing counter function
    if(Counter(s1) == Counter(s2)):
        print("Son anagrams.")
    else:
        print("No son anagrams.")
 
 
# driver code
s1 = "FORM"
s2 = "FROM"
check(s1, s2)

#==================================22==============================

def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A

A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)

#==================================23==============================

def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length-1])
    print("Smallest element is:", list1[0])
    print("Second Largest element is:", list1[length-2])
    print("Second Smallest element is:", list1[1])
  
# Driver Code
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)

#==================================24==============================

def reverseWordSentence(Sentence):
  

    words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
  
    return newSentence
  
Sentence = "GeeksforGeeks is good to learn"

print(reverseWordSentence(Sentence))

#==================================25==============================

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

#==================================26==============================

print("012345".isdecimal())

#==================================27==============================

vowels = ['a', 'e', 'i', 'o', 'u']

#input a string and transform it to lower case
str = ("hola mundo")

#define counter variable for both vowels and consonants
v_ctr = 0
c_ctr = 0

#iterate through the characters of the input string 
for x in str:
    #if character is in the vowel list,
    #update the vowel counter otherwise update consonant counter
    if x in vowels:
        v_ctr += 1
    else:
        c_ctr += 1

#output the values of the counters
print("Vowels: ", v_ctr)
print("Consonants: ", c_ctr)

#==================================28==============================

a = "546"
result = 0
for digit in a:
    result *= 10
for d in '0123456789':
    result += digit > d
          
    print(result)    

#==================================29==============================

def my_mean(sample):
     return sum(sample) / len(sample)
 
print(my_mean([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))

def my_median(sample):
     n = len(sample)
     index = n // 2

     if n % 2:
         return sorted(sample)[index]

     return sum(sorted(sample)[index - 1:index + 1]) / 2
 
print(my_median([3, 5, 1, 4, 2]))

def my_mode(sample):
     c = Counter(sample)
     return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

print(my_mode([4, 1, 2, 2, 3, 5]))


#==================================30==============================

A = {3, 1, 2};
B = {2, 2, 1, 5};
  
# union
print("Union :", A | B)
  
# intersection
print("Intersection :", A & B)
  
# difference
print("Difference :", A - B)