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

class welcome1(Page):
    def is_displayed(self):
        return self.round_number == 1

class welcome2(Page):
    form_model = 'player'
    form_fields = ['identificador']

    def is_displayed(self):
        return self.round_number == 1

class instructions_task(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            "congruent": self.participant.vars['congruent'],
        }

class practice_answer(Page):
    def is_displayed(self):
        return self.round_number < 4
    def vars_for_template(self): 
        return {
            "p_practice" : self.participant.vars['p_practice'],
        }

class instructions_contracts(Page):
    def is_displayed(self):
        return self.round_number == 4

class instructions_pairs(Page):
    def is_displayed(self):
        return self.round_number == 20


class contracts(Page):
    form_model = 'player'
    form_fields = ['n_round', 'n_contract', 'choice', 'choice_time', 'list_choice', 'list_time_choice']

    def is_displayed(self):
        return self.round_number > 4

    def vars_for_template(self):
        number_contract = int(self.participant.vars['orden_preguntas'][1:-1].split(', ')[self.subsession.round_number - 4])
        c = Constants.contracts.get(number_contract)
        config_contract = {"number": number_contract, "paymnet": c[0], "insurance": c[1], "percentage": int(100*c[1]/c[0]), "alone": c[2], "bonusrelative": c[3]}
        return {
            "config_contract": config_contract,
            "seconds_per_contract": Constants.seconds_per_contract
        }


class ResultsWaitPage(WaitPage):
    pass


class Comparacion(Page):
    pass


class config_screens(Page):
    pass


class screen1(Page):
    def vars_for_template(self):
        return {
            "congruent": self.participant.vars['congruent'],
            "seconds_per_template": Constants.seconds_per_template,
            "round": self.subsession.round_number - 4
        }


class screen2(Page):
    def vars_for_template(self):
        return {
            "seconds_per_template": Constants.seconds_per_template
        }


class screen3(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens[index_config]
        return {
            "config_screen": config_screen,
            "congruent": self.participant.vars['congruent'],
            "seconds_per_template": Constants.seconds_per_template
        }


class screen5(Page):
    def is_displayed(self):
        return self.round_number > 4

    def vars_for_template(self):
        return {
            "seconds_per_template": Constants.seconds_per_template
        }


class screen6(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens[index_config]
        return {
            "config_screen": config_screen,
            "congruent": self.participant.vars['congruent'],
            "seconds_per_template": Constants.seconds_per_template
        }


class screen7(Page):
    form_model = 'player'
    form_fields = ['left', 'left_time']

    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens[index_config]
        return {
            "config_screen": config_screen,
            "seconds_per_contract": Constants.seconds_per_contract
        }


page_sequence = [consent, welcome1, welcome2, instructions_task, instructions_contracts, screen1, screen2, screen3, contracts, screen5, screen6, screen7, practice_answer]

