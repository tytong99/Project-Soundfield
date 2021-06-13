#=============================================================================
#Spatial Audio Example 1
#Crosstalk cancellation of loudspeaker array (CTC)
#CTC is a form of broadband audible soundfield control, achieved with inverse
#filters (in most of the cases). Invented by Atal & Schroeder (yes, the reverb
#acoustics guy) in the 60s. Academic audiophiles try to revive it from time to
#time). Inverse sound field control theory is one of the most beautiful
#techniques that has ever existed in acoustics in my personal opinion (hmmm I
#wonder why hmmm...)
#=============================================================================

import numpy as np
import CoordinateGenLib as cgl 
import WaveformLib as wl 
import AnalysisLib as al
import FieldCalcLib as fcl
from matplotlib import pyplot as plt

c0 = 343
fs = 44100
nfft = 4096
f=np.arange(0,fs/2+fs/nfft,fs/nfft) #create frequency vector
t=np.arange(0,nfft/fs,1/fs) #Time vector for plotting filters

#loudspeaker geometry
speakerCrd = cgl.lineOnAxis(0.75,5,'x')
#Diameter of a listener is typically 20 cm
listenPts = np.concatenate(cgl.pt(-0.1,1,0),cgl.pt(0.1,1,0),0)
plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(speakerCrd[:,0],speakerCrd[:,1],speakerCrd[:,2],c = 'r')
ax.scatter3D(listenPts[:,0],listenPts[:,1],listenPts[:,2],c = 'b')