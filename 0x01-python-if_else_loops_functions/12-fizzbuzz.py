#!/usr/bin/python3
def fizzbuzz():
    i = range(1,101)
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    return(i)
