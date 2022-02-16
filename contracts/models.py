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
    seconds_per_tasks1 = 10
    seconds_per_contract = 20
    #date_activity1 =
    #date_activity2 =

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

    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')


    contract_pago = models.IntegerField()
    #pago = models.CurrencyField(initial=0)

    def rellenar_campos(self, campo):
        for i in range(1, Constants.num_rounds+1):
            setattr(self.in_round(i), campo, getattr(self, campo))

#    tasks

