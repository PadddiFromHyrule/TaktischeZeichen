import drawsvg as dw
import numpy as np
from grundzeichen import *
from fachdienste import *
from mobilitaet import *
from staerken import *
from sonstige import *



def taktischen_zeichen(grundzeichen=einheit, fachdienst='', organisation='HiOrg', staerke=''):
    zeichen = dw.Drawing(400,400,origin='center')
    zeichen.append(dw.Rectangle(-200,-200,400,400,fill='white'))
    grundzeichen(zeichen,organisation)
    if fachdienst == '':
        pass
    else:
        fachdienst(zeichen)
    if staerke == '':
        pass
    else:
        staerke(zeichen)
    return zeichen

taktischen_zeichen(befehlsstelle,'','Führung').save_svg('Ausgabe/Penis.svg')
