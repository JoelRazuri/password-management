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

def contraseña(password):

    valido=False

    while valido==False:
        contraseña=input("Ingrese la contraseña:")

        if contraseña==password:
            valido=True
            print("Contraseña correcta. Puede seguir con el programa.")
        else:
            print("Contraseña incorrecta. Vuelva a ingresar.")

# contraseña("joel") 

def contraseña_con_intentos(password):

    valido=False
    intentos=3

    while valido==False and intentos!=0:
        contraseña=input(f"Ingrese la contraseña(intentos: {intentos}):")

        if contraseña==password:
            valido=True
            print("Contraseña correcta. Puede seguir con el programa.")
        else:
            intentos-=1
            print("Contraseña incorrecta.")
            if intentos==0:
                print("Se acabaron los intentos.")

# contraseña_con_intentos("joel1234")

