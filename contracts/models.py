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
    # "contract#" : [paymnet, insurance, bonus relative , alone ]    
        "c1" :  [60000  , 12000 , 1 , 0],
        "c2" :  [60000  , 12000 , 0 , 0],
        "c3" :  [60000  , 12000 , 1 , 1],
        "c4" :  [60000  , 12000 , 0 , 1],
        "c5" :  [60000  , 6000  , 1 , 0],
        "c6" :  [60000  , 6000  , 0 , 0],
        "c7" :  [60000  , 6000  , 1 , 1],
        "c8" :  [60000  , 6000  , 0 , 1],
        "c9" :  [100000 , 20000 , 1 , 0],
        "c10" : [100000 , 20000 , 0 , 0],
        "c11" : [100000 , 20000 , 1 , 1],
        "c12" : [100000 , 20000 , 0 , 1],
        "c13" : [100000 , 10000 , 1 , 0],
        "c14" : [100000 , 10000 , 0 , 0],
        "c15" : [100000 , 10000 , 1 , 1],
        "c16" : [100000 , 10000 , 0 , 1]
        }

    config_screens_c = []
    ## Configuracion para las pantallas
        # Unificacion de las configuraciones para las pantallas congruentes
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
    for i in range(len(config_words_c)):
        #print("| {:>2d} |{:^10s}|{:^8s}|{:^8s}|{:^8s}|{:^10s}|{:^10s}|".format((i+1), nombres_colores[config_words_c[i]], lst_colors[config_words_c[i]], lst_colors[config_color_c[i]], type_left_c[i], nombres_colores[config_left_c[i]], nombres_colores[config_right_c[i]]))
        t_dict = {"word": nombres_colores[config_words_c[i]], "word_color": lst_colors[config_words_c[i]], "color": lst_colors[config_color_c[i]], "left": type_left_c[i], "opc1": nombres_colores[config_left_c[i]], "opc2": nombres_colores[config_right_c[i]]}
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
    c1 =  models.IntegerField()
    c2 =  models.IntegerField()
    c3 =  models.IntegerField()
    c4 =  models.IntegerField()
    c5 =  models.IntegerField()
    c6 =  models.IntegerField()
    c7 =  models.IntegerField()
    c8 =  models.IntegerField()
    c9 =  models.IntegerField()
    c10 =  models.IntegerField()
    c11 =  models.IntegerField()
    c12 =  models.IntegerField()
    c13 =  models.IntegerField()
    c14 =  models.IntegerField()
    c15 =  models.IntegerField()
    c16 =  models.IntegerField()

    n_contract = models.IntegerField(initial=0)
    #config_scn = Constants.config_screens_c[n_contract]

    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')


    contract_pago = models.IntegerField()
    #pago = models.CurrencyField(initial=0)

    def rellenar_campos(self, campo):
        for i in range(1, Constants.num_rounds+1):
            setattr(self.in_round(i), campo, getattr(self, campo))

#    tasks

