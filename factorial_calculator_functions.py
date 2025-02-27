def get_non_negative_integer():
    n = int(input("Enter a non-negative integer: "))
    return n

def calculate_factorial(n):
    if n == 0:
        return 1

    factorial = 1
    for i in range(1, n + 1):

        factorial *= i

    return factorial


n_final = get_non_negative_integer()
result = calculate_factorial(n_final)
print(f"The factorial of {n_final} is {result}.")
