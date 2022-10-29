def mapInput(value):
    if value == 'x':
        return 1
    if value == 'o':
        return 2

    return 3
    
def mapOutput(roundedValue):
    if roundedValue == 1:
        return 'Gana X'

    return 'Gana O'