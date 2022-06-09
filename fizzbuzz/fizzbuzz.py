def fizzbuzz(string: str) -> int | str:
    '''
    Returns "Fizz!" if a given number is divisible by 3,
    "Buzz!" if a number is divisible by 5,
    "FizzBuzz!" if a number is divisible by both 3 and 5,
    or the number otherwise. If a number is not a positive,
    non-zero integer number, returns the corresponding error message.

    Parameters:
        string: str

    Returns:
        int | str
    '''
    try:
        n = int(string)
    except ValueError:
        return('Submit an integer number.')

    if n <= 0:
        return('The number must be positive and non-zero.')
    elif n % 15 == 0:
        return 'FizzBuzz!'
    elif n % 3 == 0:
        return 'Fizz!'
    elif n % 5 == 0:
        return 'Buzz!'
    else:
        return n


def main():
    '''
    While user input is not empty and is a positive, non-zero integer number,
    prints fizzbuzz(n) for every number the user submits.

    Parameters:
        None

    Returns:
        None
    '''
    print('''
Welcome to Fizz Buzz!
Submit a number and get an answer.
To quit, enter an empty string.''')

    while n := input('Number: '):
        print(fizzbuzz(n))


if __name__ == '__main__':
    main()
