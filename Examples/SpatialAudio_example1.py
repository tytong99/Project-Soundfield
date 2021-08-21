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
import os, sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import numpy as np
from Project_Soundfield import CoordinateGenLib as cgl 
from Project_Soundfield import WaveformLib as wl 
from Project_Soundfield import AnalysisLib as al
from Project_Soundfield import FieldCalcLib as fcl
from matplotlib import pyplot as plt

c0 = 343
fs = 44100
nfft = 4096
f=np.arange(0,fs/2+fs/nfft,fs/nfft) #create frequency vector
t=np.arange(0,nfft/fs,1/fs) #Time vector for plotting filters

#Geometry setup of the problem
speakerCrd = cgl.lineOnAxis(0.75,5,'x')
#Diameter of a listener's head is typically 20 cm
listenPts = np.vstack((cgl.pt(-0.1,1,0),cgl.pt(0.1,1,0)))
plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(speakerCrd[:,0],speakerCrd[:,1],speakerCrd[:,2],c = 'r')
ax.scatter3D(listenPts[:,0],listenPts[:,1],listenPts[:,2],c = 'b')

#Control plant matrix
dist = fcl.distance(listenPts,speakerCrd)
