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
