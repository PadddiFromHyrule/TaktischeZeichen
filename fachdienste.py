import drawsvg as dw
import numpy as np
from hilfsfunktionen import welle
# Fachdienste
def sandienst(name):
    name.append(dw.Line(200,100,200,300,stroke='black', stroke_width=10))
    name.append(dw.Line(50,200,350,200,stroke='black', stroke_width=10))
    return name

def betreuung(name):
    name.append(dw.Line(50,300,200,100,stroke='black', stroke_width=10))
    name.append(dw.Line(200,100,350,300,stroke='black', stroke_width=10))
    return name

def erkundung(name):
    name.append(dw.Line(50,300,350,100,stroke='black', stroke_width=10))
    return name

def löschen(name):
    name.append(dw.Line(50,200,350,200,stroke='black',stroke_width=10))
    name.append(dw.Line(225,200,350,100,stroke='black',stroke_width=10))
    name.append(dw.Line(225,200,350,300,stroke='black',stroke_width=10))
    return name

def wasserversorgung(name):
    löschen(name)
    welle(name,70,180,2,70,30)
    return name

def transport(name):
    name.append(dw.Circle(200, 200, 90, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Line(200,100,200,300,stroke='black',stroke_width=10))
    name.append(dw.Line(110,200,290,200,stroke='black',stroke_width=10))
    name.append(dw.Line(200-90/np.sqrt(2),200-90/np.sqrt(2),200+90/np.sqrt(2),200+90/np.sqrt(2),stroke='black',stroke_width=10))
    name.append(dw.Line(200-90/np.sqrt(2),200+90/np.sqrt(2),200+90/np.sqrt(2),200-90/np.sqrt(2),stroke='black',stroke_width=10))
    return name

def rht(name):
    name.append(dw.Line(120,290,265,145,stroke='black',stroke_width=10))
    name.append(dw.Rectangle(265,145-30,30,30,stroke='black',stroke_width=10,fill='none'))
    return name