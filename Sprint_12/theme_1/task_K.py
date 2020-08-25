"""Пока Вася писал программу про степени четверки, погода на улице ухудшилась.
Он долго не расстраивался и придумал новую задачку! Ему нравится работать с
системами счисления. И вот что на этот раз получилось: Дано целое положительное
число. Нужно посчитать, сколько 1 встречается в двоичной записи этого числа.

Формат ввода
На вход подается число в диапазоне от 1 до 10000

Формат вывода
Выведите одно число - количество единиц."""


def solution(n: str) -> int:
    count = 0
    for i in n:
        if i == '1':
            count += 1
    return count


if __name__ == '__main__':
    n = str(format(int(input()), 'b'))
    print(solution(n))