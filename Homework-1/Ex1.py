lst1 = ['разработка', 'сокет', 'декоратор']
lst2 = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
        '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for i in lst1:
    print(type(i))

for i in lst1:
    print(i)

for i in lst2:
    print(type(i))

for i in lst2:
    print(i)

# Результат
# <class 'str'>
# <class 'str'>
# <class 'str'>
# разработка
# сокет
# декоратор
# <class 'str'>
# <class 'str'>
# <class 'str'>
# разработка
# сокет
# декоратор
