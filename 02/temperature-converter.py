def helpPrint():
    print "K - Kelvin"
    print "C - Celsius"
    print "F - Fahrenheit"

def calculate(_from, _to, temp):
    if _from == 'K':
        if _to == 'C':
            temperature = float(temp) - 273.15
        if _to == 'F':
            temperature = float(((float(temp) - 273.15) * float(9 / 5)) + 32)
    elif _from == 'C':
        if _to == 'K':
            temperature = float(temp) + 273.15
        if _to == 'F':
            temperature = (float(temp) * float(9/5)) + 32
    elif _from == 'F':
        if _to == 'K':
            temperature = (float(temp) - 32) * float(5/9) + 273.15
        if _to == 'C':
            temperature = (float(temp) - 32) * float(5/9)
    else:
        print "Wrong parameter"
        return
    return temperature

helpPrint()
_from = raw_input('From: ')
_to = raw_input('To: ')
_temperature = raw_input('Temperature: ')
_from = _from[0]
_to = _to[0]
print calculate(_from, _to, _temperature)
