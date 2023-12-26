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












