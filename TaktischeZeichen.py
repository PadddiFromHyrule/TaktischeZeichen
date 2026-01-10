import drawsvg as dw
import numpy as np
from fachdienste import *

def welle(name, x_start, y_start, anzahl_wellen, breite_welle, amplitude):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    # Start
    p.M(x_start, y_start)
    
    # Eine Welle besteht aus zwei Halbbögen (Runter und Hoch)
    for i in range(int(anzahl_wellen * 2)):
        if i % 2 == 1:
            richtung = 1
        else:
            richtung = -1
        dy = amplitude * richtung
        p.c(breite_welle/4, 0, breite_welle/4, dy, breite_welle/2, dy)
        
    name.append(p)
    return name

def taktischen_zeichen(grundzeichen, fachdienst='', organisation='HiOrg'):
    zeichen = dw.Drawing(400,375)
    zeichen.append(dw.Rectangle(0,0,400,375,fill='white'))
    if grundzeichen == 'Einheit':
        einheit(zeichen, organisation)
    elif grundzeichen == 'Fahrzeug':
        fahrzeug(zeichen, organisation)
    if fachdienst == '':
        pass
    else:
        fachdienst(zeichen)
    #if fachdienst == 'Sanität':
    #    sandienst(zeichen)
    #if fachdienst == 'Betreuung':
    #    betreuung(zeichen)
    #if fachdienst == 'Erkundung':
    #    erkundung(zeichen)
    #if fachdienst == 'Löschen':
    #    löschen(zeichen)
    #if fachdienst == 'Wasserversorgung':
    #    wasserversorgung(zeichen)
    return zeichen

# Grundzeichen
def farbe(organisation):
    if organisation == 'HiOrg' or organisation == 'Bundeswehr':
        farbe = '#ffffff'
    elif organisation == 'Feuerwehr':
        farbe = '#e30613'
    elif organisation == 'THW':
        farbe = '#0069b4'
    elif organisation == 'Polizei':
        farbe = '#13a538'
    elif organisation == 'Führung':
        farbe = '#ffed00'
    elif organisation == 'Sonstige':
        farbe = '#ec6725'
    else: 
        farbe = '#ffffff'
    return farbe

def einheit(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    name.append(dw.Rectangle(50,100,300,200,fill=füllung, stroke='black', stroke_width=10))
    return name

def fahrzeug(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(50,100).V(300).H(350).V(100).C(250,150,150,150,50,100).Z())
    return name

# Mobilität
def landgebunden(name):
    name.append(dw.Circle(80, 320, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(320, 320, 15, fill='none', stroke='black', stroke_width=10))
    return name

def gelaendefähig(name):
    name.append(dw.Circle(80, 320, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(320, 320, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(200, 320, 15, fill='none', stroke='black', stroke_width=10))
    return name

def schiene(name):
    name.append(dw.Circle(80, 320, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 320, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(280, 320, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(320, 320, 15, fill='none', stroke='black', stroke_width=10))
    return name

def anhaenger(name):
    name.append(dw.Line(20,175,50,175,stroke='black',stroke_width=10))
    return name

def abroller(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(50,185).A(15,15,0,1,1,50,165).Z())
    return name

def kette(name):
    name.append(dw.Rectangle(70,300,260,30,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
    return name

def wlf(name, mobilität='Landgebunden'):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(30,90).V(320).H(370))
    if mobilität == 'Landgebunden':
        name.append(dw.Circle(80, 340, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(320, 340, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Geländefähig':
        name.append(dw.Circle(200, 340, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(80, 340, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(320, 340, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Schiene':
        name.append(dw.Circle(80, 340, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 340, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(280, 340, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(320, 340, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Kette':
        name.append(dw.Rectangle(60,320,280,30,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))


    return name

# Stärke
def trupp(name):
    name.append(dw.Circle(200, 70, 15))
    return name

def gruppe(name):
    name.append(dw.Circle(175, 70, 15))
    name.append(dw.Circle(225, 70, 15))
    return name

def zug(name):
    name.append(dw.Circle(200, 70, 15))
    name.append(dw.Circle(155, 70, 15))
    name.append(dw.Circle(245, 70, 15))
    return name

def bereitschaft(name):
    name.append(dw.Line(200, 85, 200, 45, stroke = 'black', stroke_width = 15))
    return name

def abteilung(name):
    name.append(dw.Line(185, 85, 185, 45, stroke = 'black', stroke_width = 15))
    name.append(dw.Line(215, 85, 215, 45, stroke = 'black', stroke_width = 15))
    return name

def grossverband(name):
    name.append(dw.Line(170, 85, 170, 45, stroke = 'black', stroke_width = 15))
    name.append(dw.Line(200, 85, 200, 45, stroke = 'black', stroke_width = 15))
    name.append(dw.Line(230, 85, 230, 45, stroke = 'black', stroke_width = 15))
    return name

taktischen_zeichen(grundzeichen='Einheit',fachdienst=rht,organisation='Polizei').save_svg('Ausgabe/Penis.svg')
