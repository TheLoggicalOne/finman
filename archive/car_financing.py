import numpy as np
import pandas as pd
import itertools
import random
from functools import partial


#---------------------------------------------USEFUL FUNCTIONS--------------------------------------------------------#

def pv_calc(payments, discount_rate=0.01, rest=1):
    pv = 0
    for period, payment in enumerate(payments):
        pv += payment / (1 + discount_rate) ** (period + rest)
    return pv


def periodic_pv_calc(periodic_payment, n_periods, rest, discount_rate):
    return pv_calc(n_periods * [periodic_payment], discount_rate, rest)


def Ghest_calc(pv, n_periods, discount_rate, rest=1):
    return pv / periodic_pv_calc(1, n_periods, rest, discount_rate)


def bazar_ghest_calc(pv, n_periods, discount_rate, rest=1):
    g = (pv + (n_periods + rest - 1) * discount_rate * pv) / n_periods
    return (n_periods * g, n_periods, g)


def bazar_IRR_calc(cash_price, pre_pay, periodic_payment, n_periods, rest=1):
    loan = cash_price - pre_pay
    repay = n_periods * periodic_payment
    irr = (repay - loan) / (loan * (n_periods + rest - 1))
    return irr


def IRR_calc(payments, present_value, error=10 ** (-6), rest=1):
    irr = 0
    while pv_calc(payments, irr, rest) > present_value:
        irr += error
    return 100 * irr


def periodic_IRR_calc(periodic_payment=1, n_periods=1, present_value=1, error=10 ** (-6), rest=1):
    return IRR_calc(n_periods * [periodic_payment], present_value, error, rest)


def IRR_of_ghesti(cash_price, pre_pay, periodic_payment, n_periods, error=10 ** (-6), rest=1):
    present_value = cash_price - pre_pay
    return periodic_IRR_calc(periodic_payment, n_periods, present_value, error, rest)

#----------------------------------------------------------------------------------------------------------------------#


IR_GHESTI = [0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06]
DR = IR_GHESTI


class Payment_Plan:

    def __init__(self, cash_price, pre_pay=0, periodic_payment=None, n_periods=None, period_length=1,
                 discount_rate=0.03, ir=0.04, ir_ghesti=0.035, error=10 ** (-6), rest=1):
        self.cash_price = cash_price
        self.pre_pay = pre_pay
        self.periodic_payment = periodic_payment
        self.n_periods = n_periods
        self.period_length = period_length
        self.error = error
        self.rest = rest
        self.discount_rate = discount_rate
        self.ir = ir
        self.ir_ghesti = ir_ghesti
        self.loan = self.cash_price - self.pre_pay
        self.ghesti_pp = {x: (self.bazar_ghest_calc(r=x), self.pv_of_bazar_ghest(r=x)) for x in IR_GHESTI}

    def periodic_pv_calc(self, rest=None, discount_rate=None):
        if rest is None:
            rest = self.rest

        if discount_rate is None:
            discount_rate = self.discount_rate

        return pv_calc(self.n_periods * [self.periodic_payment], discount_rate, rest)

    def IRR_of_ghesti(self, rest=None):
        if rest is None:
            rest = self.rest

        present_value = self.cash_price - self.pre_pay
        er = self.error
        re = self.rest
        return periodic_IRR_calc(self.periodic_payment, self.n_periods, present_value,
                                 error=er, rest=re)


    def bazar_ghest_calc(self, n_periods=None, r=None, rest=None):
        if rest is None:
            rest = self.rest

        if r is None:
            r = self.ir_ghesti

        if n_periods is None:
            n_periods = self.n_periods

        pv = self.cash_price - self.pre_pay

        g = (pv + (n_periods + rest - 1) * r * pv) / n_periods
        return (n_periods * g, n_periods, g)

    def bazar_IRR_calc(self, periodic_payment=None, n_periods=None, rest=None):
        if periodic_payment is None:
            periodic_payment = self.periodic_payment

        if n_periods is None:
            n_periods = self.n_periods

        if rest is None:
            rest = self.rest
        loan = self.cash_price - self.pre_pay
        repay = n_periods * periodic_payment
        irr = (repay - loan) / (loan * (n_periods + rest - 1))
        return irr

    def pv_of_bazar_ghest(self, n_periods=None, r=None, rest=None, discount_rate=None):

        if rest is None:
            rest = self.rest

        if r is None:
            r = self.ir_ghesti

        if n_periods is None:
            n_periods = self.n_periods

        if discount_rate is None:
            discount_rate = self.discount_rate

        pv = self.cash_price - self.pre_pay

        g = self.bazar_ghest_calc(n_periods, r, rest)[-1]
        bpv = periodic_pv_calc(g, n_periods, rest, discount_rate)
        profit = bpv - pv
        profit_ratio = (profit / pv - 1)
        real_price = self.pre_pay + bpv
        return bpv, bpv/pv


if __name__ == '__main__':
    # loan500 = Payment_Plan(500, n_periods=6)
    PERIODS = [1, 2, 3, 4, 5, 6, 8, 10, 12,15, 18, 24, 36]
    pp0 = Payment_Plan(1450, 800, 47.4, 24)
    loan500 = {n: Payment_Plan(500, n_periods=n) for n in PERIODS}

    AREA = 185
    PRICE = 75
    TOTAL_PRICE = AREA * PRICE
    PSANAD_PERCENT = 0.1
    PREPAY0 = 8500
    PREPAY1 = 4160

    NP = 30
    mp0 = (TOTAL_PRICE-PSANAD_PERCENT*TOTAL_PRICE - PREPAY0)/NP
    mp1 = (TOTAL_PRICE - PSANAD_PERCENT * TOTAL_PRICE - PREPAY1) / NP
    pv0 = periodic_pv_calc(mp0, NP, 1, 0.03)
    pv1 = periodic_pv_calc(mp1, NP, 1, 0.03)


    sanad_per_meter = PSANAD_PERCENT*TOTAL_PRICE/AREA

    ghesti = 150*0.30
    ghest = Ghest_calc(ghesti, 36, 0.18/12)
    periodic_pv_calc(ghest, 36, 1, 0.03)
    ghest_5 = Ghest_calc(ghesti, 60, 0.18 / 12)
    ghest_10 = Ghest_calc(ghesti, 120, 0.18 / 12)




