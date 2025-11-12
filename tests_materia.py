import unittest
from batallaNaval import *
from biblioteca import *

# Tests
# Tests Ejercicio 1
class cantidadDeBarcosDeTamaño_Test(unittest.TestCase):
    def test_longitud_2_hay_uno_en_el_medio(self): # Un ejemplo de test 
        barcos = [[('H',3), ('H',4), ('H',5)],
                  [('F',4), ('E',4)],
                  [('B',4), ('B',3), ('B',2)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),1)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                  [('F',4), ('E',4)],
                                  [('B',4), ('B',3), ('B',2)]] )

    def test_lista_vacía(self): # Caso borde: lista vacía
        barcos = []       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,3),0)
        self.assertEqual(barcos, [] )

    def test_sin_barcos_de_ese_tamaño(self): # Caso borde: sin barcos de ese tamaño
        barcos = [[('A',1), ('A',2)],
                  [('C',3), ('D',3), ('E',3)],
                  [('F',4), ('F',5), ('F',6), ('F',7)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,5),0)
        self.assertEqual(barcos, [[('A',1), ('A',2)],
                                  [('C',3), ('D',3), ('E',3)],
                                  [('F',4), ('F',5), ('F',6), ('F',7)]] )
        
    def test_varios_barcos_de_ese_tamaño(self): # Caso general: varios barcos de ese tamaño
        barcos = [[('A',1), ('A',2)],
                  [('C',3), ('D',3), ('E',3)],
                  [('F',4), ('F',5), ('F',6), ('F',7)],
                  [('H',1), ('H',2)],
                  [('J',5), ('J',6)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),3)
        self.assertEqual(barcos, [[('A',1), ('A',2)],
                                  [('C',3), ('D',3), ('E',3)],
                                  [('F',4), ('F',5), ('F',6), ('F',7)],
                                  [('H',1), ('H',2)],
                                  [('J',5), ('J',6)]] )
        
    def test_todos_los_barcos_son_de_ese_tamaño(self): # Caso borde: todos los barcos son de ese tamaño
        barcos = [[('A',1), ('A',2)],
                  [('C',3), ('D',3)],
                  [('F',4), ('F',5)],
                  [('H',1), ('H',2)],
                  [('J',5), ('J',6)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),5)
        self.assertEqual(barcos, [[('A',1), ('A',2)],
                                  [('C',3), ('D',3)],
                                  [('F',4), ('F',5)],
                                  [('H',1), ('H',2)],
                                  [('J',5), ('J',6)]] )
        
    def test_tamaño_cero(self): # Caso borde: tamaño cero
        barcos = [[('A',1)],
                  [('C',3), ('D',3), ('E',3)],
                  [('F',4), ('F',5), ('F',6), ('F',7)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,0),0)
        self.assertEqual(barcos, [[('A',1)],
                                  [('C',3), ('D',3), ('E',3)],
                                  [('F',4), ('F',5), ('F',6), ('F',7)]] )
        
    def test_tamaño_negativo(self): # Caso borde: tamaño negativo
        barcos = [[('A',1)],
                  [('C',3), ('D',3), ('E',3)],
                  [('F',4), ('F',5), ('F',6), ('F',7)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,-3),0)
        self.assertEqual(barcos, [[('A',1)],
                                  [('C',3), ('D',3), ('E',3)],
                                  [('F',4), ('F',5), ('F',6), ('F',7)]] )
        
    def test_tamaño_uno(self): # Caso borde: tamaño uno
        barcos = [[('A',1)],
                  [('C',3), ('D',3), ('E',3)],
                  [('F',4), ('F',5), ('F',6), ('F',7)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,1),1)
        self.assertEqual(barcos, [[('A',1)],
                                  [('C',3), ('D',3), ('E',3)],
                                  [('F',4), ('F',5), ('F',6), ('F',7)]] )
        
# Tests Ejercicio 2
class nuevoJuego_Test(unittest.TestCase):
    def test_2x2_y_un_barco_longitud_2(self): #
        grilla_vacia_2x2: Grilla = [[VACÍO, VACÍO],
                                   [VACÍO, VACÍO]]
        
        juego = nuevoJuego(2,2,[2])
        
        # Asegura que las 4 grillas sean estructuralmente iguales a la vacía 2x2
        self.assertEqual(juego[0], (2,2))
        self.assertEqual(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        
        self.assertEqual(juego[3][0], grilla_vacia_2x2) # Grilla local J1
        self.assertEqual(juego[3][1], grilla_vacia_2x2) # Grilla oponente J1
        self.assertEqual(juego[4][0], grilla_vacia_2x2) # Grilla local J2
        self.assertEqual(juego[4][1], grilla_vacia_2x2) # Grilla oponente J2

        # Asegura que las grillas sean objetos independientes
        self.assertIsNot(juego[3][0], juego[3][1])
        self.assertIsNot(juego[4][0], juego[4][1])
        self.assertIsNot(juego[3][0], juego[4][0])
        self.assertIsNot(juego[3][1], juego[4][1])

    def test_grilla_2x3(self):
        grilla_resultado = [[VACÍO, VACÍO, VACÍO],[VACÍO, VACÍO, VACÍO]]
        self.assertEqual(grillaVacía(2,3), grilla_resultado)

    def test_grilla_1x1(self):
        grilla_resultado = [[VACÍO]]
        self.assertEqual(grillaVacía(1,1), grilla_resultado)

    def test_grilla_3x1(self):
        grilla_resultado = [[VACÍO],[VACÍO],[VACÍO]]
        self.assertEqual(grillaVacía(3,1), grilla_resultado)

    def test_tablero_2x2(self):
        tablero = nuevoTablero(2,2)
        grilla_vacia_2x2 = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        
        self.assertEqual(tablero[0], grilla_vacia_2x2)
        self.assertEqual(tablero[1], grilla_vacia_2x2)
        self.assertIsNot(tablero[0], tablero[1])

    def test_tablero_1x3(self):
        tablero = nuevoTablero(1,3)
        grilla_vacia_1x3 = [[VACÍO, VACÍO, VACÍO]]

        self.assertEqual(tablero[0], grilla_vacia_1x3)
        self.assertEqual(tablero[1], grilla_vacia_1x3)
        self.assertIsNot(tablero[0], tablero[1])

    def test_grilla_totalmente_vacia_2x2(self):
        grilla = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        self.assertTrue(esGrillaVacía(grilla))
        self.assertEqual(grilla, [[VACÍO, VACÍO],[VACÍO, VACÍO]])

    def test_grilla_con_un_barco(self):
        grilla = [[VACÍO, VACÍO],[BARCO, VACÍO]]
        self.assertFalse(esGrillaVacía(grilla))

    def test_grilla_con_agua(self):
        grilla = [[VACÍO, AGUA],[VACÍO, VACÍO]]
        self.assertFalse(esGrillaVacía(grilla))

    def test_grilla_1x1_vacia(self):
        grilla = [[VACÍO]]
        self.assertTrue(esGrillaVacía(grilla))

    def test_grilla_1x1_con_barco(self):
        grilla = [[BARCO]]
        self.assertFalse(esGrillaVacía(grilla))


# Tests Ejercicio 3
class esEstadoDeJuegoVálido_Test(unittest.TestCase):
    def test_grilla_DOS_local_no_coincide_con_disponibles(self): # la grillaDOSlocal tiene un solo barco de tamaño 3, en lugar de dos de tamaño 2
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaVacia = [[VACÍO, VACÍO, VACÍO, VACÍO]]*4
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, BARCO], # Barco de 3
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaVacia), (grillaDosLocal, grillaVacia))
        
        self.assertFalse(coincidenBarcosEnGrilla([2,2], grillaDosLocal))
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado[1], [2,2]) # Se mantiene el estado original

    def test_tablero_valido(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        estado = ((2,2),[2],[UNO],tablero_valido,tablero_valido)
        self.assertTrue(tableroVálidoEnJuego(tablero_valido,estado))
    
    def test_tablero_error_dimensiones_jugador(self):
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        estado = ((2,2),[2],[UNO],(grillaVacía(2,2),grillaVacía(2,2)),(grillaVacía(2,2),grillaVacía(2,2)))
        grilla_invalida = [[VACÍO, VACÍO, VACÍO]]
        tablero_invalido = (grilla_invalida, grilla_oponente_valida)
        self.assertFalse(tableroVálidoEnJuego(tablero_invalido,estado))

    def test_tablero_dimensiones_oponente(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_invalida = [[VACÍO, VACÍO, VACÍO]]
        tablero_invalido = (grilla_valida, grilla_invalida)
        estado = ((2,2),[2],[UNO],(grillaVacía(2,2),grillaVacía(2,2)),(grillaVacía(2,2),grillaVacía(2,2)))
        self.assertFalse(tableroVálidoEnJuego(tablero_invalido,estado))

    def test_tablero_no_coinciden_barcos(self):
        grilla_con_barco_3 = [[BARCO, VACÍO],[BARCO, VACÍO],[BARCO, VACÍO]] # Barco de tamaño 3
        grilla_oponente_valida_3x2 = grillaVacía(3,2)
        tablero_barco_3 = (grilla_con_barco_3,grilla_oponente_valida_3x2)
        estado_3x2 = ((3,2),[2], [UNO], tablero_barco_3, tablero_barco_3) # Barco disponible de tamaño 2
        self.assertFalse(tableroVálidoEnJuego(tablero_barco_3,estado_3x2))

    def test_coinciden_perfectamente(self):
        # Grilla compleja
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        barcos_disponibles = [3, 2, 2, 3] # Tamaños: 3, 2, 2, 3
        self.assertTrue(coincidenBarcosEnGrilla(barcos_disponibles, grilla))

    def test_no_coinciden_por_cantidad(self):
        grilla: Grilla = [[BARCO],[BARCO]] # Barco de tamaño 2
        barcos_disponibles = [2,2]
        self.assertFalse(coincidenBarcosEnGrilla(barcos_disponibles, grilla))

    def test_no_coinciden_por_tamanio(self):
        grilla: Grilla = [[BARCO],[BARCO]] # Barco de tamaño 2
        barcos_disponibles = [3]
        self.assertFalse(coincidenBarcosEnGrilla(barcos_disponibles, grilla))

    def test_grilla_vacia_barcos_vacios(self):
        grilla = grillaVacía(3,3)
        barcos_disponibles = []
        self.assertTrue(coincidenBarcosEnGrilla(barcos_disponibles, grilla))
    
    def test_grilla_vacia_barcos_disponibles(self):
        grilla = grillaVacía(3,3)
        barcos_disponibles = [2]
        self.assertFalse(coincidenBarcosEnGrilla(barcos_disponibles, grilla))

    def test_grilla_con_barcos_vacios(self):
        grilla: Grilla = [[BARCO],[BARCO]]
        barcos_disponibles = []
        self.assertFalse(coincidenBarcosEnGrilla(barcos_disponibles, grilla))

    def test_lista_barcos_vacia(self):
        self.assertEqual(tamaños([]),[])
    
    def test_lista_varios_barcos(self):
        barcos = [[('A',1),('A',2)],[('C',3)],[('F',4),('F',5),('F',6)]]
        self.assertEqual(tamaños(barcos),[2,1,3])

    def test_lista_barcos_mismo_tamanio(self):
        barcos = [[('A',1),('A',2)],[('C',1),('C',2)]]
        self.assertEqual(tamaños(barcos),[2,2])

    def test_listas_vacias(self):
        self.assertTrue(mismosElementos([],[]))

    def test_listas_iguales_mismo_orden(self):
        self.assertTrue(mismosElementos([1,2,3],[1,2,3]))
    
    def test_listas_iguales_distinto_orden(self):
        self.assertTrue(mismosElementos([1,2,3],[3,2,1]))

    def test_listas_con_duplicados_iguales(self):
        self.assertTrue(mismosElementos([1,2,2,3],[2,3,1,2]))

    def test_listas_distinta_longitud(self):
        self.assertFalse(mismosElementos([1,2,3],[1,2]))

    def test_listas_mismos_elementos_distinta_cantidad(self):
        self.assertFalse(mismosElementos([1,2,2],[1,1,2]))

    def test_listas_distintos_elementos(self):
        self.assertFalse(mismosElementos([1,2,3],[1,2,4]))

    def test_listas_distintos_tipos_falla(self):
        self.assertFalse(mismosElementos([1,2],["1","2"]))

    def test_sin_ataques_coinciden(self):
        j1_local = [[BARCO, VACÍO],[BARCO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, BARCO],[VACÍO, BARCO]]
        j2_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2 = (j2_local, j2_oponente)

        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_ataque_j1_coincide(self):
        j1_local = [[BARCO, VACÍO],[BARCO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, BARCO],[VACÍO, BARCO]]
        j2_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)

        j1_oponente[0][0] = AGUA
        j2_local[0][0] = AGUA
        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_ataque_j1_tocado_coincide(self):
        j1_local = [[BARCO, VACÍO],[BARCO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, BARCO],[VACÍO, BARCO]]
        j2_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)

        # Si J1 dispara y toca un barco en (A,2)
        j1_oponente[0][1] = BARCO # J1 marca el impacto
        j2_local[0][1] = BARCO     # J2 mantiene el BARCO (solo fue impactado)
        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_ataque_j2_coincide(self):
        j1_local = [[BARCO, VACÍO],[BARCO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, BARCO],[VACÍO, BARCO]]
        j2_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)

        # Si J2 dispara y toca un barco en (A,1)
        j1_oponente[0][1] = AGUA # J1 falla
        j2_local[0][1] = AGUA     # J2 marca su ataque en tu local
        j2_oponente[0][0] = BARCO   #Ataque de J2
        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_j1_oponente_no_coincide_con_j2_local(self):
        j1_local = [[BARCO, VACÍO],[BARCO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, BARCO],[VACÍO, BARCO]]
        j2_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)

        # J1 marca impacto (BARCO), pero J2 marcó AGUA en su local
        j1_oponente[0][0] = BARCO
        j2_local[0][0] = AGUA
        self.assertFalse(coincidenPosicionesAtacadas(tablero1, tablero2))
        
    def test_menos_de_una_fila(self):
        tablero = nuevoTablero(3,3)
        estado = ((0,10), [3, 1], [UNO], tablero, tablero)
        self.assertFalse(esEstadoDeJuegoVálido(estado))
    
    def test_menos_de_una_columna(self):
        tablero = nuevoTablero(3,3)
        estado = ((10,0), [3, 1], [UNO], tablero, tablero)
        self.assertFalse(esEstadoDeJuegoVálido(estado))

    def test_estado_sin_barcos(self):
        tablero = nuevoTablero(3,3)
        estado = ((3,3), [], [UNO], tablero, tablero)
        self.assertFalse(esEstadoDeJuegoVálido(estado))

    def test_tablero_no_valido(self):
        tablero = nuevoTablero(3,3)
        # La grilla local (tablero[0]) no es válida
        estado = ((3,3), [3, 1], [UNO], (tablero[0], [[VACÍO,VACÍO,VACÍO]]), tablero)
        self.assertFalse(esEstadoDeJuegoVálido(estado))

    def test_pos_atacadas1_no_coinciden(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        
        # J1 dispara y marca AGUA en (A,2) de su oponente (tablero[1])
        # pero J2 tiene BARCO en (A,2) de su local (tablero_valido[0])
        tablero_valido_mutado = (grilla_valida, [[VACÍO, AGUA],[VACÍO, VACÍO]])
        estado = ((2,2),[2],[UNO],tablero_valido_mutado,tablero_valido)
        self.assertFalse(esEstadoDeJuegoVálido(estado))
    
    def test_pos_atacadas2_no_coinciden(self):
        j1_local = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_oponente = [[VACÍO, AGUA],[VACÍO, VACÍO]] # J2 atacó (A,2) con fallo
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)
        
        # J2 atacó (A,2) y marcó AGUA. J1 local en (A,2) DEBE ser AGUA o BARCO, no VACÍO
        # En este caso J1 local es VACÍO, por lo que no coincide
        self.assertFalse(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_estado_de_juego_valido(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        estado = ((2,2),[2],[UNO],tablero_valido,tablero_valido)
        self.assertTrue(esEstadoDeJuegoVálido(estado))

    def test_estadosub2_mayor_a_uno(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        estado = ((2,2),[2],[UNO,DOS],tablero_valido,tablero_valido) # Estado con lista de turno incorrecta
        self.assertFalse(esEstadoDeJuegoVálido(estado))

# Tests Ejercicio 4
class DispararEnPosición_Test(unittest.TestCase):
    def test_disparo_en_posicion_vacia(self):
        estado = nuevoJuego(2,2,[2])
        # J1 turno, J2 local vacío.
        
        # Preparación: J2 local tiene un barco en (A,1). (B,2) sigue VACÍO
        estado[4][0][0][0] = BARCO 
        
        # J1 (UNO) dispara a ("B", 2). J2 local en (B,2) es VACÍO
        resultado = dispararEnPosición(estado, ("B", 2)) 
        
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado[2], [DOS]) # Turno cambia a DOS
        self.assertEqual(estado[4][0][1][1], AGUA) # Local J2: AGUA
        self.assertEqual(estado[3][1][1][1], AGUA) # Oponente J1: AGUA

    def test_disparo_a_barco(self):
        estado = nuevoJuego(2,2,[2])
        # J2 local tiene un barco en (A,1).
        estado[4][0][0][0] = BARCO 
        
        # J1 (UNO) dispara a ("A", 1). J2 local en (A,1) es BARCO. Resultado: TOCADO.
        resultado = dispararEnPosición(estado, ("A", 1)) 
        
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado[2], [DOS]) # Turno cambia a DOS
        self.assertEqual(estado[4][0][0][0], BARCO) # Local J2 sigue siendo BARCO
        self.assertEqual(estado[3][1][0][0], BARCO) # Oponente J1 es BARCO

    def test_disparo_en_ultimo_barco_fila(self):
        estado = nuevoJuego(2,2,[2])
        # J2 local tiene un barco en (A,1).
        estado[4][0][0][0] = BARCO
        
        # CORRECCIÓN DE ERROR: Cambiar el turno para simular que J2 dispara a J1.
        estado[2][0] = DOS 
        
        # J2 (DOS) dispara a ("A", 2). J1 local en (A,2) es VACÍO. Resultado: NADA.
        resultado = dispararEnPosición(estado, ("A", 2)) 
        
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado[2], [UNO]) # Turno cambia a UNO
        self.assertEqual(estado[3][0][0][1], AGUA) # Local J1: AGUA
        self.assertEqual(estado[4][1][0][1], AGUA) # Oponente J2: AGUA

    def test_turno_inicial_dos(self):
        estado = nuevoJuego(2,2,[2])
        # J1 local tiene un barco en (A,1)
        estado[3][0][0][0] = BARCO
        
        # J2 comienza el turno (J1 estaba antes, pero el test lo hace así)
        estado[2][0] = DOS
        
        # Disparo: J2 (DOS) dispara a ("A", 1). J1 local en (A,1) es BARCO
        resultado = dispararEnPosición(estado, ("A",1))
        
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado[2], [UNO]) # Turno cambia a UNO
        self.assertEqual(estado[3][0][0][0], BARCO) # Local J1: sigue siendo BARCO
        self.assertEqual(estado[4][1][0][0], BARCO) # Oponente J2: BARCO


# Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):
    def test_varios_barcos_distintos_tamanios(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO], # B1, B4-B6
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], # C1
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO], # D1, D3-D4, D6
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]] # E6
        
        barcosEsperados: list[BarcoEnGrilla] = [
                                                [('B', 1), ('C', 1), ('D', 1)],       # V: B1-D1
                                                [('B', 4), ('B', 5), ('B', 6)],       # H: B4-B6
                                                [('D', 3), ('D', 4)],                 # H: D3-D4
                                                [('D', 6), ('E', 6)],                 # V: D6-E6
                                                ]
        
        self.assertCountEqual(barcosEnGrilla(grilla), barcosEsperados)

    def test_barcos_en_grilla_1_horizontal(self):
        grilla = [
            [BARCO, BARCO, VACÍO],
            [VACÍO, VACÍO, VACÍO]
        ]
        resultado = barcosEnGrilla(grilla)
        esperado = [[('A',1), ('A',2)]]
        self.assertEqual(resultado, esperado)

    def test_barcos_en_grilla_1_vertical(self):
        grilla = [
            [BARCO, VACÍO],
            [BARCO, VACÍO]
        ]
        resultado = barcosEnGrilla(grilla)
        esperado = [[('A',1), ('B',1)]]
        self.assertEqual(resultado, esperado)

    def test_barcos_en_grilla_varios(self):
        grilla = [
            [BARCO, BARCO, VACÍO],
            [VACÍO, BARCO, BARCO]
        ]
        resultado = barcosEnGrilla(grilla)
        esperado = [[('A',1), ('A',2)], [('B',2), ('B',3)]]
        self.assertCountEqual(resultado, esperado)

    def test_horizontal_y_vertical_false(self):
        grilla = [
            [BARCO, BARCO],
            [BARCO, VACÍO]
        ]
        self.assertFalse(noHayMásDeUnaFormaDeConstruirUnBarcoDesde(grilla, ('A',1))) # Puede ser H o V
        self.assertTrue(noHayMásDeUnaFormaDeConstruirUnBarcoDesde(grilla, ('B',2))) # No tiene vecinos BARCO

    def test_horizontal_true(self):
        grilla = [
            [BARCO, BARCO, VACÍO]
        ]
        self.assertTrue(sePuedeConstruirBarcoHorizontalDesde(grilla, ('A',1)))
        self.assertFalse(sePuedeConstruirBarcoHorizontalDesde(grilla, ('A',3)))

    def test_vertical_true(self):
        grilla = [[BARCO],[BARCO]]
        self.assertTrue(sePuedeConstruirBarcoVerticalDesde(grilla, ('A',1)))
        self.assertTrue(sePuedeConstruirBarcoVerticalDesde(grilla, ('B',1)))

    def test_todas_ocupadas(self):
        grilla = [
            [BARCO, BARCO]
        ]
        posiciones = [('A',1), ('A',2)]
        self.assertTrue(posicionesOcupadasEnGrilla(grilla, posiciones))

    def test_una_no_ocupada(self):
        grilla = [
            [BARCO, VACÍO]
        ]
        posiciones = [('A',1), ('A',2)]
        self.assertFalse(posicionesOcupadasEnGrilla(grilla, posiciones))

    def test_ocupa(self):
        barcos = [[('A',1), ('A',2)], [('B',1)]]
        self.assertTrue(algúnBarcoOcupaLaPosición(barcos, ('A',1)))
        self.assertTrue(algúnBarcoOcupaLaPosición(barcos, ('B',1)))
        self.assertFalse(algúnBarcoOcupaLaPosición(barcos, ('C',1)))


if __name__ == '__main__':
    unittest.main(verbosity=1)