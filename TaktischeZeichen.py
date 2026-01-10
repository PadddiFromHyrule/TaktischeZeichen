import drawsvg as dw
import numpy as np
from grundzeichen import *
from fachdienste import *
from mobilitaet import *
from staerken import *

def taktischen_zeichen(grundzeichen, fachdienst='', organisation='HiOrg'):
    zeichen = dw.Drawing(400,375)
    zeichen.append(dw.Rectangle(0,0,400,375,fill='white'))
    if grundzeichen == 'Einheit':
        einheit(zeichen, organisation)
    elif grundzeichen == 'Fahrzeug':
        fahrzeug(zeichen, organisation)
    if fachdienst == '':
        pass
    else:
        fachdienst(zeichen)
    #if fachdienst == 'Sanität':
    #    sandienst(zeichen)
    #if fachdienst == 'Betreuung':
    #    betreuung(zeichen)
    #if fachdienst == 'Erkundung':
    #    erkundung(zeichen)
    #if fachdienst == 'Löschen':
    #    löschen(zeichen)
    #if fachdienst == 'Wasserversorgung':
    #    wasserversorgung(zeichen)
    return zeichen

taktischen_zeichen(grundzeichen='Einheit',fachdienst=rht,organisation='Polizei').save_svg('Ausgabe/Penis.svg')
