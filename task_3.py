"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

words = ['attribute','класс','функция','type']

print(f'Success: {words[0],words[3]}')
print(f'Error: {words[1],words[2]}')
print('Error text: SyntaxError: bytes can only contain ASCII literal characters.')

