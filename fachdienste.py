import drawsvg as dw
import numpy as np
from hilfsfunktionen import welle
# Fachdienste
def sandienst(name, arzt=False):
    name.append(dw.Line(0,-100,0,100,stroke='black', stroke_width=10))
    name.append(dw.Line(-150,0,150,0,stroke='black', stroke_width=10))
    if arzt:
        name.append(dw.Line(-30,50,30,50,stroke='black', stroke_width=10))

def betreuung(name):
    name.append(dw.Line(-150,100,0,-100,stroke='black', stroke_width=10))
    name.append(dw.Line(0,-100,150,100,stroke='black', stroke_width=10))

def erkundung(name):
    name.append(dw.Line(-150,100,150,-100,stroke='black', stroke_width=10))

def löschen(name):
    name.append(dw.Line(-150,0,150,0,stroke='black',stroke_width=10))
    name.append(dw.Line(25,0,150,-100,stroke='black',stroke_width=10))
    name.append(dw.Line(25,0,150,100,stroke='black',stroke_width=10))

def wasserversorgung(name):
    löschen(name)
    welle(name,-130,-30,2,70,30)

def transport(name):
    name.append(dw.Circle(0, 0, 90, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Line(-90,0,90,0,stroke='black',stroke_width=10))
    name.append(dw.Line(0,-90,0,90,stroke='black',stroke_width=10))
    name.append(dw.Line(-90/np.sqrt(2),-90/np.sqrt(2),90/np.sqrt(2),90/np.sqrt(2),stroke='black',stroke_width=10))
    name.append(dw.Line(-90/np.sqrt(2),90/np.sqrt(2),90/np.sqrt(2),-90/np.sqrt(2),stroke='black',stroke_width=10))

def rht_drehleiter(name):
    name.append(dw.Line(-70,90,40,40*(-9/7),stroke='black',stroke_width=10))
    name.append(dw.Rectangle(40,40*(-9/7)-30,30,30,stroke='black',stroke_width=10,fill='none'))
