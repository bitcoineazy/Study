
def foo():
    """foo()"""
    return 'something'

def bar():
    """bar()"""
    return 'anything'

def baz():
    """baz()"""
    return 'sert'

def sk(s):
    """sk(*s)"""
    z=''
    for el in s:
        z+=el
    return z

def br(length=5):
    """(расстояние=5)"""
    return f'Предмет брошен на расстояние={length}'
f_names = (foo,bar,baz,sk,br)

def names2dict(*f_nm):
    return {func.__name__: f'<function __main__.{func.__doc__}' for func in f_nm}

func_dict = names2dict(*f_names)
print(func_dict)


def repl(f_dict):
    for each in f_dict.items():
        print(each)

def repl_mod(input):
    elements = input.split(' ')
    elements.remove('СКЛЕИТЬ')
    print(''.join(elements))


repl(func_dict)
repl_mod(input())