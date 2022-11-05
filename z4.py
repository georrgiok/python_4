# Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
def open_file(path, p = 'r'):
    try: 
        f = open(path, p)
    except IOError:
        print('file '+FILE_NAME+' does not exist!')
        return False
    else:
        return f

def sup_int(i):
    if i =='':
        return 1
    return int(i)


def make_mch_list(str):
    list = {}
    tmp = str.split()
    z = 1
    for i in tmp:
        z = 1
        if i == "+":
            continue
        elif i == "-":
            z = -1
            continue
        a = i.split('x')
        if len(a) == 1:
            if 0 in list:
                list[0] += int(a[0])
            else:
                list[0] = int(a[0])
            continue
        elif len(a) == 2:
            list[sup_int(a[1][1:])] = sup_int(a[0]) * z
        else:
            print('parse err')
            break
    return list

def print_mch(mch):
    text = ''
    for i in mch:
        if i == 0:
            text = str(mch[i]) + text
        else:
            if i == 1:
                t = "x"
            else:
                t = "x^" + str(i)
            text = str(mch[i]) + t + text
        if mch[i] >= 0:
            text = " + "+ text
        else: 
            text = " - "+ text
    return text[3:]

def sum_mch(mch1, mch2):
    list = {}
    def add(mch):
        for i in mch:
            if i in list:
                list[i] += mch[i]
            else:
                list[i] = mch[i]
    add(mch1)
    add(mch2)
    return list


f1 = make_mch_list(open_file('3_z4_1.txt').read())
f2 = make_mch_list(open_file('3_z4_2.txt').read())

print(f1)
print(f2)

print(print_mch(sum_mch(f1,f2)))
