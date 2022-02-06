my_lst = ['attribute', 'класс', 'функция', 'type']


def my_checker(my_str):
    try:
        my_str = eval("b'" + my_str + "'")
        print(f'{my_str} - возможно')
    except ValueError or SyntaxError:
        print(f'{my_str} - невозможно')


for i in my_lst:
    my_checker(i)

# Результат
# b'attribute' - возможно
# класс - невозможно
# функция - невозможно
# b'type' - возможно
