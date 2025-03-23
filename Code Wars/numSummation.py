"""
Write a program that finds the summation of every number from 1 to num (both inclusive). The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

def summation(num):
    sum = 0
    for i in range(1, num + 1):
        if num > 0:
            sum += i
    return sum

"""

number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print(f"Sum: {sum}")
