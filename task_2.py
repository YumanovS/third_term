"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = [b'class', b'function',b'method']

for i in range(len(words)):
    print(f'Value: {words[i]}\nType: {type(words[i])}\nLength: {len(words[i])}\n')