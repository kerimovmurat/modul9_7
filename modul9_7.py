def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования:
result = sum_three (2, 3, 6)
print (result)
