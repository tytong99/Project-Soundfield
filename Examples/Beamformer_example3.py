#=============================================================================
#Beamformer Example 3
#Simple broadband beamforming
#=============================================================================
import os, sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import numpy as np
from Project_Soundfield import FieldCalcLib as fcl 
from Project_Soundfield import CoordinateGenLib as cgl 
from Project_Soundfield import WaveformLib as wl 
from scipy.signal import hilbert
from matplotlib import pyplot as plt

fs = 48000
c0 = 343
nfft = 4096
f=np.arange(0,fs/2+fs/nfft,fs/nfft) #Frequency vec

#Sensor def
n = 12  #sensor number
l = 1 #array length
ulaCrd = cgl.lineOnAxis(l,n,'x')

#Source def
srcCrd = cgl.pt(1,2,3)
src = wl.bbSinc(1,1,fs,8000,0.5)

dist = fcl.distance(srcCrd,ulaCrd)
M = fcl.fGreen(dist,f,c0)
rcvTD,rcvFD = fcl.fdTransmit(src,M)