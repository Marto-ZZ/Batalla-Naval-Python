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

    PRE:
        - cantidadDeFilas entre 1 y 26.
        - cantidadDeColumnas mayor a 0.

    Args:
        cantidadDeFilas (int): Número de filas.
        cantidadDeColumnas (int): Número de columnas.

    Returns:
        Grilla: Una grilla de cantidadDeFilas x cantidadDeColumnas con todas las celdas VACÍO.
    """

    res: Celda = []
    filaVacia: Celda = []
    
    for i in range(cantidadDeColumnas):
        filaVacia.append(VACÍO)

    for j in range(cantidadDeFilas):
        res.append(filaVacia)

    return res 

#2B
def nuevoTablero(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:
    """
    Crea un nuevo tablero con grillas local y del oponente vacías.

    PRE:
        cantidadDeFilas entre 1 y 26, cantidadDeColumnas mayor a 0.

    Args:
        cantidadDeFilas (int): Número de filas.
        cantidadDeColumnas (int): Número de columnas.

    Returns:
        Tablero: Tablero con dos grillas vacías.
    """
    grillaVacia = grillaVacía(cantidadDeFilas, cantidadDeColumnas)
    tablero: tuple = (grillaVacia,grillaVacia)

    return tablero

#2C
def esGrillaVacía(grilla: Grilla) -> bool:
    """
    Indica si todas las celdas de la grilla son VACÍO.

    PRE: La grilla es válida.

    Args:
        grilla (Grilla): Grilla a verificar.

    Returns:
        bool: True si todas las celdas son VACÍO, False en caso contrario.
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

    PRE: True

    Args:
        estadoDeJuego (EstadoJuego): Estado de juego a validar.

    Returns:
        bool: True si el estado es válido, False en caso contrario.
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
    
    PRE: True

    Args:
        tablero (Tablero): Tablero a validar.
        estadoDeJuego (EstadoJuego): Estado de juego de referencia.
        
    Returns:
        bool: True si el tablero es válido, False en caso contrario.
    """
    grillaLocalValida: bool = grillaVálidaEnJuego(grillaLocal(tablero), estadoDeJuego)
    grillaOponenteValida: bool = grillaVálidaEnJuego(grillaOponente(tablero), estadoDeJuego)
    coincidenBarcos: bool = coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), grillaLocal(tablero))

    return grillaLocalValida and grillaOponenteValida and coincidenBarcos

#3B
def coincidenBarcosEnGrilla(barcos: list[Barco], grilla: Grilla) -> bool:
    """
    Verifica si los barcos en una grilla coinciden con los barcos disponibles.
    
    PRE: La grilla es válida.

    Args:
        barcos (list[Barco]): Lista de barcos disponibles
        grilla (Grilla): Grilla a verificar
        
    Returns:
        bool: True si los barcos en la grilla coinciden con los disponibles
    """
    return mismosElementos(barcos, tamaños(barcosEnGrilla(grilla)))

#3C
def tamaños(barcos: list[BarcoEnGrilla]) -> list[int]:
    """
    Obtiene la lista de tamaños de una lista de barcos.
    
    PRE: Los barcos son válidos.
    Args:
        barcos (list[BarcoEnGrilla]): Lista de barcos.
        
    Returns:
        list[int]: Lista de tamaños de los barcos.
    """
    res: list[int] = []
    for barco in barcos:
        res.append(len(barco))

    return res

#3D
def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:
    """
    Determina si dos listas contienen los mismos elementos con las mismas frecuencias.
    
    PRE: True
    Args:
        lista1 (list): Primera lista a comparar.
        lista2 (list): Segunda lista a comparar.
        
    Returns:
        bool: True si las listas tienen los mismos elementos con las mismas frecuencias.
    """
    if (len(lista1) == 0 and not len(lista2) == 0) or (len(lista2) == 0 and not len(lista1) == 0):
        return False

    for elemento in lista1:
        if not cantidadDeApariciones(elemento, lista1) == cantidadDeApariciones(elemento, lista2):
            return False
        
    for elemento in lista2:
        if not cantidadDeApariciones(elemento, lista1) == cantidadDeApariciones(elemento, lista2):
            return False

    return True

#3E
def coincidenPosicionesAtacadas(tablero: Tablero, tableroOponente: Tablero) -> bool:
    """
    Verifica la consistencia de las posiciones atacadas entre dos tableros.
    
    Las posiciones atacadas son consistentes si:
    - Las celdas no vacías en la grilla del oponente de tablero1 coinciden con las de tablero2.
    - Las celdas no vacías en la grilla del oponente de tablero2 coinciden con las de tablero1.
    - La diferencia en cantidad de celdas no vacías es 0 o 1.
    
    PRE: True

    Args:
        tablero1 (Tablero): Primer tablero.
        tablero2 (Tablero): Segundo tablero.
        
    Returns:
        bool: True si las posiciones atacadas son consistentes
    """
    n1: int = 0
    n2: int = 0
    i: int = 0
    j: int = 0
    
    for fila in tablero[1]:
        for posicion in fila:
            if not posicion == VACÍO:
                n1+=1
                if not tableroOponente[0][i][j] == posicion:
                    return False
            j+=1
        i+=1

    j = 0
    i = 0

    for fila in tableroOponente[1]:
        for posicion in fila:
            if not posicion == VACÍO:
                n1+=1
                if not tablero[0][i][j] == posicion:
                    return False
            j+=1
        i+=1

    
    return (n1-n2 >= 0 and n1-n2 <= 1)


## Ejercicio 4

def dispararEnPosición(estadoDeJuego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """
    Realiza un disparo en la posición especificada y actualiza el estado del juego.
    El jugador actual dispara a la posición indicada en el tablero del oponente.
    Si impacta un barco, marca la posición como TOCADO, de lo contrario como AGUA.
    Luego cambia el turno al siguiente jugador.
    
    PRE:
        - El estado de juego es válido.
        - La posición es válida en la grilla del oponente del jugador actual.
        - La posición no ha sido atacada previamente (está VACÍA en la grilla del oponente).
    
    Args:
        estadoDeJuego (EstadoJuego): Estado actual del juego.
        posición (Posición): Posición a disparar (letra, número).
        
    Returns:
        ResultadoDisparo: NADA si no impactó un barco, TOCADO si impactó un barco.
        
    Modifica:
        estadoDeJuego: Actualiza las grillas y cambia el turno
    """
    resultado: ResultadoDisparo = NADA

    turnoActual = turno(estadoDeJuego)
    turnoOpuesto = None
    if turnoActual == UNO:
        turnoOpuesto = DOS
    else:
        turnoOpuesto = UNO

    grillaLocal = tableroDeJugador(estadoDeJuego, turnoActual)[1]
    grillaOponente = tableroDeJugador(estadoDeJuego, turnoOpuesto)[0]
   
    celdaAtacadaOponente: Celda = celdaEnPosición(grillaOponente, posición) #celda atacada en jugador 2
    celdaAtacadaLocal: Celda = celdaEnPosición(grillaLocal, posición) #celda atacada en jugador 1
    
    if celdaAtacadaOponente == BARCO:
        resultado = TOCADO
        cambiarCeldaGrilla(grillaLocal, posición, BARCO)
        cambiarCeldaGrilla(grillaOponente, posición, AGUA)

    else:
        cambiarCeldaGrilla(grillaLocal, posición, AGUA)
        cambiarCeldaGrilla(grillaOponente, posición, AGUA)


    cambiarTurno(estadoDeJuego)

    return resultado

## Ejercicio 5

#AUX PERSONALIZADA
def ordenarBarcos(posicionesConBarcos: list[Posición]) -> list[BarcoEnGrilla]:
    """
    Dada una lista de posiciones cuyas celdas contienen BARCO, devuelve una lista con barcos armados
    
    PRE:
        - Todas las posiciones de posicionesConBarcos referencian celdas con el valor BARCO
        
    Args:
        posicionesConBarcos (list[Posición]): Lista de posiciones a ordenar.
        
    Returns:
        list[BarcoEnGrilla]: Lista con los barcos armados.
    """
    
    barcosOrdenados: list[BarcoEnGrilla] = []
    barcoTemp: BarcoEnGrilla = []
    yaVistos: list[Posición] = []

    i = 0

    while i < len(posicionesConBarcos):
        pos = posicionesConBarcos[i]
        if (pos in yaVistos):
            i+=1
            continue
        if len(barcoTemp) == 0:
            barcoTemp.append(pos)
            yaVistos.append(pos)
            
        j = 1
        while j < len(posicionesConBarcos):
            pos2 = posicionesConBarcos[j]
            if ((pos2[0] == pos[0] and pos2[1] == (pos[1]+1)) or (ord(pos2[0]) == ord(pos[0])+1 and pos2[1] == pos[1])) and (pos2 not in yaVistos):
                barcoTemp.append(posicionesConBarcos[j])
                yaVistos.append(pos2)
            j+=1
            
        barcosOrdenados.append(barcoTemp)
        barcoTemp = []
        i+=1

    return barcosOrdenados

def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """
    Identifica y devuelve todos los barcos presentes en una grilla.
    
    Recorre la grilla buscando posiciones con BARCO y agrupa las posiciones
    consecutivas (horizontal o verticalmente) que forman cada barco.
    
    PRE:
        - La grilla es válida.
        - Hay una única forma de construir barcos desde cada posición.
        
    Args:
        grilla (Grilla): Grilla a analizar.
        
    Returns:
        list[BarcoEnGrilla]: Lista de barcos encontrados en la grilla,
        donde cada barco es una lista de posiciones consecutivas.
    """
    posicionesConBarco: list[Posición] = []
    columnas: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    for i in range(len(grilla)):
        for j in range(len(grilla[0])):
            if grilla[i][j] == BARCO:
                posicion = (columnas[i], j+1)
                posicionesConBarco.append(posicion)

    return ordenarBarcos(posicionesConBarco)

#5A
def noHayMásDeUnaFormaDeConstruirUnBarcoDesde(grilla: Grilla, posición: Posición) -> bool:
    """
    Determina si desde una posición dada solo hay una forma posible de construir un barco.
    
    PRE:
        - La grilla es válida.
        - La posición pertenece a la grilla.
        
    Args:
        grilla (Grilla): Grilla a analizar.
        posición (Posición): Posición desde la cual verificar.
        
    Returns:
        bool: True si no hay ambigüedad en la construcción del barco,
        False si se puede construir tanto horizontal como verticalmente.
    """
    return (not sePuedeConstruirBarcoHorizontalDesde(grilla, posición) or not sePuedeConstruirBarcoVerticalDesde(grilla, posición))

#5B
def sePuedeConstruirBarcoHorizontalDesde(grilla: Grilla, posición: Posición) -> bool:
    """
    Verifica si se puede construir un barco horizontalmente desde la posición dada.
    
    PRE:
        - La grilla es válida.
        - La posición pertenece a la grilla.
        
    Args:
        grilla (Grilla): Grilla a analizar.
        posición (Posición): Posición desde la cual verificar.
        
    Returns:
        bool: True si hay un barco en la posición y tiene barcos adyacentes
        horizontalmente (izquierda o derecha).
    """
    
    hayBarcoEnPosición: bool = celdaEnPosición(grilla, posición) == BARCO
    hayBarcoALaDerecha: bool = hayBarcoAl(grilla, posición, DERECHA)
    hayBarcoALaIzquierda: bool = hayBarcoAl(grilla, posición, IZQUIERDA)

    return hayBarcoEnPosición and (hayBarcoALaDerecha or hayBarcoALaIzquierda)

#5C
def sePuedeConstruirBarcoVerticalDesde(grilla: Grilla, posición: Posición) -> bool:
    """
    Verifica si se puede construir un barco verticalmente desde la posición dada.
    
    PRE:
        - La grilla es válida.
        - La posición pertenece a la grilla.
        
    Args:
        grilla (Grilla): Grilla a analizar.
        posición (Posición): Posición desde la cual verificar.
        
    Returns:
        bool: True si hay un barco en la posición y tiene barcos adyacentes
        verticalmente (arriba o abajo).
    """
    
    hayBarcoEnPosición: bool = celdaEnPosición(grilla, posición) == BARCO
    hayBarcoArriba: bool = hayBarcoAl(grilla, posición, ARRIBA)
    hayBarcoAbajo: bool = hayBarcoAl(grilla, posición, ABAJO)

    return hayBarcoEnPosición and (hayBarcoArriba or hayBarcoAbajo)

#5D
def posicionesOcupadasEnGrilla(grilla: Grilla, posiciones: list[Posición]) -> bool:
    """
    Verifica si todas las posiciones dadas están ocupadas por barcos en la grilla.
    
    PRE:
        - La grilla es válida.
        - Todas las posiciones son válidas en la grilla.
        
    Args:
        grilla (Grilla): Grilla a verificar.
        posiciones (list[Posición]): Lista de posiciones a comprobar.
        
    Returns:
        bool: True si todas las posiciones contienen BARCO en la grilla.
    """
    
    for pos in posiciones:
        if not celdaEnPosición(grilla, pos) == BARCO:
            return False 
    
    return True

#5E
def algúnBarcoOcupaLaPosición(barcos: list[BarcoEnGrilla], posición: Posición) -> bool:
    """
    Determina si algún barco de la lista ocupa la posición especificada.
    
    PRE:
        - Todos los barcos en la lista son válidos.
        
    Args:
        barcos (list[BarcoEnGrilla]): Lista de barcos a verificar.
        posición (Posición): Posición a buscar.
        
    Returns:
        bool: True si la posición está contenida en algún barco de la lista.
    """
    
    res = False
    i = 0

    while (not res and i < len(barcos)):
        #barcos[i] siempre cumple barcos[i] in barcos
        if posición in barcos[i]:
            res = True
        i+=1

    return res