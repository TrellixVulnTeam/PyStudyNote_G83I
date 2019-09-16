class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass
def raiser0():
    x=General()
    raise x
def raiser1():
    x=Specific1()
    raise  x
def raiser2():
    x=Specific2()
    raise x

for f in (raiser0,raiser1,raiser2):
    try:
        f()
    except General:
        import sys
        print('caught:',sys.exc_info()[0])

