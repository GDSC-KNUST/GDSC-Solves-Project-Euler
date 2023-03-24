# AUTHOR: Fransay
# DATE: 24/93/23
# DESCRIPTION: A program that output the sum of the multiples of 3 or 5 less than 1000

LIMIT = 1000

def multiples_of_three(number):
    """returns a bool representation whether a number is three or not"""
    if number%3 == 0:
        return True 
    return False 

def multiples_of_five(number):
    """
    returns a bool representation whether a number is five or not
    """
    if number%5 == 0:
        return True
    return False


def main():
    """
    returns the sum of the multiples of 3 or 5 less than 1000
    """
    counter = 0
    sum = 0
    while counter < LIMIT:
        if multiples_of_three(counter) | multiples_of_five(counter):
            sum += counter
        counter+=1
    return sum


if __name__ == '__main__':
    print(main())
