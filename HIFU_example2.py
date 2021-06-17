#=============================================================================
#HIFU Example 2
#Example of a HIFU soundfield steering
#1. Define source and receiver plane coordinates and find propagation matrix
#2. Define focus and steering point, and find steering delay matrix
#3. Define sound source (assume the waveform is universal at all sources) and 
#find received signal through linear transformation
#3. Find v^2 integral as uncalibrated intensity
#=============================================================================

import numpy as np
from Project_Soundfield import FieldCalcLib as fcl 
from Project_Soundfield import CoordinateGenLib as cgl 
from Project_Soundfield import WaveformLib as wl 
from scipy.signal import hilbert
from matplotlib import pyplot as plt

fs = 2400000
f = 500000
c0=1500

#Source and receiver coordinate
sourceCrd = cgl.sphrRect(0.2,8,5,60,30,0,0) #source

scanCrd1 = cgl.lineOnAxis(0.05, 50, 'x')
scanCrd2 = cgl.lineOnAxis(0.05, 50, 'z')
planeCrd = cgl.planeGrid(scanCrd1, scanCrd2)    #receiver

#Distance and propagational delay+attenuation
dist = fcl.distance(sourceCrd,planeCrd)
propagation = fcl.fixedfGreen(dist, f, c0)
propagation = np.sum(propagation,0) #linear transformation

#Steering coordinate
steerCrd = np.array([[0,0,0.02]])
focusCrd = np.array([[0,0,0]])
distFocus = fcl.distance(sourceCrd,focusCrd)
distSteer = fcl.distance(sourceCrd,steerCrd)
delay = (distSteer-distFocus)/c0
delay = delay-np.min(delay)
