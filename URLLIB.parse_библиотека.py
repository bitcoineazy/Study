import urllib.parse


strings = [
    'что такое backend',
    'Привет!',
    ' ',  # просто пробел
    'letiště',  # аэропорт по-чешски
    'München',  # крупнейший город Баварии
    'Champs-Élysées',  # Елисейские поля
    '東京',  # а это Токио, столица Японии  :)
]

for s in strings:
    encoded = urllib.parse.quote(s)  # зашифрованная строка
    decoded = urllib.parse.unquote(encoded)  # расшифрованная обратно строка
    print(decoded, '-', encoded)