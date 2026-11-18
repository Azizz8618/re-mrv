#!/usr/bin/env python3
"""Нормализация омоглифов в полях кода МАДЛЕН (комментарии и GOST-текст не трогаем)."""
import re, sys

MAP = str.maketrans({
    'А':'A','В':'B','Е':'E','К':'K','М':'M','Н':'H','О':'O','Р':'P','С':'C',
    'Т':'T','Х':'X','У':'Y','Г':'G','І':'I','Ј':'J','ѕ':'s','Р':'P',
})

def norm_code(line):
    # разделитель инлайн-комментария: точка после пробела
    m = re.search(r'(?<=\s)\.', line)
    code, comment = (line[:m.start()], line[m.start():]) if m else (line, '')
    # GOST-литерал: нормализуем только ключевое слово, текст литерала сохраняем
    g = re.search(r'[GГ][OО][SС][TТ]', code)
    if g:
        kw = code[g.start():g.start()+4].translate(MAP)
        code = code[:g.start()] + kw + code[g.start()+4:]
    else:
        code = code.translate(MAP)
    return code + comment

def main(src, dst):
    out = []
    for line in open(src, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('C'):
            out.append(line)
        else:
            out.append(norm_code(line))
    open(dst, 'w', encoding='utf-8').write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
