from tabulate import tabulate 

agenda = {}
identificador = 1

while True:
    datos = []
    print           ('Clave Id: ',identificador)
    apellido = input('Apellido: ').title()
    nombre   = input('Nombre : ').title()
    while True:
        try:
            edad = int(input('Edad:   '))
            break
        except ValueError:
            print('La edad es un numero.... verifique')
    telefono = input('Telefono: ')


    datos.append(identificador)
    datos.append(apellido)
    datos.append(nombre)
    datos.append(edad)
    datos.append(telefono)

    agenda[identificador] = datos
    print()
    sigo = input('Sigue agregando datos a la agenda? (s/n): ').lower()
    if sigo != 's':
        break
    else:
        identificador += 1 
'''
for id, dato in agenda.items():
    print('Clave: ', id)
    print('Apellido:', dato[1])
    print('Nombre:', dato[2])
    print('Edad:', dato[3])
    print('Telefono:', dato[4])
    print('------------------')
'''
print(tabulate(agenda.values(), headers=['id','Apellido','Nombre','Edad','Telefono'], tablefmt='fancy_grid', numalign='center'))

