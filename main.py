import datetime
import math
def date():
    x = datetime.datetime.now()
    return x

def squareRoot(one):
    a = math.sqrt(one)
    return a

def threeDates():
    y = datetime.datetime.now()
    return(y.strftime("%x"), y.strftime("%c"), y.strftime("%Y"))

def addition(numberOne, numberTwo):
    return (numberOne + numberTwo)

def subtraction(numberOne, numberTwo):
    return (numberOne - numberTwo)

def multiplication(numberOne, numberTwo):
    return (numberOne * numberTwo)

def division(numberOne, numberTwo):
    return (numberOne / numberTwo)
