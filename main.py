import os


def human_read_format(size):
    i = 0
    a = [''] + list('КМГ')
    size = int(size)
    while size >= 1024:
        i += 1
        size = round(size / 1024)
    return str(size) + a[i] + 'Б'


def get_files_sizes():
    a = []
    for cdr, dr, fl in os.walk('.'):
        for i in fl:
            if os.path.isfile(cdr + '/' + i):
                a.append(i + ' ' + human_read_format(os.path.getsize(cdr + '/' + i)))
    return '\n'.join(a)


if __name__ == '__main__':
    print(get_files_sizes())
