import drawsvg as dw
import numpy as np
from grundzeichen import *
from fachdienste import *
from fahrzeuge import *
from staerken import *
from sonstige import *
from verwaltungsstufen import *

zeichen = dw.Drawing(450,450,origin='center')
zeichen.append(dw.Rectangle(-225,-225,450,450,fill='white'))
#person(zeichen,'THW')
#sandienst(zeichen,arzt=True)
#europäische_union(zeichen)
einheit(zeichen)
kampfmittelbeseitigung(zeichen)
zeichen.save_svg('Ausgabe/Penis.svg')
