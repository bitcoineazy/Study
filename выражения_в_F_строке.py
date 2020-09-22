def calc_stat(listened):  # от англ. calculate statistics, посчитать статистику
    N = len(listened)
    M = sum(listened)//60
    S = sum(listened)%60
    return f'Вы прослушали {N} песен, общей продолжительностью {M} минут и {S} секунд.'

# напишите код функции calc_stat


print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))