import datetime as dt

class Record:
    date_format = '%d.%m.%Y'
    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = amount
        self.comment = comment
        if not isinstance(date, dt.date):
            self.date = dt.datetime.strptime(date, self.date_format).date()
        else:
            self.date = date
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_time(self, days_cnt):
        amount_days = 0
        past = dt.date.today() - dt.timedelta(days = days_cnt)
        today = dt.date.today()
        for values in self.records:
            if past < values.date <= today:
                amount_days += values.amount
        return amount_days

    def get_today_stats(self):
        return self.get_time(1)
    def get_week_stats(self):
        return self.get_time(7)


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        potratil = self.get_today_stats()
        left = self.limit - potratil
        if left > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {left} кКал'
        else:
            return 'Хватит есть!'



class CashCalculator(Calculator):
    USD_RATE = 77.23
    EURO_RATE = 90.74
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        potratil = self.get_today_stats()
        left = self.limit - potratil

        if left == 0:
            return 'Денег нет, держись'

        all_currency = {
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro'),
            'rub': (self.RUB_RATE, 'руб')
        }
        currency_out = f'{round(abs(left) / all_currency[currency][0], 2)} {all_currency[currency][1]}'


        if left < 0:
            return (f'Денег нет, держись: твой долг - {currency_out}')

        return (f'На сегодня осталось {currency_out}')

cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained('rub'))
# должно напечататься
# На сегодня осталось 555 руб
