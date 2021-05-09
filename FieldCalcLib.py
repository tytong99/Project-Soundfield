#============================================================================#
#Library that stores functions for calculating sound field parameters        #
#============================================================================#
import numpy as np

'''Point to point Euclidian distance calculation for two sets of coordinates
Input parameters:
    coord1, coord2: 2D arrays, with the columns being x,y and z coordinates
Output:
    dist as distance matrix
'''
def distance(coord1,coord2):
    m = int(coord1.size/3)
    n = int(coord2.size/3)  #dude I miss matlab, this size/3 is cringy
    dist = np.ndarray((m,n))
    for i in range (m):
        for j in range (n):
            dist[i,j]=np.sqrt((coord1[i,0]-coord2[j,0])**2\
                +(coord1[i,1]-coord2[j,1])**2+(coord1[i,2]-coord2[j,2])**2)
    return (dist)

'''Freefield monopole green function wave propagation matrix, fixed frequency
G = (e^-jkr/c0)/r
Input parameters:
    dist, a matrix of distances
    freq, frequency of propagating wave [Hz]
    c0 speed of sound
Output:
    m is the complex propagation matrix with fixed frequency attenuation
'''
def fixedfGreen(dist,freq,c0):
    m = np.ndarray(shape=dist.shape,dtype=complex)
    m = np.exp(-1j*2*np.pi*freq*dist/c0)/dist
    return (m)
