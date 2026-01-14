import drawsvg as dw

def führung(name):
    name.append(dw.Rectangle(-150,-100,300,25,fill='black'))

def fachberater(name):
    name.append(dw.Line(-38,-60,38,-60,stroke='black',stroke_width=10))

def logistik(name):
    name.append(dw.Rectangle(-150,75,300,25,fill='black'))

def drohne(name):
    drone_path = dw.Path(fill='black')
    drone_path.M(0, 20).L(60, -20).V(-30).L(0, 0).L(-60, -30).V(-20).Z()

    name.append(drone_path)

def fahrrad(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-100,-50).A(100,100,0,0,1,100,-50).M(0,-150).V(100))

def kraftrad(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-100,-50).A(100,100,0,0,1,100,-50).M(-10,-150).V(100).M(10,-150).V(100))

def ortsfest(name):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,-30).L(0,-180).L(150,-30))