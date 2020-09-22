def check_query(query):
    request = (query.split())
    if request[-1] == 'друзей?':
        return ' '.join(request[1:])
    elif request[-1] == 'был?':
        return ' '.join(request[1:])
    elif request[-1] == 'скорей!':
        return ' '.join(request[1:])
    return ' '.join(request[1:])

# дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '-', result)