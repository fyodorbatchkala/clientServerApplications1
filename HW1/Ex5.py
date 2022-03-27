import chardet
import subprocess
import platform
import locale


# YANDEX
param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
result = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in result.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


# YOUTUBE
param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'youtube.com']
result = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in result.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


default_encoding = locale.getpreferredencoding()
print(default_encoding)
