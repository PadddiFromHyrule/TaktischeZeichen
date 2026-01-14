import drawsvg as dw
from hilfsfunktionen import *
from grundzeichen import *

# Mobilität und sonstige Fahrzeuge

def strassenfähig(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))

def gelaendefähig(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(0, 120, 15, fill='none', stroke='black', stroke_width=10))

def offroadfähig(name):
    p = dw.Path(fill='none', stroke='black', stroke_width=10)
    name.append(p.M(-120,120).H(120))
    name.append(dw.Circle(-120, 120, 15, fill='white', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='white', stroke='black', stroke_width=10))
    name.append(dw.Circle(0, 120, 15, fill='white', stroke='black', stroke_width=10))

def amphibienfahrzeug(name):
    welle(name,-90,130,2,90,20)
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))

def kette(name):
    name.append(dw.Rectangle(-130,100,260,30,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))

def schiene(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(-80, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(80, 120, 15, fill='none', stroke='black', stroke_width=10))

def aufgleisbar(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(0, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(-80, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(80, 120, 15, fill='none', stroke='black', stroke_width=10))

def anhänger(name):
    p = dw.Path(fill='none', stroke='black', stroke_width=10)
    name.append(p.M(-150,-57.5).H(-180).V(-42.5).H(-150))

def pkw_anhänger(name):
    anhänger(name)
    name.append(dw.Circle(0, 120, 15, fill='none', stroke='black', stroke_width=10))

def lkw_anhänger(name):
    anhänger(name)
    name.append(dw.Circle(-20, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(20, 120, 15, fill='none', stroke='black', stroke_width=10))

def abroller(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,-35).A(20,15,0,1,1,-150,-65).Z())

def container(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,-100).A(20,20,0,0,1,-110,-100))
    name.append(p.M(110,-100).A(20,20,0,0,1,150,-100))

def wechselbrücke(name):
    name.append(dw.Line(-120,100,-120,140, stroke='black', stroke_width=10))
    name.append(dw.Line(120,100,120,140, stroke='black', stroke_width=10))

def rollcontainer(name,organisation='HiOrg'):
    füllung = farbe(organisation)
    name.append(dw.Circle(-20, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(20, 120, 15, fill='none', stroke='black', stroke_width=10))
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(-65,-100).V(100).H(65).V(-100).C(30,-60,-30,-60,-65,-100).Z())
    h = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(h.M(65,-100).A(20,15,0,1,1,65,-60))

def wlf(name, mobilität='Strassenfähig'): # ToDo
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-170,-120).V(120).H(170))
    if mobilität == 'Landgebunden':
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Geländefähig':
        name.append(dw.Circle(0, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Offroadfähig':
        p = dw.Path(fill='none', stroke='black', stroke_width=10)
        name.append(p.M(-120,140).H(140))
        name.append(dw.Circle(-120, 140, 15, fill='white', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='white', stroke='black', stroke_width=10))
        name.append(dw.Circle(0, 140, 15, fill='white', stroke='black', stroke_width=10))
    elif mobilität == 'Amphibienfahrzeug':
        welle(name,-90,150,2,90,20)
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Schiene':
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(-80, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(80, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Aufgleisbar':
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(0, 140, 15, fill='none', stroke='black', stroke_width=10))        
        name.append(dw.Circle(-80, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(80, 140, 15, fill='none', stroke='black', stroke_width=10))  
    elif mobilität == 'Kette':
        name.append(dw.Rectangle(-130,120,260,30,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
    elif mobilität == 'Anhänger':
        p = dw.Path(fill='none', stroke='black', stroke_width=10)
        name.append(p.M(-170,-77.5).H(-200).V(-62.5).H(-170))
    elif mobilität == 'PKW-Anhänger':
        p = dw.Path(fill='none', stroke='black', stroke_width=10)
        name.append(p.M(-170,-77.5).H(-200).V(-62.5).H(-170))
        name.append(dw.Circle(0, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'LKW-Anhänger':
        p = dw.Path(fill='none', stroke='black', stroke_width=10)
        name.append(p.M(-170,-77.5).H(-200).V(-62.5).H(-170))
        name.append(dw.Circle(-20, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(20, 140, 15, fill='none', stroke='black', stroke_width=10))

def hebegerät(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-75,100).V(-100).H(0).A(37.5,37.5,0,0,0,75,-100))

def bagger(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    p.M(-75,100).V(-100).H(0).A(37.5,37.5,0,0,1,75,-100).args['transform'] = 'rotate(45)'
    name.append(p)

def räumgerät(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,0).H(75).M(75,-60).V(30).L(125,50))

# Aus der alten Empfehlung

# def flugzeug():
#     name = dw.Drawing(400,400,origin='center')
#     name.append(dw.Rectangle(-200,-200,400,400,fill='white'))
#     name.append(dw.Rectangle(-150,-20,140,40,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
#     name.append(dw.Rectangle(10,-20,140,40,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
#     name.append(dw.Line(0,-50,0,50,stroke_width=10, stroke='black'))
#     return name

# def hubschrauber():
#     name = dw.Drawing(400,400,origin='center')
#     name.append(dw.Rectangle(-200,-200,400,400,fill='white'))
#     name.append(dw.Rectangle(-150,-20,140,40,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
#     name.append(dw.Rectangle(10,-20,140,40,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
#     name.append(dw.Line(0,0,0,100,stroke_width=10, stroke='black'))
#     name.append(dw.Line(-50,100,50,100,stroke_width=10, stroke='black'))
#     return name
