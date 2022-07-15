def genwords():
    yield('hello')
    yield('world')
    yield('foo')
    yield('bar')
    
    
if __name__ == '__main__':
    x = genwords()
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    #print(next(x)) <= Fehler!
