'''import hashlib

input = 'Gasdj cxzcxz cxzdsqwe'
hashed = hashlib.sha256(input.encode('UTF-8')).hexdigest()'''
from collections import defaultdict

def load_words(filename=r'C:\Users\79268\Dev\csvs\zdf-win.txt'):
    with open(filename) as f:
        for word in f:
            yield word.rstrip()

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def anagrams(word_source):
    d = get_anagrams(word_source)
    return d

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

            
word_source = load_words()
#print(anagrams(word_source))
permutations('слово', anagrams(word_source))



