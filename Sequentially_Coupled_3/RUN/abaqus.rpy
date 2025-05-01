# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022.HF11 replay file
# Internal Version: 2023_10_26-15.11.10 RELr424 177048
# Run by sp-stud on Thu Aug 22 10:57:45 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=184.807281494141, 
    height=168.210006713867)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
#: Executing "onCaeStartup()" in the home directory ...
o2 = session.openOdb(name='submo_2.odb')
#: Model: C:/Work/CavityModeling/Cube/Sequentially_Coupled_3/RUN/submo_2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs['C:/Work/CavityModeling/Cube/Sequentially_Coupled_3/RUN/submo_2.odb']
xy_result = session.XYDataFromHistory(name='ALLQB Whole Model-1', odb=odb, 
    outputVariableName='Energy lost to quiet boundaries: ALLQB for Whole Model', 
    steps=('Step-1', ), __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy_result)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
o1 = session.openOdb(
    name='C:/Work/CavityModeling/Cube/Fully_Coupled_2/RUN/fully_coupled_2.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Work/CavityModeling/Cube/Fully_Coupled_2/RUN/fully_coupled_2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       7
#: Number of Node Sets:          4
#: Number of Steps:              1
#: The deformed variable is set to UT. Analytical Rigid Surfaces and Coordinate Systems will not be displayed in the Orientation used for analysis.
odb = session.odbs['C:/Work/CavityModeling/Cube/Fully_Coupled_2/RUN/fully_coupled_2.odb']
xy_result = session.XYDataFromHistory(
    name='RADPOW through acoustic-structural interface boundary ELSET OUTER_INFINITE-1', 
    odb=odb, 
    outputVariableName='Radiated power: RADPOW through acoustic-structural interface boundary in ELSET OUTER_INFINITE', 
    steps=('Step-1', ), __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy_result)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
