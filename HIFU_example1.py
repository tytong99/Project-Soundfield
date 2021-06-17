#=============================================================================
#HIFU Example 1
#Example of a HIFU soundfield simulation of a simple geometry
#1. Define source and receiver plane coordinates and find propagation matrix
#2. Define sound source (assume the waveform is universal at all sources) and 
#find received signal through linear transformation (propagation matrix)
#3. Find field of view v^2 integral as uncalibrated intensity
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

#Source signal
source = hilbert(wl.toneBurst(1, 5, 0.2, f, 0.2, fs))

#Simulated Received Signal Matrix
receivedSig = np.ndarray(shape=(len(propagation),len(source)),dtype=complex)
for i in range(len(propagation)):
    receivedSig[i,:]=propagation[i]*source

#Normalised Intensity (square sum)
v2Int = np.sum(np.real(receivedSig)**2,1)

plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(planeCrd[:,0],planeCrd[:,1],planeCrd[:,2],c = v2Int[:])
ax.scatter3D(sourceCrd[:,0],sourceCrd[:,1],sourceCrd[:,2],c = 'b')
