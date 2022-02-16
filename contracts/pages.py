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
    form_fields = ['c1']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 1

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c2(Page):
    form_model = 'player'
    form_fields = ['c2']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 2

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 
    

class c3(Page):
    form_model = 'player'
    form_fields = ['c3']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 3

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c4(Page):
    form_model = 'player'
    form_fields = ['c4']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 4

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c5(Page):
    form_model = 'player'
    form_fields = ['c5']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 5

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c6(Page):
    form_model = 'player'
    form_fields = ['c6']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 6

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c7(Page):
    form_model = 'player'
    form_fields = ['c7']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 7

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c8(Page):
    form_model = 'player'
    form_fields = ['c8']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 8

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c9(Page):
    form_model = 'player'
    form_fields = ['c9']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 9

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c10(Page):
    form_model = 'player'
    form_fields = ['c10']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 10

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c11(Page):
    form_model = 'player'
    form_fields = ['c11']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 11

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c12(Page):
    form_model = 'player'
    form_fields = ['c12']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 12

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c13(Page):
    form_model = 'player'
    form_fields = ['c13']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 13

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c14(Page):
    form_model = 'player'
    form_fields = ['c14']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 14

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c15(Page):
    form_model = 'player'
    form_fields = ['c15']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 15

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0]) 

class c16(Page):
    form_model = 'player'
    form_fields = ['c16']
    
    def is_displayed(self):
        return json.loads(self.participant.vars['orden_preguntas'])[self.round_number-1] == 16

    def before_next_page(self):
        self.player.rellenar_campos(self.form_fields[0])

class ResultsWaitPage(WaitPage):
    pass


class Comparacion(Page):
    pass


page_sequence = [consent, Instrucciones]
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

# random.shuffle(preguntas)

for p in preguntas:
    page_sequence.append(p)

