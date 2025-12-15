import time
import random

def find_common_naive(arr1, arr2):
    start = time.perf_counter()
    """
    Наивный подход: O(n * m)
    Для каждого элемента arr1 проверяем, есть ли он в arr2
    """
    common = []
    for item in arr1:
        if item in arr2 and item not in common:
            common.append(item)
    time_set = time.perf_counter() - start
    return common, time_set 

def find_common_set(arr1, arr2):
    start = time.perf_counter()
    """
    Подход с множествами: O(n + m)
    Используем встроенную операцию пересечения множеств
    """
    set1 = set(arr1)
    set2 = set(arr2)
    time_set = time.perf_counter() - start
    return list(set1 & set2), time_set 

n = 50000
arr1 = [random.randint(1, 30000) for _ in range(n)]
arr2 = [random.randint(1, 30000) for _ in range(n)]
common, time_Set = find_common_naive(arr1, arr2)
common2, time_Set2 = find_common_set(arr1, arr2)

#with open('resultshw01.txt', 'w', encoding='utf-8') as f:
#with open('resultshw01.txt', 'w', encoding='utf-8') as f:
#with open('./resultshw01.txt', 'w', encoding='utf-8') as f:
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'resultshw01.txt')
with open(file_path, 'w', encoding='utf-8') as f:

    f.write("ДОМАШНЕЕ ЗАДАНИЕ 1 - РЕЗУЛЬТАТЫ \n")
    f.write(f"Размер array1: {n} \n")
    f.write(f"Размер array2: {n} \n")
    f.write(f"Диапазон значений: 1-30000: {n} \n")
    f.write("1: НАИВНЫЙ (вложенные циклы) \n")
    f.write(f"Время выполнения: {time_Set:.6f} секунд: \n")
    f.write(f"Найдено общих элементов: {len (common)}: \n")
    f.write("2: МНОЖЕСТВА (set intersection) \n")
    f.write(f"Время выполнения: {time_Set2:.6f} секунд: \n")
    f.write(f"Найдено общих элементов: {len (common2)}: \n")
