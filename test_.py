
class constants(self):

    n_contract = 0
    lst_colors =    [
                        'blue',     # 0
                        'red',      # 1
                        'yellow',   # 2
                        'green'     # 3
                        ]
    nombres_colores =   [
                            'Azul',         # 0
                            'Rojo',         # 1
                            'Amarillo',     # 2
                            'Verde'         # 3
                            ]
        # Congruentes
            # Configuracion de las palabras que van la mitad para las pantallas congruentes
    config_words_c =    [
                            0,  # 01 -> 'blue'
                            1,  # 02 -> 'red'
                            0,  # 03 -> 'blue'
                            2,  # 04 -> 'yellow'
                            3,  # 05 -> 'green'
                            1,  # 06 -> 'red'
                            0,  # 07 -> 'blue'
                            2,  # 08 -> 'yellow'
                            2,  # 09 -> 'yellow'
                            3,  # 10 -> 'green'
                            1,  # 11 -> 'red'
                            2,  # 12 -> 'yellow'
                            3,  # 13 -> 'green'
                            0,  # 14 -> 'blue'
                            2,  # 15 -> 'yellow'
                            3,  # 16 -> 'green'
                            2,  # 17 -> 'yellow'
                            0,  # 18 -> 'blue'
                            1,  # 19 -> 'red'
                            3,  # 20 -> 'green'
                            0,  # 21 -> 'blue'
                            1,  # 22 -> 'red'
                            1,  # 23 -> 'red'
                            3   # 24 -> 'green'
                            ]
            # Configuracion del color para las pantallas congruentes
    config_color_c =    [
                            2,  # 01 -> 'yellow'
                            2,  # 02 -> 'yellow'
                            3,  # 03 -> 'green'
                            3,  # 04 -> 'green'
                            2,  # 05 -> 'yellow'
                            3,  # 06 -> 'green'
                            2,  # 07 -> 'yellow'
                            3,  # 08 -> 'green'
                            1,  # 09 -> 'red'
                            0,  # 10 -> 'blue'
                            0,  # 11 -> 'blue'
                            0,  # 12 -> 'blue'
                            1,  # 13 -> 'red'
                            1,  # 14 -> 'red'
                            1,  # 15 -> 'red'
                            2,  # 16 -> 'yellow'
                            0,  # 17 -> 'blue'
                            1,  # 18 -> 'red'
                            0,  # 19 -> 'blue'
                            0,  # 20 -> 'blue'
                            3,  # 21 -> 'green'
                            3,  # 22 -> 'green'
                            2,  # 23 -> 'yellow'
                            1   # 24 -> 'red'
                            ]
            # Configuracion de lo que va a la derecha abajo, si palabra o color
    type_left_c =   [
                        'w',    # 01
                        'c',    # 02
                        'c',    # 03
                        'c',    # 04
                        'w',    # 05
                        'c',    # 06
                        'w',    # 07
                        'w',    # 08
                        'c',    # 09
                        'w',    # 10
                        'w',    # 11
                        'c',    # 12
                        'c',    # 13
                        'c',    # 14
                        'c',    # 15
                        'w',    # 16
                        'w',    # 17
                        'w',    # 18
                        'w',    # 19
                        'c',    # 20
                        'c',    # 21
                        'c',    # 22
                        'c',    # 23
                        'w'     # 24
                        ]
            # Configuracion de la palabra y color que va abajo a la izquierda en las pantallas congruentes
    config_left_c =     [
                            0,  # 01 -> 'blue'
                            2,  # 02 -> 'yellow'
                            3,  # 03 -> 'green'
                            3,  # 04 -> 'green'
                            3,  # 05 -> 'green'
                            3,  # 06 -> 'green'
                            0,  # 07 -> 'blue'
                            2,  # 08 -> 'yellow'
                            1,  # 09 -> 'red'
                            3,  # 10 -> 'green'
                            1,  # 11 -> 'red'
                            0,  # 12 -> 'blue'
                            1,  # 13 -> 'red'
                            1,  # 14 -> 'red'
                            1,  # 15 -> 'red'
                            3,  # 16 -> 'green'
                            2,  # 17 -> 'yellow'
                            0,  # 18 -> 'blue'
                            1,  # 19 -> 'red'
                            0,  # 20 -> 'blue'
                            3,  # 21 -> 'green'
                            3,  # 22 -> 'green'
                            2,  # 23 -> 'yellow'
                            3   # 24 -> 
                            ]
            # Configuracion de la palabra y color que va abajo a la derecha en las pantallas congruentes
    config_right_c =    [
                            2,  # 01 -> 'yellow'
                            1,  # 02 -> 'red'
                            0,  # 03 -> 'blue'
                            2,  # 04 -> 'yellow'
                            2,  # 05 -> 'yellow'
                            1,  # 06 -> 'red'
                            2,  # 07 -> 'yellow'
                            3,  # 08 -> 'green'
                            2,  # 09 -> 'yellow'
                            0,  # 10 -> 'blue'
                            0,  # 11 -> 'blue'
                            2,  # 12 -> 'yellow'
                            3,  # 13 -> 'green'
                            0,  # 14 -> 'blue'
                            2,  # 15 -> 'yellow'
                            2,  # 16 -> 'yellow'
                            0,  # 17 -> 'blue'
                            1,  # 18 -> 'red'
                            0,  # 19 -> 'blue'
                            3,  # 20 -> 'green'
                            0,  # 21 -> 'blue'
                            1,  # 22 -> 'red'
                            1,  # 23 -> 'red'
                            1   # 24 -> 'red'
                            ]
            # Unificacion de las configuraciones para las pantallas congruentes
    config_screens_c = [{'word': nombres_colores[config_words_c[i]], 'word_color': lst_colors[config_words_c[i]], 'color': lst_colors[config_color_c[i]], 'left': type_left_c[i], 'opc1': nombres_colores[config_left_c[i]], 'opc2': nombres_colores[config_right_c[i]]} for i in range(24)]

print(config_screens_c)

print("--------------------------------")

for i in config_screens_c:
    print(i)