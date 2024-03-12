def fizz_buzz(i):
    if i % 5 == 0 and i % 3 == 0:
        return("FizzBuzz")
    elif i % 5 == 0:
        return("Buzz")
    elif i % 3 == 0:
        return("Fizz")
    return i

def main():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(20) == "Buzz"
    assert fizz_buzz(45) == "FizzBuzz"
    
if __name__ == '__main__':
    main()