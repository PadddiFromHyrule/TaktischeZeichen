import drawsvg as dw

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
    name.append(p.M(50,100).V(300).H(350).V(100).C(250,150,150,150,50,100).Z())
    return name