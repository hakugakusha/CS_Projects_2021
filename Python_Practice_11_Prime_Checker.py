# Ask the user for a number and determine whether the number is prime or not.
number = int(input("Please enter a number: "))
def is_prime(n):
    if n > 1:
        for value in range(2, n):
            if n % value == 0:
                return False
        return True
    else:
        return False
# don't use outside variables inside the function!
print(is_prime(number))

