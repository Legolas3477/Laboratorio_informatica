
from ezgraphics import GraphicsWindow

win = GraphicsWindow()
win.setTitle("My First Graphics Program")
canvas=win.canvas()
canvas.setColor("blue")
canvas.drawLine(0,0,200,200)

win.wait()

