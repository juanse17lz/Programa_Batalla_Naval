import random

def printear_matriz(matriz:list):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end= " ")
        print("")

def bool_aleatorio()->bool:
    numero = random.randint(0,1)
    if numero == 0:
        retorno = False
    else:
        retorno = True
    return retorno

def inicializar_matriz(filas:int,columnas:int,valor_inicial=0)->list:
    """Inicializa una matriz con la cantidad de filas y columas ingresadas. Por defecto los elmentos seran ceros pero se le puede pasar por parametro el valor de los elementos iniciales. 

    Args:
        filas (int): Cantidad de filas que tendra la matriz.
        columnas (int): Cantida de columnas que tendra la matriz.
        valor_inicial : Valor inicial que tendran los elementos de la matriz, por defecto en cero.

    Returns:
        list: Retorna la matriz inicializada.
    """
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def colocar_barco(matriz:list,barco:list):
    pos = bool_aleatorio()
    posicion_valida = False
    while posicion_valida == False:
        fila = random.randint(0,len(matriz)-1)
        columna = random.randint(0,len(matriz[0])-1)
        for i in range(len(barco)):
            if pos:
                if columna + i >= len(matriz[0]) or matriz[fila][columna + i] == 1:
                    break
                elif matriz[fila][columna + i] == 0 and i == len(barco)-1:
                    posicion_valida = True
            else:
                if fila + i >= len(matriz) or matriz[fila + i][columna] == 1:
                    break
                elif matriz[fila + i][columna] == 0 and i == len(barco)-1:
                    posicion_valida = True
    if posicion_valida:
        for i in range(len(barco)):
            if pos:
                matriz[fila][columna + i] = 1
            else:
                matriz[fila + i][columna] = 1

def colocacion_barcos(matriz:list,barco:list):
    for i in range(len(barco)):
        if len(barco) == 1:
            for c in range(4):
                colocar_barco(matriz,barco)
        elif len(barco) == 2:
            for c in range(3):
                colocar_barco(matriz,barco)
        elif len(barco) == 3:
            for c in range(2):
                colocar_barco(matriz,barco)
        elif len(barco) == 4:
            colocar_barco(matriz,barco)

def tablero_juego(dificultad:str="F"):
    filas = 10
    columnas = 10
    repeticiones = 1
    if dificultad == "M":
        filas *= 2
        columnas *= 2
        repeticiones *= 2
    elif dificultad == "D":
        filas *= 4
        columnas *= 4
        repeticiones *= 3
    else:
        pass

    submarino = [1]
    destructore = [1,1]
    crucero = [1,1,1]
    acorazado =[1,1,1,1]
    barcos = [submarino,destructore,crucero,acorazado]

    tablero = inicializar_matriz(filas,columnas)

    for r in range(repeticiones):
        for barco in barcos:
            colocacion_barcos(tablero,barco)

    return tablero
        

