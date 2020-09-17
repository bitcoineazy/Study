favorite_songs = {
    'Серёга': ["Unforgiven", "Holiday", "Highway to hell"],
    'Соня': ["Shake it out", "Don't stop me now", "Наше лето"],
    'Дима': ["Владимирский централ", "Мурка", "Третье сентября"]
}

# напишите код, который напечатает на экран, сколько у Димы любимых песен
print(len(favorite_songs['Дима']))
#for name, songs in favorite_songs.items():
#    if name == 'Дима':
#        for songs in favorite_songs['Дима']:
 #           i += 1

# здесь напишите код, который напечатает
# все любимые песни Сони через запятую и пробел ', '

print(', '.join(favorite_songs['Соня']))
#print(', '.join(favorite_songs.values()))