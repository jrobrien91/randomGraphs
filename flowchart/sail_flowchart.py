#!/usr/bin/env python
"""
NAME:
SAIL_flowchart.py

PURPOSE:
To create a flowchart diagram for the SAIL Z-S methodology

MODIFICATION HISTORY:
2022/05/26 - Joe O'Brien <obrienj@anl.gov> - Created
"""


import schemdraw
from schemdraw import flow

with schemdraw.Drawing() as d:
    d.config(fontsize=11, unit=1.0)
    # Terminal to Show the Start of the Diagram
    label0 = "1. CSU X-Band Radar \n\n Single File per Scan"
    d += flow.Terminal().label(label0)
    d += flow.Arrow()

    # Square Processes Container
    label1 = "2. Merged CSU X-Band \n\n Combined Scans per Date"
    d += flow.Process().label(label1).drop('E')
    d += flow.Arrow().right()

    # data-in/data-out rhomboid container
    label2 = "3. Radar Corrections \n\n CMAC2.0 \n Clutter Removal \n Obstruction Removal"
    d += flow.Data().label(label2).drop('E')
    d += flow.Arrow().right()

    # Round Processes Container
    label3 = "4. Py-ART Column Extraction \n\n Per Instrumented Location"
    d += flow.RoundProcess().label(label3).drop('E')
    d += flow.Arrow().right()

    # Square Processes Container
    label4 = "5. Matched Datasets \n\n CSU X-Band Radar Gate \n Collocated with \n Ground Instrumentation"
    d += flow.Process().label(label4).drop('S')
    d += flow.Arrow().down()

    label5 = "6. Estimated \n Snowfall Retrevial"
    d += flow.Terminal().label(label5)
