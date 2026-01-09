import drawsvg as dw

pic = dw.Drawing(400,300)
def taktischen_zeichen(grundzeichen, fachdienst='', organisation='HiOrg'):
    zeichen = dw.Drawing(400,300)
    zeichen.append(dw.Rectangle(0,0,400,300,fill='white'))
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
    name.append(dw.Rectangle(50,50,300,200,fill=füllung, stroke='black', stroke_width=10))
    return name

def fahrzeug(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(50,50).V(250).H(350).V(50).C(250,100,150,100,50,50).Z())
    return name


# Fachdienste
def sandienst(name):
    name.append(dw.Line(200,50,200,250,stroke='black', stroke_width=10))
    name.append(dw.Line(50,150,350,150,stroke='black', stroke_width=10))
    return name

def betreuung(name):
    name.append(dw.Line(50,250,200,50,stroke='black', stroke_width=10))
    name.append(dw.Line(200,50,350,250,stroke='black', stroke_width=10))
    return name

def erkundung(name):
    name.append(dw.Line(50,250,350,50,stroke='black', stroke_width=10))
    return name

def trupp(name):
    name.append(dw.Circle(200, 20, 15))
    return name

def gruppe(name):
    name.append(dw.Circle(175, 20, 15))
    name.append(dw.Circle(225, 20, 15))
    return name

def zug(name):
    name.append(dw.Circle(200, 20, 15))
    name.append(dw.Circle(155, 20, 15))
    name.append(dw.Circle(245, 20, 15))
    return name

zug(taktischen_zeichen(grundzeichen='Einheit',fachdienst='Sanität',organisation='Polizei')).save_svg('Ausgabe/Penis.svg')
