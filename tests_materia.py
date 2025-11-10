import unittest
from batallaNaval import *

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
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        juego = nuevoJuego(2,2,[2])
        
        self.assertEqual(juego[0], (2,2))
        self.assertTrue(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

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
        grilla_vacia_2x2 = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_resultado = (grilla_vacia_2x2, grilla_vacia_2x2)
        self.assertEqual(nuevoTablero(2,2), tablero_resultado)

    def test_tablero_1x3(self):
        grilla_vacia_1x3 = [[VACÍO, VACÍO, VACÍO]]
        tablero_resultado = (grilla_vacia_1x3, grilla_vacia_1x3)
        self.assertEqual(nuevoTablero(1,3), tablero_resultado)

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
    def test_grilla_DOS_local_no_coincide_con_disponibles(self): # la grillaDOSlocal tiene un solo barco de tamaño 3, en lugar de dos de tamaño 2.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_tablero_valido(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        estado = ((2,2),[2],[UNO],tablero_valido,tablero_valido)
        self.assertTrue(tableroVálidoEnJuego(tablero_valido,estado))
    
    def test_tablero_error_dimensiones_jugador(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        estado = ((2,2),[2],[UNO],tablero_valido,tablero_valido)
        grilla_invalida = [[VACÍO, VACÍO, VACÍO]]
        tablero_invalido = (grilla_invalida, grilla_oponente_valida)
        self.assertFalse(tableroVálidoEnJuego(tablero_invalido,estado))

    def test_tablero_dimensiones_oponente(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        estado = ((2,2),[2],[UNO],tablero_valido,tablero_valido)
        grilla_invalida = [[VACÍO, VACÍO, VACÍO]]
        tablero_invalido = (grilla_invalida, grilla_invalida)
        self.assertFalse(tableroVálidoEnJuego(tablero_invalido,estado))

    def test_tablero_no_coinciden_barcos(self):
        grilla_con_barco_3 = [[BARCO, VACÍO],[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida_3x2 = grillaVacía(3,2)
        tablero_barco_3 = (grilla_con_barco_3,grilla_oponente_valida_3x2)
        estado_3x2 = ((3,2),[2],[UNO],tablero_barco_3,tablero_barco_3)
        self.assertFalse(tableroVálidoEnJuego(tablero_barco_3,estado_3x2))

    def test_coinciden_perfectamente(self):
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        barcos_disponibles = [2,2,1,1,2,2]
        self.assertTrue(coincidenBarcosEnGrilla(barcos_disponibles, grilla))

    def test_no_coinciden_por_cantidad(self):
        grilla: Grilla = [[BARCO],[BARCO]]
        barcos_disponibles = [2,2]
        self.assertFalse(coincidenBarcosEnGrilla(barcos_disponibles, grilla))

    def test_no_coinciden_por_tamanio(self):
        grilla: Grilla = [[BARCO],[BARCO]]
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

        j1_oponente[0][1] = BARCO
        j2_local[0][1] = BARCO
        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_ataque_j2_coincide(self):
        j1_local = [[BARCO, VACÍO],[BARCO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, BARCO],[VACÍO, BARCO]]
        j2_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)

        j2_oponente[0][0] = BARCO
        j1_local[0][0] = BARCO
        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_j1_oponente_no_coincide_con_j2_local(self):
        j1_local = [[BARCO, VACÍO],[BARCO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, BARCO],[VACÍO, BARCO]]
        j2_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)

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
        tablero[0].pop()
        estado = ((3,3), [3, 1], [UNO], tablero, tablero)
        self.assertFalse(esEstadoDeJuegoVálido(estado))

    def test_pos_atacadas1_no_coinciden(self):
        grilla_valida = [[BARCO, VACÍO],[BARCO, VACÍO]]
        grilla_oponente_valida = [[VACÍO, AGUA],[VACÍO, VACÍO]]
        tablero_valido = (grilla_valida, grilla_oponente_valida)
        estado = ((2,2),[2],[UNO],tablero_valido,tablero_valido)
        self.assertFalse(esEstadoDeJuegoVálido(estado))
    
    def test_pos_atacadas2_no_coinciden(self):
        j1_local = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j1_oponente = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_local = [[VACÍO, VACÍO],[VACÍO, VACÍO]]
        j2_oponente = [[VACÍO, AGUA],[VACÍO, VACÍO]]
        tablero1 = (j1_local, j1_oponente)
        tablero2= (j2_local, j2_oponente)

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
        estado = ((2,2),[2],[UNO,DOS],tablero_valido,tablero_valido)
        self.assertFalse(esEstadoDeJuegoVálido(estado))

# Tests Ejercicio 4
class DispararEnPosición_Test(unittest.TestCase):
    def test_disparo_en_posicion_vacia(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_a_barco(self):
        estado = ((3,3), [2], [UNO],
            ([[BARCO, BARCO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]]))
       
        estado_esperado = ((3,3), [2], [DOS],
            ([[BARCO, BARCO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]],
             [[AGUA, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]]))
        
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_a_ultimo_barco_fila(self):
        estado = ((2,3), [2], [DOS],
            ([[VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]]),
            ([[BARCO, BARCO, VACÍO],
              [VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]]))
        
        estado_esperado = ((2,3), [2], [UNO],
            ([[VACÍO, BARCO, AGUA],
              [VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO]]),
            ([[BARCO, BARCO, VACÍO],
              [VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, BARCO],
              [VACÍO, VACÍO, VACÍO]]))
        resultado = dispararEnPosición(estado, ("A", 3))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_barco(self):
        estado = ((2,2), [2], [UNO],
            ([[BARCO, VACÍO],
              [VACÍO, VACÍO]],
             [[VACÍO, VACÍO],
              [VACÍO, VACÍO]]),
            ([[BARCO, BARCO],
              [VACÍO, VACÍO]],
             [[VACÍO, VACÍO],
              [VACÍO, VACÍO]]))

        estado_esperado = ((2,2), [2], [DOS],
            ([[BARCO, VACÍO],
              [VACÍO, VACÍO]],
             [[BARCO, VACÍO],
              [VACÍO, VACÍO]]),
            ([[AGUA, BARCO],
              [VACÍO, VACÍO]],
             [[VACÍO, VACÍO],
              [VACÍO, VACÍO]]))
        
        resultado = dispararEnPosición(estado, ("A",1))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)


    def test_disparo_en_ultimo_barco_fila(self):
        estado = ((2,2), [2], [UNO],
                  ([[BARCO,VACÍO],
                    [BARCO, VACÍO]],
                    [[VACÍO,VACÍO],
                    [VACÍO,VACÍO]]),
                    ([[BARCO,BARCO],
                      [VACÍO,VACÍO]],
                      [[VACÍO,VACÍO],
                       [VACÍO,VACÍO]]))
        estado_esperado = ((2,2), [2], [DOS],
                  ([[BARCO,VACÍO],
                    [BARCO, VACÍO]],
                    [[VACÍO,VACÍO],
                    [AGUA,VACÍO]]),
                    ([[BARCO,BARCO],
                      [AGUA,VACÍO]],
                      [[VACÍO,VACÍO],
                       [VACÍO,VACÍO]]))
        resultado = dispararEnPosición(estado, ("B",1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_turno_inicial_dos(self):
      estado = ((2,2), [2], [DOS],  # turno inicial DOS
          ([[BARCO, VACÍO],
            [VACÍO, VACÍO]],
          [[VACÍO, VACÍO],
            [VACÍO, VACÍO]]),
          ([[BARCO, BARCO],
            [VACÍO, VACÍO]],
          [[VACÍO, VACÍO],
            [VACÍO, VACÍO]]))

      estado_esperado = ((2,2), [2], [UNO],  # cambia turno a UNO
          ([[AGUA, VACÍO],
            [VACÍO, VACÍO]],
          [[VACÍO, VACÍO],
            [VACÍO, VACÍO]]),
          ([[BARCO, BARCO],
            [VACÍO, VACÍO]],
          [[BARCO, VACÍO],
            [VACÍO, VACÍO]]))

      resultado = dispararEnPosición(estado, ("A",1))
      self.assertEqual(resultado, TOCADO)
      self.assertEqual(estado, estado_esperado)


# Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):
    def test_varios_barcos_distintos_tamanios(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('D',3), ('D',4)],
                                                [('B',6), ('B',5), ('B',4)],
                                                [('D',6), ('E',6)],
                                                [('D',1),('C',1), ('B',1)]]
        
        # Pensar! qué pasa si el orden de los barcos en la lista no es el mismo? respeta la especificación?
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])

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
        self.assertEqual(resultado, esperado)

    def test_horizontal_y_vertical_false(self):
        grilla = [
            [BARCO, BARCO],
            [BARCO, VACÍO]
        ]
        self.assertFalse(noHayMásDeUnaFormaDeConstruirUnBarcoDesde(grilla, ('A',1)))
        self.assertTrue(noHayMásDeUnaFormaDeConstruirUnBarcoDesde(grilla, ('B',2)))

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
