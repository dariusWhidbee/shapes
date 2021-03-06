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

# Circle 
Circle = Circle(Point(120,495), 70)
# circle center point and radius.
Circle.draw(window)
# Draws the circle
Circle.setFill(color_rgb(0,0,0))
# color

# Triangle
Tri = Polygon(Point(70, 50), Point(120, 160), Point(170, 50))
# X, Y points of this object
Tri.draw(window)
# Draws the Triangle
Tri.setFill(color_rgb(170,0,0))
# color

# Rectangle
Rectangle = Rectangle(Point(400,455), Point(550,560))
# X, Y points of this object
Rectangle.draw(window)
# Draws the Rectangle
Rectangle.setFill(color_rgb(0,0,170))
# color

# Oval
Oval = Oval(Point(410,50), Point(540,140))
# X, Y points of this object
Oval.draw(window)
# Draws the Oval
Oval.setFill(color_rgb(160,20,190))
# color

window.getMouse()
window.close()



