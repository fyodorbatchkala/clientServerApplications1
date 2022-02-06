my_lst = ['class', 'function', 'method']
for i in my_lst:
    i = eval("b'" + i + "'")
    print(i)
    print(type(i))
    print(len(i))

# Результат
# b'class'
# <class 'bytes'>
# 5
# b'function'
# <class 'bytes'>
# 8
# b'method'
# <class 'bytes'>
# 6
