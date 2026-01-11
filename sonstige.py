import drawsvg as dw

def sirene():
    name = dw.Drawing(400,400,origin='center')
    name.append(dw.Rectangle(-200,-200,400,400,fill='white'))
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,-50).A(150,75,0,0,1,150,-50).Z().M(0,-50).V(100))
    return name