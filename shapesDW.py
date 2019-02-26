# shapesDW.py

from graphics import*
# Brings in all functions to my program.

winX = 600
winY = 600
window = GraphWin("Multiple Shapes", winX, winY)
# Creates a title on the Top Border of the window.
# As well as set the windows Width(550, 1st) and height(550, 2nd)
window.setCoords(0, 0, winX, winY)
# Sets coordinates

# diamond
diaSize = 70
# diamonds size
dia = Polygon(Point(winX/2 - diaSize, winY/2),
                  Point(winX/2, winY/2 + diaSize),
                  Point(winX/2 + diaSize, winY/2),
                  Point(winX/2, winY/2 - diaSize))
# diamonds points
dia.draw(window)
# draws the diamond
dia.setFill(color_rgb(0,170,0))
# color
