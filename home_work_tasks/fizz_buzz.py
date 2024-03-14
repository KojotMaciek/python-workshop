def fizz_buzz(i):
    if i % 5 == 0 and i % 3 == 0:
        return("FizzBuzz")
    elif i % 5 == 0:
        return("Buzz")
    elif i % 3 == 0:
        return("Fizz")
    return i
