#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from images import Picture
from EdgeDetector import Detector
import skimage.viewer


cut_region = (450, 50, 100, 100)  # Границы обрезки изображения
tk = TkDrawer()
Photo1 = Picture(filename="./images/1.bmp", region=cut_region)
tk.clean()

try:
    while True:

        tk.clean()
        if ():
            tk.draw_point(f.p)
        elif ():
            tk.draw_line(f.p, f.q)
        elif ():
            for n in range(f.points.size()):
                tk.draw_line(f.points.last(), f.points.first())
                f.points.push_last(f.points.pop_first())
        print()

        view = skimage.viewer.ImageViewer(image=Photo1.image)
        view.show()

except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
