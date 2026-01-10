import drawsvg as dw

def taktischen_zeichen(grundzeichen, fachdienst='', organisation='HiOrg'):
    zeichen = dw.Drawing(400,350)
    zeichen.append(dw.Rectangle(0,0,400,350,fill='white'))
    if grundzeichen == 'Einheit':
        einheit(zeichen, organisation)
    elif grundzeichen == 'Fahrzeug':
        fahrzeug(zeichen, organisation)
    if fachdienst == 'Sanität':
        sandienst(zeichen)
    if fachdienst == 'Betreuung':
        betreuung(zeichen)
    if fachdienst == 'Erkundung':
        erkundung(zeichen)
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
    name.append(p.M(50,100).V(250).H(350).V(50).C(250,100,150,100,50,100).Z())
    return name


# Fachdienste
def sandienst(name):
    name.append(dw.Line(200,100,200,300,stroke='black', stroke_width=10))
    name.append(dw.Line(50,200,350,200,stroke='black', stroke_width=10))
    return name

def betreuung(name):
    name.append(dw.Line(50,300,200,100,stroke='black', stroke_width=10))
    name.append(dw.Line(200,100,350,300,stroke='black', stroke_width=10))
    return name

def erkundung(name):
    name.append(dw.Line(50,300,350,100,stroke='black', stroke_width=10))
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


grossverband(taktischen_zeichen(grundzeichen='Einheit',fachdienst='Betreuung',organisation='Polizei')).save_svg('Ausgabe/Penis.svg')
