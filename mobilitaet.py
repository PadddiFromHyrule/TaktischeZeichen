import drawsvg as dw

# Mobilität und sonstige Fahrzeuge

def landgebunden(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))

def gelaendefähig(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(0, 120, 15, fill='none', stroke='black', stroke_width=10))

def schiene(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(-80, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(80, 120, 15, fill='none', stroke='black', stroke_width=10))

def anhaenger(name):
    name.append(dw.Line(-180,-50,-150,-50,stroke='black',stroke_width=10))

def abroller(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,-35).A(20,15,0,1,1,-150,-65).Z())

def kette(name):
    name.append(dw.Rectangle(-130,100,260,30,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))

def wlf(name, mobilität='Landgebunden'):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-170,-120).V(120).H(170))
    if mobilität == 'Landgebunden':
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Geländefähig':
        name.append(dw.Circle(0, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Schiene':
        name.append(dw.Circle(-120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(120, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(-80, 140, 15, fill='none', stroke='black', stroke_width=10))
        name.append(dw.Circle(80, 140, 15, fill='none', stroke='black', stroke_width=10))
    elif mobilität == 'Kette':
        name.append(dw.Rectangle(-130,120,260,30,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
    elif mobilität == 'Anhänger':
        name.append(dw.Line(-200,-70,-170,-70,stroke='black',stroke_width=10))

def fahrrad(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-100,-50).A(100,100,0,0,1,100,-50).M(0,-150).V(100))

def kraftrad(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-100,-50).A(100,100,0,0,1,100,-50).M(-10,-150).V(100).M(10,-150).V(100))

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
