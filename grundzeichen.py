import drawsvg as dw

farben_dict ={
    'Feuerwehr': '#FA321E',
    'HiOrg': '#FFFFFF',
    'THW': '#003399',
    'Führung': '#FAFA00',
    'Polizei': '#64DC32',
    'Bundeswehr': '#B4783C',
    'Sonstige': '#FA8C00',
    'Zivil': '#BEBEBE',
    'Massnahmen': '#3264FA',
    'Gefahren': '#FA321E',
    'Kontamination': '#FAFA00',
    'Sicherheit': '#64DC32',
}
# Grundzeichen
def farbe(organisation):
    # Besser als Dictionary?
    if organisation == 'Feuerwehr':
        farbe = '#fa321e'
    if organisation == 'HiOrg':
        farbe = '#ffffff'
    elif organisation == 'THW':
        farbe = '#003399'
    elif organisation == 'Führung':
        farbe = '#fafa00'
    elif organisation == 'Polizei':
        farbe = '#64dc32'
    elif organisation == 'Bundeswehr':
        farbe = '#b4783c'
    elif organisation == 'Sonstige':
        farbe = '#fa8c00'
    elif organisation == 'Zivil':
        farbe = '#bebebe'
    else: 
        farbe = '#ffffff'
    return farbe

def einheit(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    name.append(dw.Rectangle(-150,-100,300,200,fill=füllung, stroke='black', stroke_width=10))
    return name

def fahrzeug(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(-150,-100).V(100).H(150).V(-100).C(100,-50,-100,-50,-150,-100).Z())
    return name

def befehlsstelle(name,organisation='Führung'):
    füllung = farbe(organisation)
    name.append(dw.Rectangle(-150,-100,300,200,fill=füllung, stroke='black', stroke_width=10))
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,100).V(140))
    return name