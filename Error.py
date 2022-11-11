class ValueHighError(Exception):
    pass

class ValueLowError(Exception):
    pass

def testValue(x):
    if x > 1000:
        raise ValueHighError('value is high')
    if x < 5:
        raise ValueLowError('value is low')
    
try:
    testValue(100000)
except ValueHighError as e:
    print(e)
except ValueLowError as e:
    print(e)
else:
    print("No error")


