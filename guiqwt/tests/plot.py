# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guiqwt/__init__.py for details)

"""CurvePlotDialog test"""

SHOW = True # Show test in GUI-based test launcher

from PyQt4.QtGui import QFont

from guiqwt.plot import CurvePlotDialog
from guiqwt.tools import HRangeTool
from guiqwt.builder import make
from guiqwt import panels

def plot(*items):
    win = CurvePlotDialog(edit=False, toolbar=True,
                          wintitle="CurvePlotDialog test",
                          options=dict(title="Title", xlabel="xlabel",
                                       ylabel="ylabel"))
    win.add_tool(HRangeTool)
    plot = win.get_plot()
    for item in items:
        plot.add_item(item)
    plot.set_axis_font("left", QFont("Courier"))
    win.get_panel(panels.ID_ITEMLIST).show()
    plot.set_items_readonly(False)
    win.show()
    win.exec_()

def test():
    """Test"""
    # -- Create QApplication
    import guidata
    guidata.qapplication()
    # --
    from numpy import linspace, sin
    x = linspace(-10, 10, 200)
    dy = x/100.
    y = sin(sin(sin(x)))    
    x2 = linspace(-10, 10, 20)
    y2 = sin(sin(sin(x2)))
    plot(make.curve(x, y, color="b"),
         make.curve(x2, y2, color="g"),
         make.curve(x, sin(2*y), color="r"),
         make.merror(x, y/2, dy),
         make.label("Relative position <b>outside</b>",
                    (x[0], y[0]), (-10, -10), "BR"),
         make.label("Relative position <i>inside</i>",
                    (x[0], y[0]), (10, 10), "TL"),
         make.label("Absolute position", "R", (0,0), "R"),
         make.legend("TR"),
         )

if __name__ == "__main__":
    test()
