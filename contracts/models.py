from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy as np
import random
import json




author = 'Cesar Mantilla & Ferley Rincón'

doc = """
Cognitive load and the valuation of job attributes: evidence from an eye-tracking experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'contracts'
    players_per_group = None
    num_rounds = 16
    likelihood_activity= 0.1
    fixed_payoff = c(20000)
    contract_payoff = random.randint(1, num_rounds)
    use_timeout = True
    seconds_per_tasks1 = 1
    seconds_per_tasks2 = 10
    seconds_per_contract = 10

    contracts = {
    # contract# : [paymnet, insurance, alone, bonus relative]    
        1   :   [60000,     12000,      1,      0],
        2   :   [60000,     12000,      0,      0],
        3   :   [60000,     12000,      1,      1],
        4   :   [60000,     12000,      0,      1],
        5   :   [60000,     6000,       1,      0],
        6   :   [60000,     6000,       0,      0],
        7   :   [60000,     6000,       1,      1],
        8   :   [60000,     6000,       0,      1],
        9   :   [100000,    20000,      1,      0],
        10  :   [100000,    20000,      0,      0],
        11  :   [100000,    20000,      1,      1],
        12  :   [100000,    20000,      0,      1],
        13  :   [100000,    10000,      1,      0],
        14  :   [100000,    10000,      0,      0],
        15  :   [100000,    10000,      1,      1],
        16  :   [100000,    10000,      0,      1]
        }

    config_screens_c = []
    ## Configuracion para las pantallas
        # Unificacion de las configuraciones para las pantallas congruentes
    lst_colors =    [
                        '#0000ff',  # 0 BLUE
                        '#ff0000',  # 1 RED
                        '#ffc000',  # 2 YELLOW
                        '#008000'   # 3 GREEN
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
                            3   # 24 -> 'green'
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
    for i in range(len(config_words_c)):
        t_dict = {"word": nombres_colores[config_words_c[i]], "word_color": lst_colors[config_words_c[i]], "color": lst_colors[config_color_c[i]], "left": type_left_c[i], "opc1": nombres_colores[config_left_c[i]], "opc2": nombres_colores[config_right_c[i]], "in_t7": "l"+str(i+1)}
        config_screens_c.append(t_dict)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
               #p.contract_pago = random.randint(1,4)
                p.participant.vars['orden_preguntas'] = json.dumps((np.random.choice(Constants.num_rounds, Constants.num_rounds, replace=False) + 1).tolist())
        #else:
            #for p in self.get_players():
                #p.contract_pago = p.in_round(1).pregunta_pago
    
    #def set_pago_jugadores(self):
    #    for j in self.get_players():
    #        j.set_pago()

    #def set_rank_contracts(self):
    #    rank_contracts = {}
    #    for k,j in enumerate(self.get_players()):
    #        rank_contracts['j' + str(k+1)] = j.append("c" + str(k))
    #    self.rank_contracts = json.dumps(self.sort(rank_contracts))

    #def set_contract_payoff(self):
    #    rank_contracts = json.loads(self.rank_contracts)
    #    self.position_ranking = rank_contracts[self.subsession.contract_payoff]    


class Group(BaseGroup): 
    pass


class Player(BasePlayer):
    n_round             =   models.IntegerField()  # round number 
    n_contract          =   models.IntegerField()  # contract number displated
    choice              =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])  # choice chosen by the player
    # if you do not choose any before the default time, 9 is placed
    choice_time         =   models.FloatField()  # time it took the player to choose his final choice
    # if you didn't choose any option the time is 0
    list_choice         =   models.StringField() # list with the elections for this contract
    # every time the player presses an option the value of that option is saved in this list
    # if the player does not press any option the list is empty
    list_time_choice    =   models.StringField() # list with the times for this contract
    # each time an option is pressed in this list adds the time it took to press since 
    # this screen was displayed
    # if the player does not press any option the list is empty
    left                =   models.StringField() # to know if the player pressed the right
    # or left option = 1 -> left | 2 -> right
    # if the player does not press any option the value will be 9
    left_time           =   models.FloatField() # time it takes to choose 

    '''
    c1 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t1 =    models.FloatField()  # time
    adc1 =  models.StringField() # array data choice by contract 1
    atc1 =  models.StringField() # array time choice by contract 1
    l1 =    models.StringField() # value of left by contract 1 -> 1: left, 2: right
    l1_time = models.FloatField() # time it takes to choose 

    c2 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t2 =    models.FloatField() 
    adc2 =  models.StringField() # array data choice by contract 2
    atc2 =  models.StringField() # array time choice by contract 2
    l2 =    models.StringField() # value of left by contract 2 -> 1: left, 2: right
    l2_time = models.FloatField() # time it takes to choose 

    c3 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t3 =    models.FloatField()
    adc3 =  models.StringField() # array data choice by contract 3
    atc3 =  models.StringField() # array time choice by contract 3
    l3 =    models.StringField() # value of left by contract 3 -> 1: left, 2: right
    l3_time = models.FloatField() # time it takes to choose 

    c4 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t4 =    models.FloatField()
    adc4 =  models.StringField() # array data choice by contract 4
    atc4 =  models.StringField() # array time choice by contract 4
    l4 =    models.StringField() # value of left by contract 4 -> 1: left, 2: right
    l4_time = models.FloatField() # time it takes to choose 

    c5 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t5 =    models.FloatField()
    adc5 =  models.StringField() # array data choice by contract 5
    atc5 =  models.StringField() # array time choice by contract 5
    l5 =    models.StringField() # value of left by contract 5 -> 1: left, 2: right
    l5_time = models.FloatField() # time it takes to choose 

    c6 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t6 =    models.FloatField()
    adc6 =  models.StringField() # array data choice by contract 6
    atc6 =  models.StringField() # array time choice by contract 6
    l6 =    models.StringField() # value of left by contract 6 -> 1: left, 2: right
    l6_time = models.FloatField() # time it takes to choose 

    c7 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t7 =    models.FloatField()
    adc7 =  models.StringField() # array data choice by contract 7
    atc7 =  models.StringField() # array time choice by contract 7
    l7 =    models.StringField() # value of left by contract 7 -> 1: left, 2: right
    l7_time = models.FloatField() # time it takes to choose 

    c8 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t8 =    models.FloatField()
    adc8 =  models.StringField() # array data choice by contract 8
    atc8 =  models.StringField() # array time choice by contract 8
    l8 =    models.StringField() # value of left by contract 8 -> 1: left, 2: right
    l8_time = models.FloatField() # time it takes to choose 

    c9 =    models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t9 =    models.FloatField()
    adc9 =  models.StringField() # array data choice by contract 9
    atc9 =  models.StringField() # array time choice by contract 9
    l9 =    models.StringField() # value of left by contract 1 -> 1: left, 2: right
    l9_time = models.FloatField() # time it takes to choose 

    c10 =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t10 =   models.FloatField()
    adc10 = models.StringField() # array data choice by contract 10
    atc10 = models.StringField() # array time choice by contract 10
    l10 =    models.StringField() # value of left by contract 10 -> 1: left, 2: right
    l10_time = models.FloatField() # time it takes to choose 

    c11 =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t11 =   models.FloatField()
    adc11 = models.StringField() # array data choice by contract 11
    atc11 = models.StringField() # array time choice by contract 11
    l11 =    models.StringField() # value of left by contract 1 -> 1: left, 2: right
    l11_time = models.FloatField() # time it takes to choose 

    c12 =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t12 =   models.FloatField()
    adc12 = models.StringField() # array data choice by contract 12
    atc12 = models.StringField() # array time choice by contract 12
    l12 =    models.StringField() # value of left by contract 1 -> 1: left, 2: right
    l12_time = models.FloatField() # time it takes to choose 

    c13 =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t13 =   models.FloatField()
    adc13 = models.StringField() # array data choice by contract 13
    atc13 = models.StringField() # array time choice by contract 13
    l13 =    models.StringField() # value of left by contract 13 -> 1: left, 2: right
    l13_time = models.FloatField() # time it takes to choose 

    c14 =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t14 =   models.FloatField()
    adc14 = models.StringField() # array data choice by contract 14
    atc14 = models.StringField() # array time choice by contract 14
    l14 =    models.StringField() # value of left by contract 14 -> 1: left, 2: right
    l14_time = models.FloatField() # time it takes to choose 

    c15 =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t15 =   models.FloatField()
    adc15 = models.StringField() # array data choice by contract 15
    atc15 = models.StringField() # array time choice by contract 15
    l15 =    models.StringField() # value of left by contract 15 -> 1: left, 2: right
    l15_time = models.FloatField() # time it takes to choose 

    c16 =   models.IntegerField(initial = 9, widget=widgets.RadioSelect, choices=[1,2,3,4,5,9])
    t16 =   models.FloatField()
    adc16 = models.StringField() # array data choice by contract 16
    atc16 = models.StringField() # array time choice by contract 16
    l16 =    models.StringField() # value of left by contract 16 -> 1: left, 2: right
    l16_time = models.FloatField() # time it takes to choose 
    '''

    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')

    contract_pago = models.IntegerField()
    #pago = models.CurrencyField(initial=0)

    def rellenar_campos(self, campo):
        for i in range(1, Constants.num_rounds+1):
            setattr(self.in_round(i), campo, getattr(self, campo))

#    tasks

