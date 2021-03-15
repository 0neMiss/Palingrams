
"""
Arguments:
    * An set of the words.
Returns:
    *A list of palindromes from the set provided.
"""

def palindrome(word_set):
    palindromes = []
    for word in word_set:
        end = len(word)
        rev = word[::-1]
        if end > 1:
           for i in range(end):
               if word[i:] == rev[:end-i] and rev[end-i:] in word_set:
                   palindromes.append((word, rev[end-i:]))
               if word[:i] == rev[end-i:] and rev[:end-i] in word_set:
                   palindromes.append((rev[:end-i], word))
    return palindromes
    
    print(palindromes)