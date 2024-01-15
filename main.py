from graphics import Window, Line, Points

def main():
    win = Window(800, 600)
    line = Line(Points(50, 50), Points(400, 400))
    win.draw_line(line, "black")
    win.wait_for_close()

main()