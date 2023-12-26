import pv_calc




def create_payments(first_pay=None,
                    periodic_pay=None, n_periods=None,
                    last_pay=None, last_pay_distance=None):
    pays = ([first_pay]+[periodic_pay for i in range(n_periods)]
             + [last_pay])
    return pays





if __name__ =='__main__':

    # 36 month
    payments_36 = create_payments(first_pay=850, periodic_pay=20, n_periods=18
                                  ,last_pay=450.421)

    pv_calc.pv_calc(payments=payments_36, discount_rate=0.03)

    # 18 month
    payments_18 = create_payments(first_pay=550, periodic_pay=60, n_periods=9
                                  , last_pay=650.1)

    pv_calc.pv_calc(payments=payments_18, discount_rate=0.03)

    # 30 month
    payments_30 = create_payments(first_pay=750, periodic_pay=30, n_periods=15
                                  , last_pay=500.29)

    pv_calc.pv_calc(payments=payments_30, discount_rate=0.04)


    # Dey 1402, Kerman Motor
    # J4 36 month
    pv_calc.IRR_of_ghesti(765.89, 350, 48.1175, 12)

    # J4 48 month
    pv_calc.IRR_of_ghesti(765.89, 450, 30.2095, 16)

    # T8 48 month
    pv_calc.IRR_of_ghesti(1650, 700, 85.9097, 16)
