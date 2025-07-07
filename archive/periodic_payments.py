import pv_calc




class PaymentPlan:
    def __init__(self, present_value=None, n_periods=None,  periodic_pay=None, interest_rate=None,
                 nosoul_rate=None,
                 rest=1, error=10**(-6)):
        self.pv = present_value
        self.n_periods = n_periods
        self.periodic_pay = periodic_pay
        self.interest_rate = interest_rate
        self.nosoul_rate = nosoul_rate
        self.rest = rest
        self.error = error







pv_calc.oldbank_periodic_payment_calc(100, 5, 0.03)










