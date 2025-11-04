import time
import random
totl_time = 0
right_answer = 0
N = int(input("Количество строк: "))
for i in range(N):
    print(f"{i + 1}/{N}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    while True:
        try:
            start_time = time.time()
            answer = int(input(f"{a} × {b} = "))
            time_spend = time.time() - start_time
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    totl_time += time_spend
    if answer == a*b:
        right_answer+=1
        print(f"Верно(Время:{time_spend:.1f}сек.)")
    elif answer != a*b:
        print(f"Неверно! Правильно: {a*b}(Время:{time_spend:.1f}сек.)")
print(f"=" * 50)
print("СТАТИСТИКА:")
print(f"=" * 50)
print(f"Общее время:{totl_time:.1f}")
print(f"Cреднее время на вопрос:{totl_time / N:.1f}")
print(f'Правильных ответов:{right_answer}/{N}')
print(f"Процент правильных: {right_answer*100 / N}%")