import drawsvg as dw
import numpy as np
from hilfsfunktionen import welle
# Fachdienste
# CBRN

def cbrn(name):
    name.append(dw.Line(-60,75,60,-75,stroke='black', stroke_width=10))
    name.append(dw.Line(-60,-75,60,75,stroke='black', stroke_width=10))
    name.append(dw.Circle(74,-61,25,fill='black'))
    name.append(dw.Circle(-74,-61,25,fill='black'))

def cbrn_messen(name):
    name.append(dw.Line(-60,75,60,-75,stroke='black', stroke_width=10))
    name.append(dw.Line(-60,-75,60,75,stroke='black', stroke_width=10))
    name.append(dw.Line(-120,45,120,-45,stroke='black', stroke_width=10))
    name.append(dw.Circle(74,-61,25,fill='black'))
    name.append(dw.Circle(-74,-61,25,fill='black'))

def dekontamination(name):
    name.append(dw.Line(-60,75,60,-75,stroke='black', stroke_width=10))
    name.append(dw.Line(-60,-75,60,75,stroke='black', stroke_width=10))
    p = dw.Path(stroke='black', stroke_width=10)
    name.append(p.M(-60,75).h(50).h(-50).v(-50))
    name.append(p.M(60,75).h(-50).h(50).v(-50))
    name.append(dw.Circle(74,-61,25,fill='black'))
    name.append(dw.Circle(-74,-61,25,fill='black'))

def umweltschutz_gewässer(name):
    name.append(dw.Line(-60,25,60,-75,stroke='black', stroke_width=10))
    name.append(dw.Line(-60,-75,60,25,stroke='black', stroke_width=10))
    p = dw.Path(stroke='black', stroke_width=10)
    name.append(p.M(-60,25).h(50).h(-50).v(-50))
    name.append(p.M(60,25).h(-50).h(50).v(-50))
    name.append(dw.Circle(74,-61,25,fill='black'))
    name.append(dw.Circle(-74,-61,25,fill='black'))
    welle(name,-75,65,2,75,25)
    welle(name,-75,85,2,75,25)

def trinkwasseraufbereitung(name):
    p =dw.Path(stroke='black', stroke_width=10,fill='none')
    name.append(p.M(60,-75).A(100,100,0,0,1,60,75).m(-5,0).h(25).h(-25).v(-25))
    name.append(p.M(-60,-75).A(100,100,0,0,0,-60,75).m(5,0).h(-25).h(25).v(-25))
    welle(name,-60,-25,2,60,20)
    name.append(p.M(-60,15).h(90).A(30,30,0,0,1,60,45))
    name.append(p.M(20,30).v(-30).m(-15,0).h(30))

# Betreuung

def betreuung(name):
    name.append(dw.Line(-150,100,0,-100,stroke='black', stroke_width=10))
    name.append(dw.Line(0,-100,150,100,stroke='black', stroke_width=10))

def psnv(name):
    betreuung(name)
    name.append(dw.Text('PSNV',50, x=0, y=75,text_anchor='middle', font_family='DejaVu Sans',font_weight='bold'))

def sandienst(name, arzt=False, pflege=False, rettungsdienst=False):
    name.append(dw.Line(0,-100,0,100,stroke='black', stroke_width=10))
    name.append(dw.Line(-150,0,150,0,stroke='black', stroke_width=10))
    if arzt:
        name.append(dw.Line(-30,50,30,50,stroke='black', stroke_width=10))
    if pflege:
        name.append(dw.Line(-75,30,-75,-30,stroke='black', stroke_width=10))
    if rettungsdienst:
        name.append(dw.Line(75,30,75,-30,stroke='black', stroke_width=10))


def erkundung(name):
    name.append(dw.Line(-150,100,150,-100,stroke='black', stroke_width=10))

def löschen(name):
    name.append(dw.Line(-150,0,150,0,stroke='black',stroke_width=10))
    name.append(dw.Line(25,0,150,-100,stroke='black',stroke_width=10))
    name.append(dw.Line(25,0,150,100,stroke='black',stroke_width=10))

# def wasserversorgung(name):
#     löschen(name)
#     welle(name,-130,-30,2,70,30)

def transport(name):
    name.append(dw.Circle(0, 0, 90, fill='none', stroke='black', stroke_width=10))
    name.append(dw.Line(-90,0,90,0,stroke='black',stroke_width=10))
    name.append(dw.Line(0,-90,0,90,stroke='black',stroke_width=10))
    name.append(dw.Line(-90/np.sqrt(2),-90/np.sqrt(2),90/np.sqrt(2),90/np.sqrt(2),stroke='black',stroke_width=10))
    name.append(dw.Line(-90/np.sqrt(2),90/np.sqrt(2),90/np.sqrt(2),-90/np.sqrt(2),stroke='black',stroke_width=10))

def rht_drehleiter(name):
    name.append(dw.Line(-70,90,40,40*(-9/7),stroke='black',stroke_width=10))
    name.append(dw.Rectangle(40,40*(-9/7)-30,30,30,stroke='black',stroke_width=10,fill='none'))

def deichverteidigung(name):
    p = dw.Path(stroke='black', stroke_width=10,fill='none')
    name.append(p.M(-130,80).H(-30).L(30,-80).H(80).L(100,-20).H(130))
    welle(name,-130,-50,2,60,20)
    welle(name,-130,-20,2,60,20)

def kampfmittelbeseitigung(name):
    name.append(dw.Circle(0,0,45,fill='black'))
    name.append(dw.Circle(0,0,75,fill='none',stroke='black', stroke_width=10))
    name.append(dw.Line(0.5*np.sqrt(2)*75,-0.5*np.sqrt(2)*75,0.5*np.sqrt(2)*110,-0.5*np.sqrt(2)*110,fill='none',stroke='black', stroke_width=10))
    name.append(dw.Line(-0.5*np.sqrt(2)*75,-0.5*np.sqrt(2)*75,-0.5*np.sqrt(2)*110,-0.5*np.sqrt(2)*110,fill='none',stroke='black', stroke_width=10))

def gefahr_a(name):
    name.append(dw.Circle(0,0,20,stroke='black',stroke_width='black',fill='black'))
    # winkel_ende = winkel_start + 60
    p = dw.Path(stroke='black',fill='black')
    for x in [30, 150, 270]:
        name.append(p.M(np.sin(np.radians(x))*30,np.cos(np.radians(x))*30).L(np.sin(np.radians(x))*90,np.cos(np.radians(x))*90))
        name.append(p.A(125,125,0,0,1,np.sin(np.radians(x-60))*90,np.cos(np.radians(x-60))*90))
        name.append(p.L(np.sin(np.radians(x-60))*30,np.cos(np.radians(x-60))*30))
        name.append(p.A(30,30,0,0,0,np.sin(np.radians(x))*30,np.cos(np.radians(x))*30).Z())

def gefahr_b(name):
    pass