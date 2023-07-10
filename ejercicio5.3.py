"""
    Manejo de contraseñas:
        a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario
        la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
        b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
        c) Modificar el programa anterior para que después de cada intento agregue una pausa
        cada vez mayor, utilizando la función sleep del módulo time.
        d) Modificar el programa anterior para que sea una función que devuelva si el usuario
        ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).
"""

from time import sleep


def contrasenia(password):

    valido = False

    while not valido:
        contrasenia = input("Ingrese la contraseña:")

        if contrasenia == password:
            valido=True
            print("Contraseña correcta. Puede seguir con el programa.")
        else:
            print("Contraseña incorrecta. Vuelva a ingresar.")

# contrasenia("contrasenia") 

def contrasenia_con_intentos(password):

    valido = False
    intentos = 3

    while not valido and intentos!=0:
        contrasenia=input(f"Ingrese la contraseña(intentos: {intentos}):")

        if contrasenia == password:
            valido=True
            print("Contraseña correcta. Puede seguir con el programa.")
        else:
            intentos-=1
            print("Contraseña incorrecta.")

    if intentos == 0:
        print("Se acabaron los intentos.")

# contrasenia_con_intentos("contrasenia")

def contrasenia_con_intentos_sleep(password):

    valido = False
    intentos = 3
    retraso = 0

    while not valido and intentos!=0:
        contrasenia = input(f"Ingrese la contraseña(intentos: {intentos}):")

        if contrasenia == password:
            valido=True
            print("Contraseña correcta. Puede seguir con el programa.")
        else:
            intentos-=1
            retraso+=1
            print("Contraseña incorrecta.")
            sleep(retraso)

    if intentos == 0:
        print("Se acabaron los intentos.")

# contrasenia_con_intentos_sleep('contrasenia')


def contrasenia_con_intentos_sleep_boolean(password):
    valido = False
    intentos = 3
    retraso = 0

    while not valido and intentos!=0:
        contrasenia = input(f"Ingrese la contraseña(intentos: {intentos}):")

        if contrasenia == password:
            valido = True
            return valido
        else:
            intentos-=1
            retraso+=1
            sleep(retraso)
    
    return valido

# contrasenia_con_intentos_sleep_boolean('contrasenia')
