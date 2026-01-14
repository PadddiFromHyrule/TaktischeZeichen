import drawsvg as dw
import numpy as np
import sys
from grundzeichen import *
from ergänzungszeichen import *
from fachdienste import *
from fahrzeuge import *
from staerken import *
from sonstige import *
from verwaltungsstufen import *

print(sys.argv)
zeichen = dw.Drawing(450,450,origin='center')
zeichen.append(dw.Rectangle(-225,-225,450,450,fill='white'))
#person(zeichen,'THW')
#sandienst(zeichen,arzt=True)
#europäische_union(zeichen)
stelle(zeichen)
drohne(zeichen)
# kampfmittelbeseitigung(zeichen)
for element in sys.argv:
    if element == 'einheit':
        einheit(zeichen)
zeichen.save_svg('Ausgabe/Penis.svg')
