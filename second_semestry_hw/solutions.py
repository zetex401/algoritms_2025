import time
import random

def find_common_naive(arr1, arr2):
    """
    Наивный подход: O(n * m)
    Для каждого элемента arr1 проверяем, есть ли он в arr2
    """
    common = []
    for item in arr1:
        if item in arr2 and item not in common:
            common.append(item)
    return common

def find_common_set(arr1, arr2):
    """
    Подход с множествами: O(n + m)
    Используем встроенную операцию пересечения множеств
    """
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)

n = 50000
arr1 = [random.randint(1, 30000) for _ in range(n)]
arr2 = [random.randint(1, 30000) for _ in range(n)]

#with open('resultshw01.txt', 'w', encoding='utf-8') as f:
#with open('resultshw01.txt', 'w', encoding='utf-8') as f:
#with open('./resultshw01.txt', 'w', encoding='utf-8') as f:
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'resultshw01.txt')
with open(file_path, 'w', encoding='utf-8') as f:

    f.write("ДОМАШНЕЕ ЗАДАНИЕ 1 - РЕЗУЛЬТАТЫ \n")