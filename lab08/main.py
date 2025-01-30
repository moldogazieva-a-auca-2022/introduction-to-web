def square(num):
    return num ** 2

number = 5
print(f"The square of {number} is {square(number)}")

def sum_of_numbers(numbers):
    return sum(numbers)

numbers_list = [1, 2, 3, 4, 5]
print(f"The sum of the numbers is {sum_of_numbers(numbers_list)}")

def fibonacci(n):
    if n <= 1:
        return n
    # Recursive call
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
print(f"The {n}th Fibonacci number is {fibonacci(n)}")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 7
print(f"Is {number} a prime number? {is_prime(number)}")