import pv_calc

periodic_payment = 8.2219
n_periods = 36
pv = 212.4
penalty = 0.7904287
prev_payments = 32.8876
payments_4_periods = 4*periodic_payment
total_payments = n_periods * periodic_payment
remained_total_payments = total_payments - prev_payments

nominal_total_interest = total_payments - pv

nominal_remained_interest = (32/36)*nominal_total_interest


r_real = pv_calc.periodic_IRR_calc(periodic_payment, n_periods, pv)

r_yearly_bank = 12 * r_real
to_pay = 207

# cash flow analysis
cash_flow = 4*[periodic_payment] + [0, to_pay]
x = pv_calc.pv_calc(payments=cash_flow, discount_rate=r_real)

# test

class Loan:
    def __init__(self, present_value=1, interest_rate=0, number_of_periods=1):
        self.pv = present_value
        self.ir = interest_rate
        self.n_periods = number_of_periods
        self.periodic_payment = pv_calc.periodic_payment_calc(pv=self.pv, n_periods=self.n_periods,
                                                              discount_rate=self.ir)

    def to_settle_payment(self, n_preiodic_payments_made, time_passed=None):
        if time_passed is None:
            time_passed = n_preiodic_payments_made

        pv_of_paid = pv_calc.periodic_pv_calc(self.periodic_payment, n_preiodic_payments_made, self.ir)
        pv_of_to_pay = self.pv - pv_of_paid
        pv_of_to_pay_today = pv_of_to_pay * (1+self.ir) ** time_passed
        return pv_of_to_pay_today


if __name__ == '__main__':
    sd_loan = Loan(present_value=pv, interest_rate=r_real, number_of_periods=n_periods)
    x = sd_loan.to_settle_payment(4, 5.33)
    y = sd_loan.to_settle_payment(4, 4)














