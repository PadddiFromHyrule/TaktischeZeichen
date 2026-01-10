import drawsvg as dw
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
