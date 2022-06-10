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
    variable_payoff = c(20000)
    use_timeout = True
    seconds_per_template = 10
    seconds_per_color = 10
    seconds_per_choice = 10
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
    
    # Configuracion las respuestas congruentes
    answers_c=     [
                        1, #1 -> True
                        0, #2 -> True
                        0, #3 -> True
                        1, #4 -> True
                        1, #5 -> True
                        0, #6 -> True
                        0, #7 -> True
                        1, #8 -> True
                        0, #9 -> True
                        0, #10 -> True
                        0, #11 -> True
                        1, #12 -> True
                        1, #13 -> True
                        0, #14 -> True
                        0, #15 -> True
                        0, #16 -> True
                        1, #17 -> True
                        0, #18 -> True
                        0, #19 -> True
                        0, #20 -> True
                        1, #21 -> True
                        1, #22 -> True
                        1, #23 -> True
                        1, #24 -> True
                    ]
    # Configuracion las respuestas INcongruentes
    answers_i=     [
                        0, #1 -> True
                        1, #2 -> True
                        1, #3 -> True
                        0, #4 -> True
                        0, #5 -> True
                        1, #6 -> True
                        1, #7 -> True
                        0, #8 -> True
                        1, #9 -> True
                        1, #10 -> True
                        1, #11 -> True
                        0, #12 -> True
                        0, #13 -> True
                        1, #14 -> True
                        1, #15 -> True
                        1, #16 -> True
                        0, #17 -> True
                        1, #18 -> True
                        1, #19 -> True
                        1, #20 -> True
                        0, #21 -> True
                        0, #22 -> True
                        0, #23 -> True
                        0, #24 -> True
                        ]

    for i in range(len(config_word)):
        t_dict = {"word": nombres_colores[config_word[i]], "word2": nombres_colores[config_color[i]], "word_color": lst_colors[config_word[i]], "color": lst_colors[config_color[i]], "left": type_left[i], "opc1": nombres_colores[config_left[i]], "opc2": nombres_colores[config_right[i]], "in_t7": "l"+str(i+1)}
        config_screens.append(t_dict)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number==1:
            for j in self.get_players():
                j.participant.vars['points'] = 0
                j.get_congruent()

        if self.round_number == 1:
            for p in self.get_players():
               #p.contract_pago = random.randint(1,4)
                p.participant.vars['orden_preguntas'] = json.dumps((np.random.choice(Constants.num_contracts, Constants.num_contracts, replace=False) + 1).tolist())
        #else:
            #for p in self.get_players():
                #p.contract_pago = p.in_round(1).pregunta_pago

    def set_id_players(self):
        for j in self.get_players():
            j.set_id()
    
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
    pago = models.CurrencyField()

    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')
    congruent = models.BooleanField() # Saber si es tratamiento congruente o no congruente el jugador

    correct =   models.IntegerField()  # correct answer stroop task
    points =   models.IntegerField()  # of correct answers

    pair1 = models.StringField()
    pair2 = models.StringField()
    pair3 = models.StringField()
    pair4 = models.StringField()


    def rellenar_campos(self, campo):
        for i in range(1, Constants.num_rounds+1):
            setattr(self.in_round(i), campo, getattr(self, campo))

    def get_congruent(self):
        self.congruent = random.choice([True, False])
        self.participant.vars['congruent'] = self.congruent
        return self.congruent

    def set_pago(self):
        if self.participant.vars['congruent'] == True:
            if int(self.left) == Constants.answers_c[self.round_number-1]:
                self.correct=1
            else:
                 self.correct=0
        else: 
            if int(self.left) == Constants.answers_i[self.round_number-1]:
                self.correct=1
            else:
                self.correct=0
        if self.correct==1: 
            if (self.round_number>4):
                self.participant.vars['points'] = self.participant.vars['points']+1
        self.points= self.participant.vars['points']

        if (self.round_number==Constants.num_rounds):
            answer_tasks = []
#            for j in self.in_all_rounds():
#                answer_tasks.append(j.left)
#            for k in range (5,24):
#                if self.participant.vars['congruent'] == True:
#                    if answer_tasks[k] == Constants.answers_c[k]:
#                        self.participant.vars['points'] = self.participant.vars['points']+1
#                else:
#                    if answer_tasks[k] == Constants.answers_i[k]:
#                        self.participant.vars['points'] = self.participant.vars['points']+1
            if self.participant.vars['points']>=16:
                self.pago= Constants.fixed_payoff + Constants.variable_payoff
            else:
                self.pago= Constants.fixed_payoff
            self.participant.vars['pagototal']=self.pago        
            

    def set_id(self):
            self.participant.vars['identificador'] = self.in_round(1).identificador


