dollar = 'dollar'
euro = 'euro'
print('exchange rates hryvna to:')
exchange_rates = {dollar: 0.0258, euro: 0.0236}
print(exchange_rates)
hryvna = float(input('enter the amount of hryvnia: '))
currency = input('enter the currency to transfer: ').lower()
if currency == 'dollar':
    a = hryvna * exchange_rates[currency]
    print(a)
elif currency == 'euro':
    print(hryvna * exchange_rates[currency])
