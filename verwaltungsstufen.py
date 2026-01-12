import drawsvg as dw
# Verwaltungsstufen
def gemeinde(name):
    name.append(dw.Text('*',100, x=0, y=-100,text_anchor='middle', font_family='DejaVu Sans'))

def landkreis(name):
    name.append(dw.Text('*',100, x=-40, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=40, y=-100,text_anchor='middle', font_family='DejaVu Sans'))

def bezirk(name):
    name.append(dw.Text('*',100, x=-50, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=0, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=50, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
   
def bundesland(name):
    name.append(dw.Text('*',100, x=-75, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=-25, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=25, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=75, y=-100,text_anchor='middle', font_family='DejaVu Sans'))

def nationalstaat(name):
    name.append(dw.Text('*',100, x=-100, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=-50, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=0, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=50, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=100, y=-100,text_anchor='middle', font_family='DejaVu Sans'))

def europäische_union(name):
    name.append(dw.Text('*',100, x=-25, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=25, y=-100,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=-25, y=-150,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=25, y=-150,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=-75, y=-125,text_anchor='middle', font_family='DejaVu Sans'))
    name.append(dw.Text('*',100, x=75, y=-125,text_anchor='middle', font_family='DejaVu Sans'))

