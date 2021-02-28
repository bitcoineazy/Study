from ipaddress import IPv4Address
class MyIPv4(IPv4Address):
    def __and__(self, other: IPv4Address):
        if not isinstance(other, (int, IPv4Address)):
            raise NotImplementedError
        return self.__class__(int(self) & int(other))

MyIPv4("220.14.9.37").binary_repr()

