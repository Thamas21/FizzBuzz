def fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number} is a FizzBuzz")
        elif number % 3 == 0:
            print(f"{number} is a Fizz")
        elif number % 5 == 0:
            print(f"{number} is a Buzz")

fizzbuzz(50)