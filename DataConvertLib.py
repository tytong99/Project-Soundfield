#============================================================================#
#Datatype Conversion Lib                                                     #
#Sometimes I hate python and want to use matlab                              #
#wrapping up existing functions to make sure they work                       #
#============================================================================#
import numpy as np
import scipy.signal as signal
from scipy import io

'''Convert numpy array to .mat matrix
File name needs to have .mat in it
'''
def matGen(arr,fileName)
    io.savemat(fileName,{'data':arr})
    return 0
    
'''Convert a numpy array into int16 to write to wav file
File name needs to have .wav in it
'''
def wavGen(sig,fileName,fs):
    sig=np.asarray(sig, dtype=np.int16)
    io.wavfile.write(fileName,fs,sig)
    return 0