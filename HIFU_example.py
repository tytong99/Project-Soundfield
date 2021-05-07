import numpy as np
import FieldCalcLib as fcl 
import CoordinateGenLib as cgl 
import WaveformLib as wl 
from scipy.signal import hilbert
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

fs = 2400000
f = 500000
c0=1500

#Source and receiver coordinate
sourceCrd = cgl.sphrRect(0.2,8,5,60,30,0,0) #source

scanCrd1 = cgl.lineOnAxis(0.05, 25, 'x')
scanCrd2 = cgl.lineOnAxis(0.05, 25, 'z')
planeCrd = cgl.planeGrid(scanCrd1, scanCrd2)    #receiver

dist = fcl.distance(sourceCrd,planeCrd)
propagation = fcl.fixedfGreen(dist, f, c0)
propagation = np.sum(propagation,0) #linear transformation

source = hilbert(wl.pulsedSine_single(1, 5, 0.2, f, 0.2, fs))

receivedSig = np.ndarray(shape=(len(propagation),len(source)),dtype=complex)
for i in range(len(propagation)):
    receivedSig[i,:]=propagation[i]*source

v2Int = np.sum(np.real(receivedSig)**2,1)

ax = plt.axes(projection="3d")
ax.scatter3D(planeCrd[:,0],planeCrd[:,1],planeCrd[:,2],c = v2Int[:])
