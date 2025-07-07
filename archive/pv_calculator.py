import numpy as np
import pandas as pd


def pv_calc(payments, discount_rate=0.01, rest=1):
    pv = 0
    for period, payment in enumerate(payments):
        pv += payment/(1+discount_rate)**(period + rest)
    return pv


def periodic_pv_calc(periodic_payment, n_periods, discount_rate, rest=1):
    return pv_calc(n_periods*[periodic_payment], discount_rate, rest)


def Ghest_calc(pv, n_periods, discount_rate):
    return pv/periodic_pv_calc(1, n_periods, discount_rate)


def IRR_calc(payments, present_value, error=10**(-6), rest=1):
    irr = 0
    while pv_calc(payments, irr, rest) > present_value:
        irr += error
    return irr


def periodic_IRR_calc(periodic_payment=1, n_periods=1, present_value=1, error=10**(-6), rest=1):
    return IRR_calc(n_periods * [periodic_payment], present_value, error, rest)


def IRR_of_ghesti(cash_price, pre_pay, periodic_payment, n_periods, error=10**(-6), rest=1):
    present_value = cash_price-pre_pay
    return periodic_IRR_calc(periodic_payment, n_periods, present_value, error, rest)


if __name__ == '__main__':

    # PERIODS = [5, 10, 20]
    # PRE_PAYS = [0.3, 0.45, 0.55]
    # DISCOUNTS = [0.88, 0.9, 1]
    # cp = 1
    # gp = 1.25
    # n = 3

    # for i in range(n):
    #     prepay = gp*PRE_PAYS[i]*DISCOUNTS[i]
    #     periodicpayment = (gp*DISCOUNTS[i]-prepay)/PERIODS[i]
    #     print(IRR_of_ghesti(cp, prepay, periodicpayment, PERIODS[i]))

    # Shahr Loan

    R = (23/12)/100

    PERIODS = [12, 24, 30, 36, 48]
    LoanToAv = [0.944, 0.514, 0.424, 0.364, 0.288]
    GHESTS = 5*[np.nan]
    PAYMENTS = 5*[np.nan]









