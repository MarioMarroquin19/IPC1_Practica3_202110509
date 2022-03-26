#MARIO MARROQUIN 202110509
import numpy as np
from numpy import *

def menuPrincipal():
    print("=====MENÚ INICIO=====")
    print("1.   Iniciar Juego")
    print("2.   Salir")
    print("=====================")
    opcion = int(input("Ingrese una opción:"))
    return opcion

Nombre ="Prueba"
def opciones(opcion1):

    if(opcion1 == 1):
        global Nombre
        Nombre = input("Ingresa tu nombre:")
        generarTablero()

    if(opcion1 == 2):
        print("Saliendo")    

def regresar():
    opciones(menuPrincipal())

def main():
    opciones(menuPrincipal())

Punteo =0

def usuario():
    print("---------------")
    print("USUARIO:", Nombre)
    print("PUNTEO:",Punteo)
    print("---------------")

matriz  = [[" ",chr(88)," ",chr(64),chr(88)," "],[chr(64)," ",chr(88)," "," ",chr(79)],
        [" ",chr(64)," ",chr(79)," ",chr(88)],[chr(88),chr(79)," "," "," ",chr(64)],[" "," ",chr(88)," "," ",chr(79)]]

pacman = 0   
fila = 0
columna =0 

def generarTablero():
    global matriz  
    global pacman
    global fila
    global columna
    usuario()
    fila=random.randint(0,5)
    columna=random.randint(0,6) 
    print("---------------")    
    for i in range(5):  
        print("|",end=' ')
        for j in range (6):
            if(pacman < 1):
                if(matriz[fila][columna] ==" "):  
                    matriz[fila][columna]=chr(60)
                    pacman+=1
                else:
                    fila=random.randint(0,5)
                    columna=random.randint(0,6) 

            print(matriz[i][j],end=' ')
            
        print("|",end='')   
        print(' ')
    print("---------------")
    impTablero()

mov=""
vida = 1
def movimientos():
    global mov
    mov =input("Ingrese movimiento:")
    global fila
    global columna
    global vida
    global Punteo

    if(mov == "W" or mov == "w"):
        a=fila-1
        if(a<=0):
            a=0
        if(matriz[a][columna] == chr(64) ):
            matriz[fila][columna]=" "
            fila -=1
            vida = 0
            if(fila <=0):
                fila = 0
            return mov
        if(matriz[a][columna] == chr(79) ):
            Punteo += 10
            matriz[fila][columna]=" "
            fila -=1
            if(fila <=0):
                fila = 0
            return mov
        if(matriz[a][columna] == " "):
            matriz[fila][columna]=" "
            fila -=1
            if(fila <=0):
                fila = 0
            return mov
        if(matriz[a][columna] == chr(88)):
            return mov
        
    if(mov == "S" or mov == "s"):
        a=fila+1
        if(a>=4):
            a=4
        if(matriz[a][columna] == chr(64) ):
            matriz[fila][columna]=" "
            fila +=1
            vida = 0
            if (fila >= 4):
                fila = 4
            return mov
        if(matriz[a][columna] == chr(79) ):
            Punteo += 10
            matriz[fila][columna]=" "
            fila +=1
            if (fila >= 4):
                fila = 4
            return mov
        if(matriz[a][columna] == " "):
            matriz[fila][columna]=" "
            fila +=1
            if (fila >= 4):
                fila = 4
            return mov
        if(matriz[a][columna] == chr(88)):
            return mov

    if(mov == "D" or mov == "d"):
        a = columna +1
        if(a >=5):
            a=5
        if(matriz[fila][a] == chr(64) ):
            matriz[fila][columna]=" "
            columna +=1
            vida = 0
            if(columna >= 5):
                columna =5
            return mov
        if(matriz[fila][a] == chr(79) ):
            Punteo += 10
            matriz[fila][columna]=" "
            columna +=1
            if(columna >= 5):
                columna =5
            return mov
        if(matriz[fila][a] == " "):
            matriz[fila][columna]=" "
            columna +=1
            if(columna >= 5):
                columna =5
            return mov
        if(matriz[fila][a] == chr(88)):
            return mov

    if(mov == "A" or mov == "a"):
        a=columna -1
        if(a<=0):
            a=0
        if(matriz[fila][a] == chr(64) ):
            matriz[fila][columna]=" "
            columna -=1
            vida = 0
            if(columna <= 0):
                columna =0
            return mov
        if(matriz[fila][a] == chr(79) ):
            Punteo += 10
            matriz[fila][columna]=" "
            columna -=1
            if(columna <= 0):
                columna =0
            return mov
        if(matriz[fila][a] == " "):
            matriz[fila][columna]=" "
            columna -=1
            if(columna <= 0):
                columna =0
            return mov
        if(matriz[fila][a] == chr(88)):
            return mov
            
    if (mov == "F" or mov == "f"):
        mov = "F"
        return mov

def impTablero():
    global mov
    global vida
    global Punteo
    global matriz
    global pacman
    global fila 
    global columna
    while(movimientos()!="F" ):
        usuario()
        print("---------------")    
        for i in range(5):  
            print("|",end=' ')
            for j in range (6):
                matriz[fila][columna]=chr(60)
                print(matriz[i][j],end=' ')
            
            print("|",end='')   
            print(' ')
        print("---------------")
        
        if(vida ==0 or Punteo == 40):
            break

    if(Punteo == 40):
        vida = 1
        matriz = [[" ",chr(88)," ",chr(64),chr(88)," "],[chr(64)," ",chr(88)," "," ",chr(79)],
        [" ",chr(64)," ",chr(79)," ",chr(88)],[chr(88),chr(79)," "," "," ",chr(64)],[" "," ",chr(88)," "," ",chr(79)]]
        pacman = 0   
        fila = 0
        columna =0
        Punteo =0 
        print("¡Felicidades! GANASTE!")

    if(vida == 0):
        vida = 1
        matriz = [[" ",chr(88)," ",chr(64),chr(88)," "],[chr(64)," ",chr(88)," "," ",chr(79)],
        [" ",chr(64)," ",chr(79)," ",chr(88)],[chr(88),chr(79)," "," "," ",chr(64)],[" "," ",chr(88)," "," ",chr(79)]]
        pacman = 0   
        fila = 0
        columna =0 
        Punteo =0
        print("HAS PERDIDO!")
        
    vida = 1
    matriz = [[" ",chr(88)," ",chr(64),chr(88)," "],[chr(64)," ",chr(88)," "," ",chr(79)],
    [" ",chr(64)," ",chr(79)," ",chr(88)],[chr(88),chr(79)," "," "," ",chr(64)],[" "," ",chr(88)," "," ",chr(79)]]
    pacman = 0   
    fila = 0
    columna =0 
    Punteo =0
    input("Preciona enter para volver al menú")
    main()

if __name__ == "__main__":
    main()
