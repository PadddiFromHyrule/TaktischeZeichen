import drawsvg as dw
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