from decimal import Decimal
import requests
import json
from config import config

class ConvertionException(Exception):
    pass

class CurrencyConvertor:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        try:
            base_ticker = config.currency[base]
        except Exception:
            raise ConvertionException(f"Введёная валюта {base} не найдена в списке доступных. \n\
        Проверьте правильность ввода.")
        try:
            quote_ticker = config.currency[quote]
        except Exception:
            raise ConvertionException(f"Введёная валюта {quote} не найдена в списке доступных. \n\
        Проверьте правильность ввода.")


        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}")
        total_base = json.loads(r.content)[quote_ticker]
        try:
            Decimal(amount)
        except Exception as e:
            raise ConvertionException(f"Введёное количество валюты не распознано. \n\
        Проверьте правильность ввода.")

        cost = Decimal(amount) * Decimal(total_base)
        result = f"Стоимость {amount} {base} в {quote} равна {cost.quantize(Decimal("0.01"))}"
        return result

