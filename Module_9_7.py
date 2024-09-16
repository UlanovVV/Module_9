def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)      # Переменная для расчетов и сбора данныех с функции
        if res > 1:
            for i in range(2, int(res*0.5) + 1):     # Выбор диапазона для проверки простого числа
                if res % i == 0:     # Проверка на целочисленное деление
                    print("Составное")
                    return res
            print("Простое")
            return res
        else:
            print("Составное")
            return res
    return wrapper


@is_prime
def sum_three(*args):
    total = sum(args)
    return total


result = sum_three(2, 3, 6)
print(result)