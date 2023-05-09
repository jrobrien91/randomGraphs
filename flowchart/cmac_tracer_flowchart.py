#!/usr/bin/env python
"""
NAME:
cmac_tracer_flowchart.py

PURPOSE:
To create a flowchart diagram for the CMAC2.0 processing

MODIFICATION HISTORY:
2022/05/26 - Joe O'Brien <obrienj@anl.gov> - Created
"""


import schemdraw
from schemdraw import flow

with schemdraw.Drawing() as d:
    d.config(fontsize=14, unit=1.0)
    # Rectangle To Start
    label0 = "1-3 Months of Staged Data"
    d += flow.Process(w = 8).label(label0).drop('S').color('black').fill('thistle').zorder(10)
    d += flow.Arrow().down()

    # Round Process for the rest
    label1 = "Clutter Detection"
    d += flow.Terminal(w = 8).label(label1).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    # Round Process for next step
    label2 = "Texture and Pseudo \n SNR Calculated"
    d += flow.Terminal(w = 8).label(label2).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label3 = "Append Temp @ gate"
    d += flow.Terminal(w = 8).label(label3).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    #d += flow.Wire(arrow='->').at([3.8, -5.25]).to([3.8, -6.25]).color('red')

    label4 = "Fuzzy Logic \n Gate ID"
    d += flow.Terminal(w = 8).label(label4).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label5 = "Region Based \n Dealias"
    d += flow.Terminal(w = 8).label(label5).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label6 = "LP PhiDP"
    d += flow.Terminal(w = 8).label(label6).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label7 = "Sobel KDP"
    d += flow.Terminal(w = 8).label(label7).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label8 = "Spider Removal"
    d += flow.Terminal(w = 8).label(label8).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label9 = "Z-Phi Specific \n Attenuation"
    d += flow.Terminal(w = 8).label(label9).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label11 = "Visualization \n and Summary"
    d += flow.Terminal(w = 8).label(label11).drop('S').color('white').fill('purple').zorder(10)
    d += flow.Arrow().down()

    label12 = "1-3 Months of Staged \nCMAC"
    d += flow.Process(w = 8).label(label12).color('black').fill('thistle').zorder(10)

    # additional side point
    label13 = "Databases, Quick Looks,\nEtc.."
    label14 = "Interpolated Sonde \n or Sounding"
    d += flow.Process(w = 8).label(label13).color('black').fill('thistle').at([18, -24.5]).zorder(1)
    d += flow.Process(w = 8).label(label14).color('black').fill('thistle').at([-10, -6.0]).zorder(1)

    # add additional main lines
    d += flow.Wire(arrow='->').at((3.8, -5.5)).to((3.8, -26.75)).color('green')
    d += flow.Wire(arrow='->').at((4.2, -5.5)).to((4.2, -26.75)).color('red')
    d += flow.Wire(arrow='->').at((4.4, -7.75)).to((4.4, -26.75)).color('blue')
    d += flow.Wire(arrow='->').at((4.6, -10.0)).to((4.6, -26.75)).color('purple')
    d += flow.Wire(arrow='->').at((3.6, -12.25)).to((3.6, -26.75)).color('cyan')
    d += flow.Wire(arrow='->').at((3.4, -16.75)).to((3.4, -26.75)).color('peru')
    d += flow.Wire(arrow='->').at((4.8, -14.5)).to((4.8, -26.75)).color('magenta')
    d += flow.Wire(arrow='->').at((5.0, -21.25)).to((5.0, -26.75)).color('brown')
    #d += flow.Wire(arrow='->').at((5.2, -23.5)).to((5.2, -26.75)).color('lime')

    # add connector lines that are off the main line
    # purple lines
    d += flow.Wire().at((8.0, -10)).to((10.0, -10)).color('purple')
    d += flow.Wire().at((8.0, -11.5)).to((10.0, -11.5)).color('purple')
    d += flow.Wire().at((8.0, -14.0)).to((10.0, -14.0)).color('purple')
    d += flow.Wire().at((8.0, -18.5)).to((10.0, -18.5)).color('purple')
    d += flow.Wire().at((8.0, -20.5)).to((10.0, -20.5)).color('purple')
    d += flow.Wire().at((8.0, -23.00)).to((10.0, -23.00)).color('purple')
    d += flow.Wire().at((10.0, -10)).to((10.0, -23.00)).color('purple')
    # red lines
    d += flow.Wire().at((8.0, -9.5)).to((9.5, -9.5)).color('red')
    d += flow.Wire().at((8.0, -4.75)).to((9.5, -4.75)).color('red')
    d += flow.Wire().at((9.5, -4.75)).to((9.5, -9.5)).color('red')
    # green lines
    d += flow.Wire().at((8.0, -9.25)).to((9.0, -9.25)).color('green')
    d += flow.Wire().at((8.0, -5.0)).to((9.0, -5.0)).color('green')
    d += flow.Wire().at((9.0, -5.0)).to((9.0, -9.25)).color('green')
    # blue line
    d += flow.Wire().at((8.0, -9.0)).to((8.5, -9.0)).color('blue')
    d += flow.Wire().at((8.0, -7.12)).to((8.5, -7.12)).color('blue')
    d += flow.Wire().at((8.5, -9.0)).to((8.5, -7.12)).color('blue')
    # gray line
    d += flow.Wire().at((8.0, -9.75)).to((10.0, -9.75)).color('gray')
    d += flow.Wire().at((8.0, -2.7)).to((10.0, -2.7)).color('gray')
    d += flow.Wire().at((10.0, -2.7)).to((10.0, -9.75)).color('gray')
    # brown line
    d += flow.Wire().at((8.0, -22.5)).to((9.5, -22.5)).color('brown')
    d += flow.Wire().at((8.0, -21.0)).to((9.5, -21.0)).color('brown')
    d += flow.Wire().at((9.5, -22.5)).to((9.5, -21.0)).color('brown')
    # light brown line
    d += flow.Wire().at((8.0, -20.25)).to((9.5, -20.25)).color('peru')
    d += flow.Wire().at((8.0, -18.75)).to((9.5, -18.75)).color('peru')
    d += flow.Wire().at((9.5, -18.75)).to((9.5, -20.25)).color('peru')
    d += flow.Wire().at((8.0, -18.25)).to((9.5, -18.25)).color('peru')
    d += flow.Wire().at((8.0, -16.5)).to((9.5, -16.5)).color('peru')
    d += flow.Wire().at((9.5, -16.5)).to((9.5, -18.25)).color('peru')
    # pink
    d += flow.Wire().at((8.0, -16.25)).to((9.5, -16.25)).color('magenta')
    d += flow.Wire().at((8.0, -14.25)).to((9.5, -14.25)).color('magenta')
    d += flow.Wire().at((9.5, -14.25)).to((9.5, -16.25)).color('magenta')

    # Connect the final boxes
    d += flow.Wire(arrow='->').at((8.0, -25.20)).to((14.0, -25.20)).color('black')
    d += flow.Wire(arrow='->').at((-5.75, -7.0)).to((0.0, -7.0)).color('black')

    # try to add one very large last square
    d += flow.Process(w = 27, h = 20).at((-1, -4)).zorder(0).fill('thistle')
