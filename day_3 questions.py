#write a python funtion, nearest palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
import sys
def near_palindrome(n):
    for i in range(n+1,sys.maxsize):
        if str(i)==str(i)[:: -1]:
            return i
            
print(near_palindrome(99))
