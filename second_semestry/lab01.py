import time 
import random 

#1 Генерация данных
n = 100000
data = [random.randint(1, n // 2) for _ in range(n)] #список из 100к чисел от 1 до 50000
target = random.choice(data) #гарантом есть в дата

print(f"n={n}, target={target}")

#2 Поиск в списке (операция: target in data)
start = time.perf_counter() #старт таймера 
found_in_list = (target in data)
end = time.perf_counter()
list_time = end - start

#3 создание множества из списка, не поиск - это отдельная операция преобразования
data_set = set(data)

#4 поиск в множестве
start = time.perf_counter()
found_in_set = target in data_set
end = time.perf_counter()
set_time = end - start

#5 вывод результатов
print(f"Найдено в списке: {found_in_list}, время: {list_time:.8f} сек")
print(f"Найдено в множестве: {found_in_set}, время: {set_time:.8f} сек")
print(f"Ускорение: {list_time / set_time:.1f}x")
