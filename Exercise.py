# perfect squares

ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")

'''Lets c another problem
fibonacci
'''


def fib(x):
    '''assumes x an int >= 0
       returns Fibonacci of x'''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)



#testing for palindromes

'''def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    #return isPal(toChars(s))

 print(isPalindrome('eve'))

 print(isPalindrome('Able was I, ere I saw Elba'))

 print(isPalindrome('Is this a palindrome'))'''
