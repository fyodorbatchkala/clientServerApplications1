from chardet import detect


f = open('test_file.txt', 'w', encoding='utf-8')
f.write('сетевое программрование\nсокет\nдекоратор')
f.close()

with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

with open('test_file.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        el_str.encode('ascii', 'xmlcharrefreplace')  # Если символ будет не в правильной кодировке, он прочитается
        print(el_str, end='')
    print()

# Результат
# encoding:  utf-8
# сетевое программирование
# сокет
# декоратор
