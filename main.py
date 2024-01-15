from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(1200, 600)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    win.wait_for_close()

main()