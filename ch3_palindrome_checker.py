from pythonds.basic.deque import Deque


def palindrome_check(inputStr):
    lettersDeq = Deque()
    for letter in inputStr.lower():
        lettersDeq.addRear(letter)
    palindrome = True
    while (lettersDeq.size() > 1) and palindrome:
        left = lettersDeq.removeRear()
        right = lettersDeq.removeFront()
        if left != right:
            palindrome = False
    return palindrome


print(palindrome_check("roar"))
print(palindrome_check("Kayak"))
print(palindrome_check("Adam"))
print(palindrome_check("lol"))
print(palindrome_check("noon"))
