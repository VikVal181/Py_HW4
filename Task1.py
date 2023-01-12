# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
def create_dict():
    number = int(input('Введите порядок многочлена: '))
    my_dict = {}
    for i in range(number, -1, -1):
        if i == number:
            while True:
                k = randint(-100,100)
                if k != 0:
                    break
            my_dict[i] = k
        else:
            my_dict[i] = randint(-100, 100)
    return my_dict

def write_polynom(polynom_dict):
    polynom = ''
    for key in polynom_dict:
        if polynom_dict[key] == 0:
            polynom += ''
        elif polynom_dict[key] == 1:
            if key == 1:
                polynom += '+x'
            elif key == 0:
                polynom += '+1'
            else:
                polynom += '+x**' + str(key)
        elif polynom_dict[key] == -1:
            if key == 1:
                polynom += '-x'
            elif key == 0:
                polynom += '-1'
            else:
                polynom += '-x**' + str(key)
        else:
            if polynom_dict[key] > 0:
                if key == 0:
                    polynom += '+' + str(polynom_dict[key])
                elif key == 1:
                    polynom += '+' + str(polynom_dict[key]) + '*x'
                else:
                    polynom += '+' + str(polynom_dict[key]) + '*x**' + str(key)
            elif polynom_dict[key] < 0:
                if key == 0:
                    polynom += str(polynom_dict[key])
                elif key == 1:
                    polynom += str(polynom_dict[key]) + '*x'
                else:
                    polynom += str(polynom_dict[key]) + '*x**' + str(key)

    # if polynom.startswith('+'):
    polynom = polynom.removeprefix('+')
    return polynom

def parse_polynom(polynom):
    polynom_list = polynom.replace('-', ' -').replace('+', ' ').split(' ')
    if polynom_list[0] == '':
        polynom_list.pop(0)
    # print(polynom_list)

    polynom_dict = {}
    for p in polynom_list:
        param = p.split('*x**')
        # print(param)
        if len(param) == 2:
            polynom_dict[int(param[1])] = int(param[0])
        else:
            if param[0].endswith('x'):
                if param[0].startswith('x'):
                    polynom_dict[1] = 1
                elif param[0].endswith('*x'):
                    param = param[0].split('*x')
                    polynom_dict[1] = int(param[0])
                else:
                    polynom_dict[1] = -1
            elif param[0].startswith('x'):
                param = param[0].split('x**')
                polynom_dict[int(param[1])] = 1
            elif param[0].startswith('-x'):
                param = param[0].split('-x**')
                polynom_dict[int(param[1])] = -1
            else:
                polynom_dict[0] = int(param[0])

    return polynom_dict

def sum_polynom(dict1, dict2):
    max_degree = max(max(dict1), max(dict2))

    result_dict = {}
    for key in range(max_degree, -1, -1):
        result_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

    return result_dict

def write_to_file(polynom, file_name):
    data = open(file_name, 'w')
    data.write(polynom)
    data.close()

def read_from_file(file_name):
    data = open(file_name, 'r')

    polynom = data.read()

    # print(f'Read {polynom}')
    return polynom

polynom_koef1 = create_dict()
polynom_koef2 = create_dict()
print(polynom_koef1)
print(polynom_koef2)
polynom1 = write_polynom(polynom_koef1)
write_to_file(polynom1, 'polynom1.txt')
print(polynom1)
polynom2 = write_polynom(polynom_koef2)
write_to_file(polynom2, 'polynom2.txt')
print(polynom2)

read_polynom1 = read_from_file('polynom1.txt')
polinom_dict1 = parse_polynom(read_polynom1)

read_polynom2 = read_from_file('polynom2.txt')
polinom_dict2 = parse_polynom(read_polynom2)

result_polinom = sum_polynom(polinom_dict1, polinom_dict2)
result_polinom = write_polynom(result_polinom)
print(result_polinom)
write_to_file(result_polinom, 'result_polynom.txt')


