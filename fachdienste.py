import drawsvg as dw
import numpy as np
from hilfsfunktionen import welle
# Fachdienste
def sandienst(name, arzt=False, pflege=False, rettungsdienst=False):
    name.append(dw.Line(0,-100,0,100,stroke='black', stroke_width=10))
    name.append(dw.Line(-150,0,150,0,stroke='black', stroke_width=10))
    if arzt:
        name.append(dw.Line(-30,50,30,50,stroke='black', stroke_width=10))
    if pflege:
        name.append(dw.Line(-75,30,-75,-30,stroke='black', stroke_width=10))
    if rettungsdienst:
        name.append(dw.Line(75,30,75,-30,stroke='black', stroke_width=10))

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

def deichverteidigung(name):
    p = dw.Path(stroke='black', stroke_width=10,fill='none')
    name.append(p.M(-130,80).H(-30).L(30,-80).H(80).L(100,-20).H(130))
    welle(name,-130,-50,2,60,20)
    welle(name,-130,-20,2,60,20)

def kampfmittelbeseitigung(name):
    name.append(dw.Circle(0,0,45,fill='black'))
    name.append(dw.Circle(0,0,75,fill='none',stroke='black', stroke_width=10))
    name.append(dw.Line(0.5*np.sqrt(2)*75,-0.5*np.sqrt(2)*75,0.5*np.sqrt(2)*110,-0.5*np.sqrt(2)*110,fill='none',stroke='black', stroke_width=10))
    name.append(dw.Line(-0.5*np.sqrt(2)*75,-0.5*np.sqrt(2)*75,-0.5*np.sqrt(2)*110,-0.5*np.sqrt(2)*110,fill='none',stroke='black', stroke_width=10))