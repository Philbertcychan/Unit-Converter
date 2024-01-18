"""
This program will be able to convert units from the metric scale (1 - millimeter, 2 - centimeter, 3 - meter, 
4 - kilometer) to any other unit in the metric scale. Made this without looking at code beforehand :). 
"""
def makeWord(x):
    if x == '1':
        return "millimeters"
    elif x == '2':
        return "centimeters"
    elif x == '3':
        return "meters"
    elif x == '4':
        return "kilometers"

def milliTo(x, y):
    if y == '1':
        return x
    elif y == '2':
        return x / 10
    elif y == '3':
        return x / 1000
    else:
        return x / 1000000

def centiTo(x, y):
    if y == '1':
        return x * 10
    elif y == '2':
        return x
    elif y == '3':
        return x / 100
    else:
        return x / 100000

def meterTo(x, y):
    #m to mm
    if y == '1':
        return x * 1000
    elif y == '2':
        return x * 100
    elif y == '3':
        return x
    else:
        return x / 1000
    
def kiloTo(x, y):
    if y == '1':
        return x * 1000000
    elif y == '2':
        return x * 100000
    elif y == '3':
        return x * 1000
    else:
        return x

while True:
    print("This application helps to convert metric units. ")
    print("1: millimeters")
    print("2: centimeters")
    print("3: meters")
    print("4: kilometers")
    unit = input("What is the unit you are entering? (1/2/3/4) ")
    newUnit = input("What unit would you like to convert to? (1/2/3/4) ")
    if unit in ('1', '2', '3', '4') and newUnit in ('1', '2', '3', '4'):
        try:
            number = float(input("What's the length? "))
        except ValueError:
            print("Please enter a valid number." )
            continue
        #millimeter
        if unit == '1':
            print(number, "millimeters converted to", makeWord(newUnit), "equals", milliTo(number, newUnit), makeWord(newUnit))
        #centimeter
        elif unit == '2':
            print(number, "centimeters converted to", makeWord(newUnit), "equals", centiTo(number, newUnit), makeWord(newUnit))
        #meter
        elif unit == '3':
            print(number, "meters converted to", makeWord(newUnit), "equals", meterTo(number, newUnit), makeWord(newUnit))
        #kilometer 
        else:
            print(number, "kilometers converted to", makeWord(newUnit), "equals", kiloTo(number, newUnit), makeWord(newUnit))
        morecalc = input("Woud you like to perform another conversion? (yes/no) ")
        if morecalc == 'no':
            break
    else:
        print("\nInvalid Input. Please try again.", end = '')