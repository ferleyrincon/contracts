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

class answer_practice(Page):
    def is_displayed(self):
        return self.round_number <= 4
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens[index_config]
        return {
            "config_screen": config_screen,
            "congruent": self.participant.vars['congruent'],
            "time": Constants.seconds_per_color1
        }

class instructions_contracts(Page):
    def is_displayed(self):
        return self.round_number == 5

class instructions_pairs(Page):
    def is_displayed(self):
        return self.round_number == 20


class contracts1(Page):
    def is_displayed(self):
        return self.round_number > 4

    def vars_for_template(self):
        number_contract = int(self.participant.vars['orden_preguntas'][1:-1].split(', ')[self.subsession.round_number])
        c = Constants.contracts.get(number_contract)
        config_contract = {"number": number_contract, "payment": c[0], "insurance": c[1], "percentage": int(100*c[1]/c[0]), "alone": c[2], "bonusrelative": c[3]}
        return {
            "config_contract": config_contract,
            "time": Constants.seconds_per_choice
        }

class contracts2(Page):
    form_model = 'player'
    form_fields = ['n_round', 'n_contract', 'choice', 'choice_time', 'list_choice', 'list_time_choice']

    def is_displayed(self):
        return self.round_number > 4

    def vars_for_template(self):
        number_contract = int(self.participant.vars['orden_preguntas'][1:-1].split(', ')[self.subsession.round_number])
        c = Constants.contracts.get(number_contract)
        config_contract = {"number": number_contract, "payment": c[0], "insurance": c[1], "percentage": int(100*c[1]/c[0]), "alone": c[2], "bonusrelative": c[3]}
        return {
            "config_contract": config_contract,
            "time": Constants.seconds_per_choice
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
            "time": Constants.seconds_per_template,
            "round": self.subsession.round_number - 4
        }


class screen2(Page):
    def vars_for_template(self):
        return {
            "time": Constants.seconds_per_template
        }


class screen3(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens[index_config]
        return {
            "config_screen": config_screen,
            "congruent": self.participant.vars['congruent'],
            "time": Constants.seconds_per_color1
        }


class screen6(Page):
    def is_displayed(self):
        return self.round_number > 4

    def vars_for_template(self):
        return {
            "time": Constants.seconds_per_template
        }


class screen7(Page):
    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens[index_config]
        return {
            "config_screen": config_screen,
            "congruent": self.participant.vars['congruent'],
            "time": Constants.seconds_per_color2
        }


class screen8(Page):
    form_model = 'player'
    form_fields = ['left', 'left_time']

    def vars_for_template(self):
        index_config = int(self.subsession.round_number - 1)
        config_screen = Constants.config_screens[index_config]
        return {
            "config_screen": config_screen,
            "time": Constants.seconds_per_choice
        }


page_sequence = [consent, welcome1, welcome2, instructions_task, instructions_contracts, screen1, screen2, screen3, contracts1, contracts2, screen6, screen7, screen8, answer_practice]

#page_sequence = [screen1, screen2, screen3, contracts, screen5, screen6, screen7, answer_practice]
