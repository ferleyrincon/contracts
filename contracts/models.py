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
    num_rounds = 24
    likelihood_activity2= 0.1
    fixed_payoff = c(10000)
    use_timeout = True
    seconds_per_template = 1
    seconds_per_template3 = 0.1
    seconds_per_template7 = 0.1
    seconds_per_contract = 20
    num_contracts = 16

    contracts = {
    # contract# : [paymnet, insurance, bonus_relative, groups]    
        1 : [100000 , 20000 , 1 , 1],
        2 : [100000 , 20000 , 1 , 0],
        3 : [100000 , 20000 , 0 , 1],
        4 : [100000 , 20000 , 0 , 0],
        5 : [100000 , 10000 , 1 , 1],
        6 : [100000 , 10000 , 1 , 0],
        7 : [100000 , 10000 , 0 , 1],
        8 : [100000 , 10000 , 0 , 0],
        9 : [60000 , 12000 , 1 , 1],
        10 : [60000 , 12000 , 1 , 0],
        11 : [60000 , 12000 , 0 , 1],
        12 : [60000 , 12000 , 0 , 0],
        13 : [60000 , 6000 , 1 , 1],
        14 : [60000 , 6000 , 1 , 0],
        15 : [60000 , 6000 , 0 , 1],
        16 : [60000 , 6000 , 0 , 0],
    }

    config_screens = []
    ## CONFIGURACIÓN DE 
        # Unificacion de las configuraciones para las pantallas congruentes
    lst_colors =    [
                            '#0000ff',  # 0 blue
                            '#ff0000',  # 1 red
                            '#ffc000',  # 2 yellow
                            '#008000'   # 3 green
                        ]
    nombres_colores =   [
                            'Azul',         # 0
                            'Rojo',         # 1
                            'Amarillo',     # 2
                            'Verde'         # 3
                        ]
    # CONGRUENT
    # Configuracion de las palabras que van la mitad para las pantallas congruentes.
    config_word =    [
                            0, #1 -> blue
                            1, #2 -> red
                            0, #3 -> blue
                            2, #4 -> yellow
                            3, #5 -> green
                            1, #6 -> red
                            0, #7 -> blue
                            2, #8 -> yellow
                            2, #9 -> yellow
                            3, #10 -> green
                            1, #11 -> red
                            2, #12 -> yellow
                            3, #13 -> green
                            0, #14 -> blue
                            2, #15 -> yellow
                            3, #16 -> green
                            2, #17 -> yellow
                            0, #18 -> blue
                            1, #19 -> red
                            3, #20 -> green
                            0, #21 -> blue
                            1, #22 -> red
                            1, #23 -> red
                            3, #24 -> green
                        ]
    # IN-CONGRUENT
    # Configuracion del color para las pantallas in-congruentes.
    config_color =    [
                            2, #1 -> yellow
                            2, #2 -> yellow
                            3, #3 -> green
                            3, #4 -> green
                            2, #5 -> yellow
                            3, #6 -> green
                            2, #7 -> yellow
                            3, #8 -> green
                            1, #9 -> red
                            0, #10 -> blue
                            0, #11 -> blue
                            0, #12 -> blue
                            1, #13 -> red
                            1, #14 -> red
                            1, #15 -> red
                            2, #16 -> yellow
                            0, #17 -> blue
                            1, #18 -> red
                            0, #19 -> blue
                            0, #20 -> blue
                            3, #21 -> green
                            3, #22 -> green
                            2, #23 -> yellow
                            1, #24 -> red
                        ]
    # ANSWERS
    # Configuracion de lo que va a la derecha abajo, si palabra o color
    type_left =   [
                            'w' , #1
                            'c' , #2
                            'c' , #3
                            'w' , #4
                            'w' , #5
                            'c' , #6
                            'c' , #7
                            'w' , #8
                            'c' , #9
                            'c' , #10
                            'c' , #11
                            'w' , #12
                            'w' , #13
                            'c' , #14
                            'c' , #15
                            'c' , #16
                            'w' , #17
                            'c' , #18
                            'c' , #19
                            'c' , #20
                            'w' , #21
                            'w' , #22
                            'w' , #23
                            'w' , #24
                    ]
    # Configuracion de la palabra y color que va abajo a la izquierda en las pantallas congruentes
    config_left =     [
                            0, #1 -> blue
                            2, #2 -> yellow
                            3, #3 -> green
                            2, #4 -> yellow
                            3, #5 -> green
                            3, #6 -> green
                            2, #7 -> yellow
                            2, #8 -> yellow
                            1, #9 -> red
                            0, #10 -> blue
                            0, #11 -> blue
                            2, #12 -> yellow
                            3, #13 -> green
                            1, #14 -> red
                            1, #15 -> red
                            2, #16 -> yellow
                            2, #17 -> yellow
                            1, #18 -> red
                            0, #19 -> blue
                            0, #20 -> blue
                            0, #21 -> blue
                            1, #22 -> red
                            1, #23 -> red
                            3, #24 -> green
                        ]
    # Configuracion de la palabra y color que va abajo a la derecha en las pantallas congruentes
    config_right =     [
                            2, #1 -> yellow
                            1, #2 -> red
                            0, #3 -> blue
                            3, #4 -> green
                            2, #5 -> yellow
                            1, #6 -> red
                            0, #7 -> blue
                            3, #8 -> green
                            2, #9 -> yellow
                            3, #10 -> green
                            1, #11 -> red
                            0, #12 -> blue
                            1, #13 -> red
                            0, #14 -> blue
                            2, #15 -> yellow
                            3, #16 -> green
                            0, #17 -> blue
                            0, #18 -> blue
                            1, #19 -> red
                            3, #20 -> green
                            3, #21 -> green
                            3, #22 -> green
                            2, #23 -> yellow
                            1, #24 -> red
                        ]
    for i in range(len(config_word)):
        t_dict = {"word": nombres_colores[config_word[i]], "word2": nombres_colores[config_color[i]], "word_color": lst_colors[config_word[i]], "color": lst_colors[config_color[i]], "left": type_left[i], "opc1": nombres_colores[config_left[i]], "opc2": nombres_colores[config_right[i]], "in_t7": "l"+str(i+1)}
        config_screens.append(t_dict)


class Subsession(BaseSubsession):
    def creating_session(self):
        # Para el random del congruente
        for j in self.get_players():
            j.get_congruent()

        if self.round_number == 1:
            for p in self.get_players():
               #p.contract_pago = random.randint(1,4)
                p.participant.vars['orden_preguntas'] = json.dumps((np.random.choice(Constants.num_contracts, Constants.num_contracts, replace=False) + 1).tolist())
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
    n_contract          =   models.IntegerField()  # contract number displayed
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

    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')

    contract_pago = models.IntegerField()

    congruent = models.BooleanField() # Saber si es tratamiento congruente o no congruente el jugador

    def rellenar_campos(self, campo):
        for i in range(1, Constants.num_rounds+1):
            setattr(self.in_round(i), campo, getattr(self, campo))

    def get_congruent(self):
        self.congruent = random.choice([True, False])
        self.participant.vars['congruent'] = self.congruent
        return self.congruent
