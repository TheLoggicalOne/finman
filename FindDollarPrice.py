MIN_PRICE = 51500
MAX_PRICE = 52500
TOTAL_PRICE = 54_040_000
price_numbers = []
ERROR = 5000
for price in range(51500,52500, 5):
    if TOTAL_PRICE-(TOTAL_PRICE//price)*price < ERROR:
        price_numbers.append([price, TOTAL_PRICE//price, TOTAL_PRICE-(TOTAL_PRICE//price)*price])
