#В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился
from operator import truediv


FILE_NAME = '3_z2_icecream.txt'
try: 
    f = open(FILE_NAME, 'r')
except IOError:
    print('file '+FILE_NAME+' does not exist!')
else:
    s = f.readlines()
    products_all = s[0][:-1].split(',')
    products_available = s[1][:-1].split(',')

    def not_available_list(all, available):
        not_avaliable = []
        for i in all:
            flag = True
            for j in available:
                if i == j:
                    flag = False
                    break
            if flag:
                not_avaliable.append(i)
        return not_avaliable
    
    print(not_available_list(products_all, products_available))
