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


class contracts(Page):
    form_model = 'player'
    form_fields = ['n_round', 'n_contract', 'choice', 'choice_time', 'list_choice', 'list_time_choice']

    def vars_for_template(self):
        number_contract = int(self.participant.vars['orden_preguntas'][1:-1].split(', ')[self.subsession.round_number - 1])
        c_c = Constants.contracts.get(number_contract)
        config_contract = {"number": number_contract, "paymnet": c_c[0], "insurance": c_c[1], "percentage": int(100*c_c[1]/c_c[0]), "alone": c_c[2], "bonusrelative": c_c[3]}
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
            "seconds_per_template": Constants.seconds_per_template
        }


class screen2(Page):
    def vars_for_template(self):
        return {
            "seconds_per_template": Constants.seconds_per_template
        }


class screen3(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens_c[index_config]
        return {
            "config_screen": config_screen,
            "congruent": self.participant.vars['congruent'],
            "seconds_per_template": Constants.seconds_per_template
        }


class screen5(Page):
    def vars_for_template(self):
        return {
            "seconds_per_template": Constants.seconds_per_template
        }


class screen6(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens_c[index_config]
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
        config_screen = Constants.config_screens_c[index_config]
        return {
            "config_screen": config_screen,
            "seconds_per_contract": Constants.seconds_per_contract
        }


page_sequence = [screen3, screen6]

