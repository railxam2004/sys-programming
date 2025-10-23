from multiprocessing import Pool

def square(i):
    return i * i

def calculate_sum_of_squares(start, end):
    # создаём пул процессов используем все ядра
    with Pool() as pool:
        # распределяем вычисления по процессам
        squares = pool.map(square, range(start, end + 1))
    return sum(squares)

if __name__ == "__main__":
    N = int(input("Введите N: "))
    result = calculate_sum_of_squares(1, N)

    print(f"Сумма квадратов первых {N} натуральных чисел = {result}")
