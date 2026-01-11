import drawsvg as dw
# Stärke
def trupp(name):
    name.append(dw.Circle(0, -130, 15))
    return name

def gruppe(name):
    name.append(dw.Circle(-25, -130, 15))
    name.append(dw.Circle(25, -130, 15))
    return name

def zug(name):
    name.append(dw.Circle(0, -130, 15))
    name.append(dw.Circle(-45, -130, 15))
    name.append(dw.Circle(45, -130, 15))
    return name

def bereitschaft(name):
    name.append(dw.Line(0, -115, 0, -155, stroke = 'black', stroke_width = 15))
    return name

def abteilung(name):
    name.append(dw.Line(-15, -115, -15, -155, stroke = 'black', stroke_width = 15))
    name.append(dw.Line(15, -115, 15, -155, stroke = 'black', stroke_width = 15))
    return name

def grossverband(name):
    name.append(dw.Line(-30, -115, -30, -155, stroke = 'black', stroke_width = 15))
    name.append(dw.Line(0, -115, 0, -155, stroke = 'black', stroke_width = 15))
    name.append(dw.Line(30, -115, 30, -155, stroke = 'black', stroke_width = 15))
    return name