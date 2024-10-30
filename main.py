"""
If the number is a multiple of 3 and not 5 you print fizz. If its multiple
of 5 and not 3 print out buzz and if it's a multiple of both you print out fizzbuzz. 
And if its not a multiple of either you just print out the number
"""

def fizz_buzz (n):
    if n % 3 == 0 and n % 5 != 0:
        print('fizz')
    elif n % 5 == 0 and n % 3 != 0:
        print('buzz')
    elif n % 5 == 0 and n % 3 == 0:
        print ('fizzbuzz')
    else:
        print (n)
fizz_buzz(15)