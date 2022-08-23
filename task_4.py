"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol',
'standard']

def toBytes(llist):
    out = []
    for i in range(len(llist)):
        current = llist[i].encode('utf-8')
        out.append(current)
    return out

def toString(llist):
    out = []
    for i in range(len(llist)):
        current = llist[i].decode('utf-8')
        out.append(current)
    return out

list1 = toBytes(words)
list2 = toString(list1)

print(list1)
print(list2)