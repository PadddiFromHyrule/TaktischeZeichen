import drawsvg as dw
import numpy as np

# Farben

def farbe(organisation: str) -> str:
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
    return farben_dict[organisation]

# Grundzeichen

def einheit(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    name.append(dw.Rectangle(-150,-100,300,200,fill=füllung, stroke='black', stroke_width=10))

def person(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(0,-100).L(100,0).L(0,100).L(-100,0).Z())

def fahrzeug(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(-150,-100).V(100).H(150).V(-100).C(100,-50,-100,-50,-150,-100).Z())

def befehlsstelle(name,organisation='Führung'):
    füllung = farbe(organisation)
    name.append(dw.Rectangle(-150,-100,300,200,fill=füllung, stroke='black', stroke_width=10))
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    name.append(p.M(-150,100).V(140))

def luftfahrzeug(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(-150,50).A(150,150,0,0,1,150,50).Z())

def wasserfahrzeug(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(-150,-50).A(150,150,0,0,0,150,-50).Z())

def stelle(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    name.append(dw.Circle(0,0,100,stroke='black', stroke_width=10, fill=füllung))

def gebäude(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    name.append(dw.Rectangle(-150,-100,300,200,fill=füllung, stroke='black', stroke_width=10))
    p = dw.Path(stroke='black', stroke_width=10, fill=füllung)
    name.append(p.M(-150,-100).L(0,-150).L(150,-100).Z())

def raum(name, organisation='HiOrg'):
    füllung = farbe(organisation)
    name.append(dw.Rectangle(-100,-100,200,200,fill=füllung, stroke='black', stroke_width=10))

# Gebiet?

def massnahme(name, organisation = 'HiOrg'):
    p = dw.Path(stroke=farbe('Massnahmen'), stroke_width=10, fill=farbe(organisation))
    name.append(p.M(-100,-100).H(100).L(0,(np.sqrt(3) / 2) * 100).Z())

def gefahr(name, organisation = 'HiOrg'):
    p = dw.Path(stroke=farbe('Gefahren'), stroke_width=10, fill=farbe(organisation))
    name.append(p.M(-100,100).H(100).L(0,-(np.sqrt(3) / 2) * 100).Z())

def markierung(name, organisation = 'HiOrg'):
    p = dw.Path(stroke='black', stroke_width=10, fill=farbe(organisation))
    name.append(p.M(-100,-150).H(100).V(50).L(0,np.sqrt(3) / 2 * 200).L(-100,50).Z())

def ereignis(name, organisation = 'HiOrg'):
    p = dw.Path(stroke='black', stroke_width=10, fill=farbe(organisation))
    name.append(p.M(-100,-100).L(0,(np.sqrt(3) / 2) * 100).L(100,-100))

def spontanhelfer(name, organisation='Zivil'):
    p = dw.Path(stroke='black', stroke_width=10, fill=farbe(organisation))
    name.append(p.M(-75,-75).A(37.5,37.5,0,0,1,75,-75).A(37.5,37.5,0,0,1,75,75).A(37.5,37.5,0,0,1,-75,75).A(37.5,37.5,0,0,1,-75,-75).Z())
