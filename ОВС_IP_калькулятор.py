from ipaddress import IPv4Address
class MyIPv4(IPv4Address):
    def __and__(self, other: IPv4Address):
        if not isinstance(other, (int, IPv4Address)):
            raise NotImplementedError
        return self.__class__(int(self) & int(other))
try:
    addr = MyIPv4(input('Введите IP адрес: '))
    mask = MyIPv4(input('Введите маску подсети: '))
    print('Ваш адрес сети: ', addr & mask)
except:
    print('Вы ввели неправильный адрес')
