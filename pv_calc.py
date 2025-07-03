import numpy as np
import pandas as pd



def convert_ir(ir, from_period_length, to_period_length):
    return (1+ir)**(to_period_length/from_period_length)-1
#----------------------------------------------------------------------------------------------------------------------#
#--------------------------------The right way: present value way------------------------------------------------------#


def create_payments(first_pay=None,
                    periodic_pay=None, n_periods=None,
                    last_pay=None, last_pay_distance=None):
    pays = ([first_pay]+[periodic_pay for i in range(n_periods)]
             + [last_pay])
    return pays

def pv_calc(*, payments=None, discount_rate=0.01, rest=1):
    pv = 0
    for period, payment in enumerate(payments):
        pv += payment/(1+discount_rate)**(period + rest)
    return pv


def periodic_pv_calc(periodic_payment=None, n_periods=None, discount_rate=None, rest=1):
    return pv_calc(payments=n_periods*[periodic_payment], discount_rate=discount_rate, rest=rest)


def periodic_payment_calc(pv=None, n_periods=None, discount_rate=None):
    return pv/periodic_pv_calc(periodic_payment=1, n_periods=n_periods, discount_rate=discount_rate)


def IRR_calc(payments=None, present_value=None, error=10**(-6), rest=1):
    irr = 0
    while pv_calc(payments=payments, discount_rate=irr, rest=rest) > present_value:
        irr += error
    return irr


# def IRR_calc_improved(payments=None, present_value=None, error=10**(-6), rest=1):
#     irr = 0
#     f = pv_calc(payments=payments, discount_rate=irr, rest=rest) - present_value
#     normality = f > 0
#     for irr
#     while pv_calc(payments=payments, discount_rate=irr, rest=rest) > present_value:
#         irr += 0.1



def periodic_IRR_calc(periodic_payment=1, n_periods=1, present_value=1, error=10**(-6), rest=1):
    return IRR_calc(payments=n_periods * [periodic_payment], present_value=present_value,
                    error=error, rest=rest)


def IRR_of_ghesti(cash_price=None, down_payments=None, periodic_payment=None,
                  n_periods=None, error=10 ** (-6), rest=1):
    present_value = cash_price - down_payments
    return periodic_IRR_calc(periodic_payment=periodic_payment,
                             n_periods=n_periods, present_value=present_value, error=error, rest=rest)

#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------OLDBANK, OLD WISE MAN --------------------------------------------------------#


def oldbank_periodic_payment_calc(pv=1, n_periods=None, discount_rate=None):
    return (pv + pv * discount_rate * ((n_periods + 1) / 2)) / n_periods


def oldbank_periodic_IR_calc(periodic_payment=1, n_periods=1, present_value=1, error=10**(-6), rest=1):
    tp_over_pv = n_periods*periodic_payment/present_value
    adj_n = (n_periods+1)/2
    return (tp_over_pv-1)/adj_n


def oldbank_pv_calc(periodic_payment=None, n_periods=None, discount_rate=None, rest=1):
    effective_discount = 1 + discount_rate*(n_periods+1)/2
    tp = periodic_payment*n_periods
    return tp/effective_discount



#----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------NO MORAL WAY, NO RAAS, GHESTI KOSKESH ------------------------------------------#



def nomoral_periodic_payment_calc(pv=1, n_periods=None, discount_rate=None):
    return (pv + pv * discount_rate * n_periods) / n_periods


def nomoral_periodic_IR_calc(periodic_payment=1, n_periods=1, present_value=1, error=10**(-6), rest=1):
    tp_over_pv = n_periods*periodic_payment/present_value
    return (tp_over_pv-1)/n_periods


def nomoral_pv_calc(periodic_payment=None, n_periods=None, discount_rate=None, rest=1):
    effective_discount = 1 + discount_rate*n_periods
    tp = periodic_payment*n_periods
    return tp/effective_discount


#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
def real_interest_of_nomoral_payment(pv=1, n_periods=None, discount_rate=None):
    m = nomoral_periodic_payment_calc(pv=pv, n_periods=n_periods, discount_rate=discount_rate)
    return periodic_IRR_calc(periodic_payment=m, n_periods=n_periods, present_value=pv, error=10 ** (-6), rest=1)


def oldbank_interest_of_nomoral_payment(pv=1, n_periods=None, discount_rate=None):
    m = nomoral_periodic_payment_calc(pv=pv, n_periods=n_periods, discount_rate=discount_rate)
    return oldbank_periodic_IR_calc(periodic_payment=m, n_periods=n_periods, present_value=pv, error=10 ** (-6), rest=1)


def real_interest_of_oldbank_payment(pv=1, n_periods=None, discount_rate=None):
    m = oldbank_periodic_payment_calc(pv=pv, n_periods=n_periods, discount_rate=discount_rate)
    return periodic_IRR_calc(periodic_payment=m, n_periods=n_periods, present_value=pv, error=10 ** (-6), rest=1)

#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#


def folk_pv_calc(*, payments=None, discount_rate=0.01, rest=1):
    pv = 0
    for period, payment in enumerate(payments):
        pv += payment/(1+discount_rate**(period + rest))
    return pv



def folk_periodic_pv_calc(periodic_payment=None, n_periods=None, discount_rate=None, rest=1):
    return folk_pv_calc(payments=n_periods*[periodic_payment], discount_rate=discount_rate, rest=rest)



def folk_periodic_payment_calc(pv=1, n_periods=None, discount_rate=None):
    return pv/folk_periodic_pv_calc(periodic_payment=1, n_periods=n_periods, discount_rate=discount_rate)

# ----------------------------------------------------------------------------------------------------------

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

    PIP = 0.001
    real_interest_of_nomoral_payment(100, 4, 0.03)
    rear_rs = [(PIP*i,real_interest_of_nomoral_payment(100, 4, PIP*i )) for i in range(1,100)]
    rs = np.array(rear_rs)
    ratio_of_rs = (rs[:, 1] / rs[:, 0])
    ratio_of_rs = ratio_of_rs[:, np.newaxis]
    rs_of_nomoral_vs_real = np.concatenate((rs, ratio_of_rs), axis=1)


    oldbank_interest_of_nomoral_payment(100, 4, 0.03)

    real_interest_of_oldbank_payment(100, 4, 0.048)


