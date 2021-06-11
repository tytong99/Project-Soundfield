#=============================================================================
#Beamformer Example 1
#Example of a ULA narrowband farfield point source beamformer
#1. Define narrowband monopole sound source, define sound source coordinates
#2. Define ULA coordinates
#3. Find received signal pattern with no delay, only sum (each channel should
# contain channel noise)
#4. Find the ideal steering delays of point source - ULA array by reciprocity
#5. Steer the ULA array and compare new received signal
#=============================================================================

import numpy as np
import FieldCalcLib as fcl 
import CoordinateGenLib as cgl 
import WaveformLib as wl 
from scipy.signal import hilbert
from matplotlib import pyplot as plt

fs = 4800000
f = 500000
c0 = 1500
n = 12  #sensor number
l = 0.1 #array length
stdNoise = 0.1  #Standard deviation of channel noise, normalised

#Source coordinates & signal def
srcCrd = cgl.pt(0.1,0.04,0.14)
srcSig = hilbert(wl.pulsedSine_single(1, 5, 0.2, f, 0.2, fs))

#Receiver coordinates
ulaCrd = cgl.lineOnAxis(l,n,'x')

#Distance and propagational delay+attenuation
dist = fcl.distance(srcCrd,ulaCrd)
propagation = fcl.fixedfGreen(dist, f, c0)
propagation = np.sum(propagation,0) #linear transformation

#Received signal at each sensor without steering
rcv0 = np.ndarray(shape=(len(propagation),len(srcSig)),dtype=complex)
for i in range(len(propagation)):
    rcv0[i,:]=propagation[i]*srcSig/(4*np.pi)\
        +np.random.normal(0,stdNoise,len(srcSig))
sum_without_delay = np.sum(rcv0,0)/n

#Reciprocical delay for steering / time reversal (however you call it)
ppgDelay = dist/c0
strDelay = np.max(ppgDelay) - ppgDelay  #Steering delay

#Received signal at each sensor with steering delay
rcv1 = np.ndarray(shape=(len(propagation),len(srcSig)),dtype=complex)
for j in range(len(propagation)):
    rcv1[j,:]=propagation[j]*np.exp(-1j*2*np.pi*f*strDelay[:,j])*srcSig/(4*np.pi)\
        +np.random.normal(0,stdNoise,len(srcSig))
sum_with_delay = np.sum(rcv1,0)/n

plt.figure()
v2Int = np.sum(np.real(rcv0)**2,1)
ax = plt.axes(projection="3d")
ax.scatter3D(ulaCrd[:,0],ulaCrd[:,1],ulaCrd[:,2],c = v2Int[:])
ax.scatter3D(srcCrd[:,0],srcCrd[:,1],srcCrd[:,2],c = 'r')

plt.figure()
plt.plot(sum_without_delay,label = 'w/o Delay, summed')
plt.plot(sum_with_delay,label = 'Delay-summed')
plt.plot(srcSig,label = 'Original Signal')
plt.legend()

'''
As can be observed, through conventional beamforming, the received waveforms
on various sensors are forced to coherent, and summing the coherent signals
result in a higher summed signal amplitude, and higher SNR against chn noise. 
This beamforming targets only one point in space, this simulation only applies 
to one single frequency band.
'''