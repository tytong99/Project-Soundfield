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
def matGen(arr,fileName):
    io.savemat(fileName,{'data':arr})
    return 0
    
'''Convert a numpy array into int16 to write to wav file
File name needs to have .wav in it
'''
def wavGen(sig,fileName,fs):
    sig=np.asarray(sig, dtype=np.int16)
    io.wavfile.write(fileName,fs,sig)
    return 0

'''2-Channel Wav File Reader
Convert .wav file into two arrays
Enable Mono file to two channels / Split 2-channel .wav file
To read mono file, use scipy.io.wavefile.read instead
'''
def wav_read2(file_name):
    fs, data = io.wavfile.read(file_name)
    shape=data.shape
    if len(shape)==1:
        ch_l=data
        ch_r=data
    elif len(shape)==2:
        ch_l=data[:, 0]
        ch_r=data[:, 1]
    else:
        ch_l=0
        ch_r=0
    return (fs,ch_l,ch_r)