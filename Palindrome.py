"""Check if a word is a palindrome
INPUT: malayalam
OUTPUT:TRUE
"""

def Palindrome(word):
    if word == word[::-1]:
        print("Yes")
    else:
        print("No")


def Iterative(word):
    for i in range(0,int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            print("no")
            return False
    print("yes")
    return True

