import drawsvg as dw
# Mobilität
def landgebunden(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    return name

def gelaendefähig(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(0, 120, 15, fill='none', stroke='black', stroke_width=10))
    return name

def schiene(name):
    name.append(dw.Circle(-120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(120, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(-80, 120, 15, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Circle(80, 120, 15, fill='none', stroke='black', stroke_width=10))
    return name

def anhaenger(name):
    name.append(dw.Line(-180,-50,-150,-50,stroke='black',stroke_width=10))
    return name

def abroller(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,-35).A(20,15,0,1,1,-150,-65).Z())
    return name

def kette(name):
    name.append(dw.Rectangle(-130,100,260,30,rx=10,ry=10,stroke_width=10, stroke='black',fill='none'))
    return name

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
    return name
