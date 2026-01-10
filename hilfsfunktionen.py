import drawsvg as dw

def welle(name, x_start, y_start, anzahl_wellen, breite_welle, amplitude):
    p = dw.Path(stroke='black', stroke_width=10, fill='none')
    # Start
    p.M(x_start, y_start)
    
    # Eine Welle besteht aus zwei Halbbögen (Runter und Hoch)
    for i in range(int(anzahl_wellen * 2)):
        if i % 2 == 1:
            richtung = 1
        else:
            richtung = -1
        dy = amplitude * richtung
        p.c(breite_welle/4, 0, breite_welle/4, dy, breite_welle/2, dy)
        
    name.append(p)
    return name