from decimal import Decimal
import requests
import json

currency = {'Доллар': 'USD',
        'Евро': 'EUR',
        'Рубль': 'RUB'}

class RequestException(Exception):
    pass

class ConvertionException(Exception):
    pass

class RequestResponse:
    def get_price(self, base, quote, amount):
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={currency[base]}&tsyms={currency[quote]}")
        print(r.content)
        total_base = json.loads(r.content)[currency[quote]]
        cost = Decimal(amount) * Decimal(total_base)
        result = f"Стоимость {amount} {base} в {quote} равна {cost.quantize(Decimal("0.01"))}"
        return result

