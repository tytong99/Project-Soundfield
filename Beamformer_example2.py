#=============================================================================
#Beamformer Example 2
#Plane wave beamforming and steering of an ULA

#1. Gain function, both analytical & computed
#2. Narrowband, plane wave steering
#=============================================================================

import numpy as np
from Project_Soundfield import CoordinateGenLib as cgl 
from Project_Soundfield import WaveformLib as wl 
from Project_Soundfield import AnalysisLib as al
from scipy.signal import hilbert
from matplotlib import pyplot as plt

fs = 48000
f = 1500
c0 = 343
strAngled = 70  #Steering angle in degree

#1. Define an array on x axis
n = 12  #sensor number, in this case also normalising factor
l = 1 #array length
ulaCrd = cgl.lineOnAxis(l,n,'x')
d = np.sqrt((ulaCrd[1,0]-ulaCrd[0,0])**2+(ulaCrd[1,1]-ulaCrd[0,1])**2\
    +(ulaCrd[1,2]-ulaCrd[0,2])**2)  #distance between sensors

thetad = np.arange(0,181,0.5)   #Ariving angle of plane wave in deg
theta = np.deg2rad(thetad)  #Angle of plane wave in rad

'''
Plane wave conventional beamforming makes the assumption that the first
sensor that senses the first wavefront reads magnitude 1, while the other
sensors suffer a delay + attenuation of e^(-2pi*f*tau),
where tau = sin(theta)d/c0

After some simplification (mathematical/philosophical overcomplication),
a normalised gain function can be achieved.
The tricks are 
1. to use geometrical series to represent n summation of e^f(tau)
2. result in (1-ne^(f(tau))/(1-e^(f(tau)), can be then simplified using 
down to sine-only terms
'''
analytical_gain = 1/n * np.abs(np.sin(np.pi*np.sin(theta)*n*d*f/c0)/\
    np.sin(np.pi*np.sin(theta)*d*f/c0))

plt.figure()
plt.polar(theta,20*np.log10(analytical_gain))
plt.title('log scaled analytical gain function')

'''
Grating lobes are none-broadside spatial directions in which the array gain 
function peaks back at 1.
For any plannar array, natually at 0/180 degs there are two gain peaks,
after some more maths, to avoid more peaks (grating lobes / 'spatial-
aliasing' is the other name for it) from happening,
f/(c0*d)>2...for non-delayed ULA
This only means we need to be rich to buy enough tiny sensors to git gud,
that's why people put a lot of hope on MEMS nowadays (QAQ?)
'''

#Plane wave beamforming
#Source definition
src = hilbert(wl.sine(1,f,0.5,fs))

#Plane wave narrowband sum beamforming
sumRms = np.zeros(len(theta))
Prcv = np.ndarray(shape = (n,len(src)),dtype='complex')
for i in range(len(theta)):
    tau = np.arange(n)*np.sin(theta[i])*d/c0
    for j in range(n):
        Prcv[j,:] = src*np.exp(-1j*2*np.pi*f*tau[j])
    sumRms[i] = al.rms(np.sum(Prcv,0))
computed_gain = sumRms/np.max(sumRms)
plt.figure()
plt.polar(theta,20*np.log10(computed_gain))
plt.title('unsteered log scaled computed gain function')
    

#Steering delay
strAngle = np.deg2rad(strAngled)
strDelay = np.flipud(np.arange(n)*np.sin(strAngle)*d/c0) #flip delays, obv.
strArray = np.exp(-1j*2*np.pi*f*strDelay)

#Plane wave beamformer steering
for i in range(len(theta)):
    tau = np.arange(n)*np.sin(theta[i])*d/c0
    for j in range(n):
        Prcv[j,:] = src*np.exp(-1j*2*np.pi*f*tau[j])*strArray[j]
    sumRms[i] = al.rms(np.sum(Prcv,0))
computed_gain = sumRms/np.max(sumRms)
plt.figure()
plt.polar(theta,20*np.log10(computed_gain))
plt.title('steered log scaled gain function')

'''
Hey, the grating lobe moves!
At angles close to end-fire, apparant apperture of the array decreases. 
Two buzzwords here hmm...
'''

'''
This script was also part of the ISVR beamformer assignment.
I didn't do it in 2020 cause I was mentally going insane during covid.
Although I learned my biggest simulation trick 'analytical signal' here.
'''