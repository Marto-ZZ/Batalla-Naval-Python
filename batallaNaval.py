from typing import Any
from biblioteca import *

## Ejercicio 1

def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ 
    Indica la cantidad de barcos de un tamaño específico en la lista de barcos.
    PRE: Los barcos son válidos (sonBarcosVálidos(barcos) es True).
    Args:
        barcos (list[BarcoEnGrilla]): Lista de barcos, donde cada barco es una lista de posiciones.
        tamaño (int): El tamaño de barco a contar.
    Returns:
        int: La cantidad de barcos en 'barcos' que tienen exactamente 'tamaño' posiciones.
    """

    cantidad: int = 0

    for barco in barcos:
        if len(barco) == tamaño:
            cantidad += 1

    return cantidad

## Ejercicio 2

def nuevoJuego(cantidadDeFilas: int, cantidadDeColumnas: int, barcosDisponibles: list[Barco]) -> EstadoJuego:
    """
    Inicializa un nuevo juego con las dimensiones y barcos dados.

    PRE:
        - cantidadDeFilas entre 1 y 26.
        - cantidadDeColumnas mayor a 0.
        - barcosDisponibles no vacío.

    Args:
        cantidadDeFilas (int): Número de filas.
        cantidadDeColumnas (int): Número de columnas.
        barcosDisponibles (list[Barco]): Lista de tamaños de barcos disponibles.

    Returns:
        EstadoJuego: Estado inicial del juego.
    """
    return((cantidadDeFilas,cantidadDeColumnas), barcosDisponibles, [UNO], nuevoTablero(cantidadDeFilas, cantidadDeColumnas), nuevoTablero(cantidadDeFilas, cantidadDeColumnas))

#2A
def grillaVacía(cantidadDeFilas: int, cantidadDeColumnas: int) -> Grilla:
    """
    Crea una grilla vacía con las dimensiones dadas.
    """

    res: Grilla = [] 
    
    for i in range(cantidadDeFilas):
        filaVacia: list[Celda] = []

        for j in range(cantidadDeColumnas):
            filaVacia.append(VACÍO)
        res.append(filaVacia)

    return res 

#2B
def nuevoTablero(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:
    """
    Crea un nuevo tablero con grillas local y del oponente vacías.
    """
    grillaLocal = grillaVacía(cantidadDeFilas, cantidadDeColumnas)
    grillaOponente = grillaVacía(cantidadDeFilas, cantidadDeColumnas)
    tablero: Tablero = (grillaLocal, grillaOponente)

    return tablero

#2C
def esGrillaVacía(grilla: Grilla) -> bool:
    """
    Indica si todas las celdas de la grilla son VACÍO.
    """

    for fila in grilla:
        for posicion in fila:
            if not posicion == VACÍO:
                return False

    return True 

## Ejercicio 3

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """
    Indica si el estado de juego es válido.
    """
    if cantidadDeFilasEstadoJuego(estadoDeJuego) < 1 or cantidadDeFilasEstadoJuego(estadoDeJuego) > 26:
        return False

    if cantidadDeColumnasEstadoJuego(estadoDeJuego) < 1:
        return False
    
    if not len(estadoDeJuego[2]) == 1:
        return False

    if len(barcosDisponibles(estadoDeJuego)) < 1:
        return False

    if (not tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego)) or (not tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego)):
        return False

    if not coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego, UNO), tableroDeJugador(estadoDeJuego, DOS)):
        return False

    return True

#3A
def tableroVálidoEnJuego(tablero: Tablero, estadoDeJuego: EstadoJuego) -> bool:
    """
    Verifica si un tablero es válido dentro del contexto de un estado de juego.
    """
    grillaLocalValida: bool = grillaVálidaEnJuego(tablero[0], estadoDeJuego)
    grillaOponenteValida: bool = grillaVálidaEnJuego(tablero[1], estadoDeJuego)
    coincidenBarcos: bool = coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), tablero[0])

    return grillaLocalValida and grillaOponenteValida and coincidenBarcos

#3B
def coincidenBarcosEnGrilla(barcos: list[Barco], grilla: Grilla) -> bool:
    """
    Verifica si los barcos en una grilla coinciden con los barcos disponibles.
    """
    return mismosElementos(barcos, tamaños(barcosEnGrilla(grilla)))

#3C
def tamaños(barcos: list[BarcoEnGrilla]) -> list[int]:
    """
    Obtiene la lista de tamaños de una lista de barcos.
    """
    res: list[int] = []
    for barco in barcos:
        res.append(len(barco))

    return res

#3D
def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:
    """
    Determina si dos listas contienen los mismos elementos con las mismas frecuencias.
    """
    if len(lista1) != len(lista2):
        return False

    lista_completa = lista1 + lista2
    
    for elemento in lista1:
        if cantidadDeApariciones(elemento, lista1) != cantidadDeApariciones(elemento, lista2):
            return False
        
    for elemento in lista2:
        if not cantidadDeApariciones(elemento, lista1) == cantidadDeApariciones(elemento, lista2):
            return False

    return True

#3E
def coincidenPosicionesAtacadas(tablero: Tablero, tableroOponente: Tablero) -> bool:
    """
    Verifica la consistencia de las posiciones atacadas entre dos tableros.
    """
    n1: int = 0
    n2: int = 0
    
    #1 Chequea tablero[1] (oponente J1) vs tableroOponente[0] (local J2)
    i: int = 0
    for fila in tablero[1]: 
        j: int = 0
        for posicion in fila:
            if not posicion == VACÍO:
                n1 += 1
                if not tableroOponente[0][i][j] == posicion:
                    return False
            j += 1
        i += 1

    #2 Chequea tableroOponente[1] (oponente J2) vs tablero[0] (local J1)
    i = 0
    for fila in tableroOponente[1]: 
        j = 0
        for posicion in fila:
            if not posicion == VACÍO:
                n2 += 1 
                if not tablero[0][i][j] == posicion:
                    return False
            j += 1
        i += 1
    
    return (n1 == n2) or (n1 == n2 + 1)


## Ejercicio 4

def dispararEnPosición(estadoDeJuego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """
    Realiza un disparo en la posición especificada y actualiza el estado del juego.
    """
    resultado: ResultadoDisparo = NADA

    turnoActual = estadoDeJuego[2][0]
    turnoOpuesto = DOS if turnoActual == UNO else UNO
    
    grillaOponenteAtacante = tableroDeJugador(estadoDeJuego, turnoActual)[1]
    grillaLocalAtacado = tableroDeJugador(estadoDeJuego, turnoOpuesto)[0]
   
    celdaAtacadaEnLocalAtacado: Celda = celdaEnPosición(grillaLocalAtacado, posición) 
    
    if celdaAtacadaEnLocalAtacado == BARCO:
        resultado = TOCADO
        cambiarCeldaGrilla(grillaOponenteAtacante, posición, BARCO) 
    else: 
        cambiarCeldaGrilla(grillaOponenteAtacante, posición, AGUA)
        cambiarCeldaGrilla(grillaLocalAtacado, posición, AGUA)

    cambiarTurno(estadoDeJuego)

    return resultado

## Ejercicio 5

def _encontrarBarcoCompleto(pos: Posición, posicionesConBarcos: list[Posición]) -> BarcoEnGrilla:
    """
    Encuentra todas las posiciones conectadas a 'pos' de forma horizontal o vertical.
    """
    letra = letraDePosición(pos)
    numero = númeroDePosición(pos)
    
    # 1. Búsqueda Horizontal
    barco_horizontal: list[Posición] = [pos]
    n = numero + 1
    while pertenecePosición((letra, n), posicionesConBarcos) and (letra, n) not in barco_horizontal:
        barco_horizontal.append((letra, n))
        n += 1
        
    n = numero - 1
    while pertenecePosición((letra, n), posicionesConBarcos) and (letra, n) not in barco_horizontal:
        barco_horizontal.append((letra, n))
        n -= 1
    
    # 2. Búsqueda Vertical
    barco_vertical: list[Posición] = [pos]
    
    def intentar_mover(start_l: str, direction_fn) -> list[Posición]:
        current_l = start_l
        temp_barco = []
        while True:
            try:
                current_l = direction_fn(current_l)
                nueva_pos = (current_l, numero)
                if pertenecePosición(nueva_pos, posicionesConBarcos) and nueva_pos not in temp_barco:
                    temp_barco.append(nueva_pos)
                else:
                    break
            except:
                break
        return temp_barco

    barco_vertical.extend(intentar_mover(letra, siguienteLetra))
    barco_vertical.extend(intentar_mover(letra, anteriorLetra))
    
    # Determinar el barco final 
    if len(barco_horizontal) > 1 and len(barco_vertical) > 1:
        if len(barco_horizontal) >= len(barco_vertical):
            return posicionesOrdenadas(barco_horizontal)
        else:
            return posicionesOrdenadas(barco_vertical)

    if len(barco_horizontal) > 1:
        return posicionesOrdenadas(barco_horizontal)
    elif len(barco_vertical) > 1:
        return posicionesOrdenadas(barco_vertical)
    else:
        return [pos]

def ordenarBarcos(posicionesConBarcos: list[Posición]) -> list[BarcoEnGrilla]:
    """
    Dada una lista de posiciones cuyas celdas contienen BARCO, devuelve una lista con barcos armados
    """
    
    barcosOrdenados: list[BarcoEnGrilla] = []
    yaVistos: list[Posición] = []
    
    posicionesConBarcos = sorted(posicionesConBarcos, key=lambda p: (ord(p[0]), p[1]))

    for pos in posicionesConBarcos:
        if not pertenecePosición(pos, yaVistos):
            barcoNuevo = _encontrarBarcoCompleto(pos, posicionesConBarcos)
            barcosOrdenados.append(barcoNuevo)
            for p in barcoNuevo:
                yaVistos.append(p)
                
    return barcosOrdenados

def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """
    Identifica y devuelve todos los barcos presentes en una grilla.
    """
    posicionesConBarcos: list[Posición] = [] # Se corrigió el nombre de la variable (plural)
    columnas: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    # 1. Obtener todas las posiciones que contienen BARCO
    for i in range(len(grilla)):
        for j in range(len(grilla[0])):
            posicion = (columnas[i], j+1)
            if celdaEnPosición(grilla, posicion) == BARCO:
                posicionesConBarcos.append(posicion) # Se corrigió el nombre de la variable (plural)

    # 2. Agrupar las posiciones en barcos
    return ordenarBarcos(posicionesConBarcos)

#5A
def noHayMásDeUnaFormaDeConstruirUnBarcoDesde(grilla: Grilla, posición: Posición) -> bool:
    """
    Determina si desde una posición dada solo hay una forma posible de construir un barco.
    """
    hayH = sePuedeConstruirBarcoHorizontalDesde(grilla, posición)
    hayV = sePuedeConstruirBarcoVerticalDesde(grilla, posición)
    return not (hayH and hayV)

#5B
def sePuedeConstruirBarcoHorizontalDesde(grilla: Grilla, posición: Posición) -> bool:
    """
    Verifica si se puede construir un barco horizontalmente desde la posición dada.
    """
    
    hayBarcoEnPosición: bool = celdaEnPosición(grilla, posición) == BARCO
    hayBarcoALaDerecha: bool = hayBarcoAl(grilla, posición, DERECHA)
    hayBarcoALaIzquierda: bool = hayBarcoAl(grilla, posición, IZQUIERDA)

    return hayBarcoEnPosición and (hayBarcoALaDerecha or hayBarcoALaIzquierda)

#5C
def sePuedeConstruirBarcoVerticalDesde(grilla: Grilla, posición: Posición) -> bool:
    """
    Verifica si se puede construir un barco verticalmente desde la posición dada.
    """
    
    hayBarcoEnPosición: bool = celdaEnPosición(grilla, posición) == BARCO
    hayBarcoArriba: bool = hayBarcoAl(grilla, posición, ARRIBA)
    hayBarcoAbajo: bool = hayBarcoAl(grilla, posición, ABAJO)

    return hayBarcoEnPosición and (hayBarcoArriba or hayBarcoAbajo)

#5D
def posicionesOcupadasEnGrilla(grilla: Grilla, posiciones: list[Posición]) -> bool:
    """
    Verifica si todas las posiciones dadas están ocupadas por barcos en la grilla.
    """
    
    for pos in posiciones:
        if not celdaEnPosición(grilla, pos) == BARCO:
            return False 
    
    return True

#5E
def algúnBarcoOcupaLaPosición(barcos: list[BarcoEnGrilla], posición: Posición) -> bool:
    """
    Determina si algún barco de la lista ocupa la posición especificada.
    """
    
    for barco in barcos:
        if pertenecePosición(posición, barco):
            return True
    return False