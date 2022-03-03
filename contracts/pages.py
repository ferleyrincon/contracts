import random
import json

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

    def is_displayed(self):
        return self.round_number == 1


class Instrucciones(Page):
    def is_displayed(self):
        return self.round_number == 1


class c1(Page):
    form_model = 'player'
    form_fields = ['c1', 't1', 'adc1', 'atc1']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 1
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c2(Page):
    form_model = 'player'
    form_fields = ['c2', 't2', 'adc2', 'atc2']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 2
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 
    

class c3(Page):
    form_model = 'player'
    form_fields = ['c3', 't3', 'adc3', 'atc3']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 3
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c4(Page):
    form_model = 'player'
    form_fields = ['c4', 't4', 'adc4', 'atc4']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 4
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c5(Page):
    form_model = 'player'
    form_fields = ['c5', 't5', 'adc5', 'atc5']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 5
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c6(Page):
    form_model = 'player'
    form_fields = ['c6', 't6', 'adc6', 'atc6']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 6
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c7(Page):
    form_model = 'player'
    form_fields = ['c7', 't7', 'adc7', 'atc7']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 7
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c8(Page):
    form_model = 'player'
    form_fields = ['c8', 't8', 'adc8', 'atc8']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 8
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c9(Page):
    form_model = 'player'
    form_fields = ['c9', 't9', 'adc9', 'atc9']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 9
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c10(Page):
    form_model = 'player'
    form_fields = ['c10', 't10', 'adc10', 'atc10']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 10
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c11(Page):
    form_model = 'player'
    form_fields = ['c11', 't11', 'adc11', 'atc11']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 11
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c12(Page):
    form_model = 'player'
    form_fields = ['c12', 't12', 'adc12', 'atc12']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 12
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c13(Page):
    form_model = 'player'
    form_fields = ['c13', 't13', 'adc13', 'atc13']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 13
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c14(Page):
    form_model = 'player'
    form_fields = ['c14', 't14', 'adc14', 'atc14']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 14
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c15(Page):
    form_model = 'player'
    form_fields = ['c15', 't15', 'adc15', 'atc15']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 15
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 


class c16(Page):
    form_model = 'player'
    form_fields = ['c16', 't16', 'adc16', 'atc16']
    '''
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 16
    '''
    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])


class ResultsWaitPage(WaitPage):
    pass


class Comparacion(Page):
    pass


class config_screens(Page):
    pass


class screen1(Page):
    pass


class screen2(Page):
    pass


class screen3(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens_c[index_config]
        return {
            "config_screen": config_screen
        }


class screen5(Page):
    pass


class screen6(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens_c[index_config]
        return {
            "config_screen": config_screen
        }


class screen7(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens_c[index_config]
        return {
            "config_screen": config_screen
        }


page_sequence = [screen1, screen2, screen3]

preguntas = [
        c1,
        c2,
        c3,
        c4,
        c5,
        c6,
        c7,
        c8,
        c9,
        c10,
        c11,
        c12,
        c13,
        c14,
        c15,
        c16
]

for p in preguntas:
    page_sequence.append(p)

page_sequence += [screen5, screen6, screen7]

