"""Вывести на экран все простые числа до заданного."""

def is_prime(num):
    if num <= 3:
      return num > 1
    elif num % 2 == 0 or num % 3 == 0:
      return False
    else:
        i = 5
        while i*i<=num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

def simple_numbers():
    max_numbers = input('Введіть до якого числа вивести прості числа: ')
    max_numbers = int(max_numbers)
    if max_numbers<2:
        print('Простих чисел не виявлено')
    else:
        for number in range(max_numbers):
            if is_prime(number):
                print(number)

if __name__ == '__main__':
    simple_numbers()
