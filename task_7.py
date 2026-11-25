"""Дополнительное задание 2. Цифровой корень натурального числа."""


def digit_root(num):
    while num > 9:
        digits_sum = 0
        for digit in str(num):
            digits_sum += int(digit)
        num = digits_sum
    return num


if __name__ == '__main__':
    print(digit_root(4851))
    print(digit_root(97569))
    print(digit_root(889987))
