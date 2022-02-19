"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess

ARGS = [['ping', '-c 4', 'yandex.ru'], ['ping', '-c 4', 'youtube.com']]

for args in ARGS:
    site_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in site_ping.stdout:
        res = chardet.detect(line)
        line = line.decode(res['encoding'])
        print(line)

