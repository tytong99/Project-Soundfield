#============================================================================#
#Numpy-based 1D Waveform Library                                             #
#Things here are implemented as time series with a sampling frequency fs     #
#============================================================================#
import numpy as np


'''Single frame of pulsulated sine wave (or cosine if you have inverted eyes)
Input parameters:
    'A' as amplitude
    'numCyc' as number of sine cycles
    'dc' as duty cycle, no larger than 1
    'freq' as frequency of signal
    'sinePos' as starting position of sine wave in the frame, 0<sinePos<dc
    'fs' as sampling frequency
Output parameters:
    'sig' as array of real singular pulsulated sine wave
'''
def toneBurst(A,numCyc,dc,freq,sinePos,fs):
    lenSig = int(round(numCyc*fs / (dc*freq)))
    startPos = int(round(sinePos*lenSig))
    t = np.arange(0,numCyc/freq,1/fs)
    sig = np.zeros(lenSig)        
    sig[startPos : startPos+len(t)] = A * np.sin(2*np.pi*freq*t)
    return (sig)


'''Analytical complex sinusoidal wave
Input parameters:
    'A' as amplitude scaler
    'freq' as frequency
    'dur' as duration in [s]
    'fs' as sampling frequency
Output:
    'sig' as complex 1D array of analytical signal
'''
def complexSine(A,freq,dur,fs):
    sig = np.array(int(round(dur*fs)),dtype = complex)
    sig = A*np.exp(-2*1j*freq*np.pi*np.arange(0,dur,1/fs))
    return (sig)

'''Simple sine wave / cos wave
'''
def sine(A,freq,dur,fs):
    sig=np.sin(2*np.pi*freq*np.arange(0,dur,1/fs))
    return (sig)
def cosine(A,freq,dur,fs):
    sig=np.cos(2*np.pi*freq*np.arange(0,dur,1/fs))
    return (sig)

'''Personal implementation of gaussian time series, not a fcking distribution
A guassian series can be expressed either as,
f(x) = a*e^(-0.5(x-b)^2 / c^2), which is implemented here
or,
f(x) = e^(ux^2 + vx + w) where u = -0.5 / c^2, v = b / c^2, 
w = 0.5(loga-b^2) / c^2
Input parameters:
    'dur' duration in [s]
    'A', 'B', 'C' as a, b and c parameters of a gaussian
    'fs' as sampling frequency
Output:
    'sig' as guassian-shaped time series/windowing function
'''
def gausss(A,dur,B,C,fs):
    sig = A*np.exp(-0.5*(np.arange(0,2*B,2*B/(fs*dur))-B)**2/(C**2))
    return (sig)

'''Personal implementation of single frame of a morlet wavelet as time series
A sine wave times a Guassian ;)
Input parameters:
    'A' as amplitude
    'fs' as base frequency of wavelet
    'dur' as duration in time [s]
    'fs' as sampling frequency
    'B' 'C' as gaussian window parameters
Output:
    'sig' is the complex morlet wavelet as a time series related to fs
'''
def morllette(A,freq,dur,B,C,fs):
    sig = complexSine(A,freq,dur,fs)*gausss(1,dur,B,C,fs)
    return (sig)

'''Additive Gaussian White Noise time series
Gaussian white noise has a flat PSD, its auto-correlation function is impulse
Input parameters:
    'dur' time duration
    'mean' mean of Gaussian distribution
    'std' std of Gaussian distribution
    'fs' sampling frequency
Output:
    'sig' as noisy time series
'''
def agwn(dur,mean,std,fs):
    sig = np.random.normal(mean,std,dur*fs)
    sig = sig-sig.mean()
    return(sig)

'''Bandwidth-limited broadband signal burst (band-defined sinc)
A braodband time-series signal with a bandwidth limit, computed through IRFFT
This is a high-quality signal given that the NFFT number equals signal length
There shouldn't be any freq domain roll-down or gibb's...
Input parameters:
    'A' amplitude
    'dur' duration of signal in [s]
    'fs' sampling frequency
    'fc' center frequency of bandwidth
    'bandwidth' a bandwidth factor as factorial of Nyquist frequency,
        0<bandwidth<1
Output:
    'sig' as the broadband sinc time series
'''
def bbSinc(A,dur,fs,fc,bandwidth):
    nfft = int(round(dur*fs))
    f=np.arange(0,fs/2+fs/nfft,fs/nfft) #create frequency vector
    fcIndex = int(round(fc*nfft/fs))
    binNum = int(round(bandwidth*nfft/4))
    f[:] = 0
    if (fcIndex-binNum<0):
        lowBound = 0
    else:
        lowBound = fcIndex-binNum
    if (fcIndex+binNum>len(f)-1):
        upBound = len(f)-1
    else:
        upBound = fcIndex+binNum
    f[lowBound:upBound] = 1
    sig = np.roll(np.fft.irfft(f,nfft),int(round(nfft/2)))
    sig = A*sig/np.max(sig)
    return(sig)

'''My personal implementation of chirp signal
'''
def chirp():
    return(sig)

'''A zero-padded chirp signal
'''
def chirpBurst():
    return(sig)

'''Rayleigh-Plesset bubble burst
'''