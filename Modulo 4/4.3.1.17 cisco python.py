from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

inputx = ''
dic = {}
name = ''
nm_fl = input("Ingresa el nombre del archivo de datos del estudiante: ")

try:
    src = open(nm_fl, "rt")
    inputx = src.readlines()    
    src.close()
    if len(inputx) == 0:
        raise FileEmpty("Error: El archivo que seleccionó está vacío")
    for x in range(len(inputx)):
        temp = inputx[x].split()
        if len(temp) != 3:
            raise BadLine("Error: línea incorrecta en el archivo de entrada en línea: " + str(x + 1))
        name = temp[0] + ' ' + temp[1]
        if name not in dic:
            dic[name] = float(temp[2])
        else:
            dic[name] += float(temp[2])
except FileEmpty as fe:
    print(fe)
    exit(1)
except BadLine as bl:
    print(bl)
    exit(2)
except IOError as e:
    print("No se puede abrir el archivo fuente: ", strerror(e.errno))
    exit(e.errno)

print('\n')
for key in sorted(dic.keys()):
    print(key, dic[key])
