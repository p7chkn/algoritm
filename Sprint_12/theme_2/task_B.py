"""Алла получила задание, связанное с мониторингом работы различных серверов.
Требуется понять, сколько времени обрабатываются определённые запросы на
конкретных серверах. Эту информацию нужно хранить в матрице, где номер столбца
соответствуют идентификатору запроса, а номер строки — идентификатору сервера.
Алла перепутала строки и столбцы местами. С каждым бывает. Помогите ей
исправить баг.

Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.

Транспонированная матрица получается из исходной замены строк на столбцы.

Например, для матрицы А


транспонированной будет следующая матрица:


Формат ввода
В первой строке задано число n - количество строк матрицы. Во второй строке -
m - число столбцов, m и n не превосходит 1000. В следующих n строках задана
матрица. Числа в матрице по модулю не превосходят 1000.

Формат вывода
Напечатайте транспонированную матрицу в том же формате."""


def solution(lst: list, n: int, m: int) -> list:
    result = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(lst[j][i])
        result.append(temp)
    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    lst = [[int(i) for i in input().split()] for _ in range(n)]
    for i in solution(lst, n, m):
        print(*i)