
def isPalindrome(word):
    if word == word[::-1]:
        print("Yes")
    else:
        print("No")


def isPalindromeIterative(word):
    for i in range(0,int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            print("no")
            return False
    print("yes")
    return True

