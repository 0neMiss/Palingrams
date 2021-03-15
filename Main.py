from Load import load
from Palindrome import palindrome

dictionary = load('dictionary.txt')
palendromes = palindrome(dictionary)

print(palendromes)