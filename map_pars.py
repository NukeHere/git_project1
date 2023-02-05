mask = ['1x1', '1x2', '2x1', '2x2', '1x3', '2x3', '3x2'][::-1]
b = ['', 'big_rock.png', 'small_rock.png', '3.png', '2.png']
a = []
f = open('1.txt')
for line in f:
    a.append(list(map(int, line.split(',')[:-1])))
sc = 0
for i in range(40):
    for j in range(40):
        if a[i][j] > 0:
            c = a[i][j]
            for m in mask:
                fl = True
                for x in range(int(m[0])):
                    for y in range(int(m[2])):
                        if i + y >= 40 or j + x >= 40:
                            fl = False
                            break
                        if a[i + y][j + x] != c:
                            fl = False
                if fl:
                    e = 1
                    if c > 2:
                        e = 0
                    print(f"{b[c]},{i * 50},{j * 50},{m},{e}")
                    for x in range(int(m[0])):
                        for y in range(int(m[2])):
                            a[i + y][j + x] = 0
                    break
