# Нужно рассмотреть больше случаев в if-elif-else
for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif remainder == 1 and messages_count % 100 != 11: # напишите ваш код здесь
        print('У вас', str(messages_count),'новое сообщение')
    elif messages_count % 100 == 11:
        print('У вас', str(messages_count), 'новых сообщений')
    elif (1 < remainder <= 9 or remainder == 0) and 10 < messages_count < 20:
        print('У вас', str(messages_count),'новых сообщений')
    elif messages_count > 20 and (1 < remainder < 5):
        print('У вас', str(messages_count), 'новых сообщения')
    elif messages_count > 20 and (5 <= remainder <= 9):
        print('У вас', str(messages_count), 'новых сообщений')
    elif messages_count < 10 and (1 < remainder < 5):
        print('У вас', str(messages_count),'новых сообщения')
    elif messages_count < 10 and (5 <= remainder <= 9):
        print('У вас', str(messages_count), 'новых сообщений')
    elif remainder == 0:
        print('У вас', str(messages_count), 'новых сообщений')