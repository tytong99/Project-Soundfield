#============================================================================#
#Numpy-based Signal Analysis Lib                                             #
#============================================================================#
import numpy as np

'''Normalised auto-correlation
Input:
    x is the time series or 1D process
Output:
    'axis' is symetrical axis for the auto-correlation function
    'func' is the normalised auto-correlation function
'''
def autocorr(x):
    axis = np.arange(-len(x)+1,len(x))
    func = np.correlate(x-x.mean(),x-x.mean(),mode='full')/len(x)
    return (axis,func)

'''Root mean square helper function
'''
def rms(x):
    return(np.sqrt(np.mean(x**2)))