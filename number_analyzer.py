'''
Laurel Lynn
IS 303 - A04

Number Analyzer

This program collects numbers and produces statistical analysis including:
- mean
- min
- max
- range
- count above average

Inputs:
- Collect numbers (int)

Processes: 
-get_valid_int(prompt): keeps asking until user enters a valid number (try/except)
    - except: ValueError
- import math library
- calculate each of the following 
    - mean(prompt): sum/ number of entries
    - min(prompt): finds the smallest number
    - max(prompt): finds the largest number
    - range(prompt): counts the distance from the lowest number to the highest number
    - count_above_average(prompt): what is in the upper quartile
- display_summary(mean, min, max, range, count_above_average): prints formatted totals

Outputs: 
- display total for each of the above

'''

#Constants
import math
prompt = (f"Enter a whole number: ")

#Functions

def get_valid_int(prompt):
    while True: 
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number. Try again! ")

numbers = []
while True:
    number = get_valid_int("Enter a whole number: ")
    numbers.append(number)
    another = input(f"Would you like to enter another number? ")
    if another.lower() != "yes":
        break


def calculate_mean(numbers):
    mean = math.fsum(numbers) / len(numbers)
    return mean

def calculate_min(numbers):
    minimum = min(numbers)
    return minimum

def calculate_max(numbers):
    maximum = max(numbers)
    return maximum

def calculate_range(numbers):
    result_range = max(numbers) - min(numbers)
    return result_range

def calculate_above(numbers):
    mean = calculate_mean(numbers)
    above = [x for x in numbers if x > mean]
    return len(above)


#Main
mean = calculate_mean(numbers)
minimum = calculate_min(numbers)
maximum = calculate_max(numbers)
result_range = calculate_range(numbers)
above = calculate_above(numbers)
print(f"--- Number Analyzer System ---")
print(f"Mean: {mean:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {result_range}")
print(f"How many numbers above the mean: {above}")