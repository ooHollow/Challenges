def solution(numbers):
    lista = []
    for n in range(numbers):
        if n % 3 == 0 or n % 5 == 0:
            lista.append(n)
    return sum(lista)