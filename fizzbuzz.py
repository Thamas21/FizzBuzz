def fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number} is a FizzBuzz")
        elif number % 3 == 0:
            print(f"{number} is a Fizz")
        elif number % 5 == 0:
            print(f"{number} is a Buzz")
        else: 
            print(number)

fizzbuzz(60)
def fizzybuzzy():
    counter = 1
    while counter < 101:
        if counter % 3 == 0 and counter % 5 == 0:
            print(f"{counter} is a FizzBuzz")
        elif counter % 3 == 0:
            print(f"{counter} is a Fizz")
        elif counter % 5 == 0:
            print(f"{counter} is a Buzz")
        else: 
            print(counter)
        counter += 1
fizzybuzzy()