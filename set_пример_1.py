bands = ['Пикник', 'Ария', 'Блестящие', 'Блестящие']
# получаем сет unique_band_names (с англ. «уникальные названия групп»)
unique_band_names = set(bands)
for band in unique_band_names:
    print('Доктор, я не могу больше слушать группу ' + band)