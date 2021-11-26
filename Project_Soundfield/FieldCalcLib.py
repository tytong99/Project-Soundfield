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


'''Angle calculation for two SETS of points with respect to a third point 
ptPivot
Input parameters:
    pt1, pt2, pt3: 
'''
def angle(pt1,pt2,ptPivot,mode):
    a = pt1-ptPivot
    b = pt2-ptPivot
    theta = np.arccos(np.dot(a,b.T)/(np.linalg.norm(a) *\
         np.linalg.norm(b)))
    if mode == 'rad':
        return(theta)
    elif mode == 'deg':
        return(np.rad2deg(theta))

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

'''Freefield monopole green function wave propagation matrix, all frequency
G = (e^-jkr/c0)/r
Input parameters:
    dist, a matrix of distances
    f, pre-defined frequency vector
    c0 speed of sound
Output:
    for each frequency, generate a corresponding plant matrix,
    return a sequence of plant matrices (3D array 'M')
    [M11, M12,......, M1b]
    [M21, M22,......, M2b]
    [        ,......,    ]    [        ,......,  ]    [        ,......,    ]
    [Ma1, ca2,......, Mab]
    --------M-of-f1---------------M-of-f2-------------------M-of-f3-------->
                                frequency
'''
def fGreen(dist,f,c0):
    M = np.ndarray(shape = (dist.shape[0],dist.shape[1],len(f)),dtype=complex)
    for k in range (len(f)):
        for i in range(dist.shape[0]):
            for q in range (dist.shape[1]):
                M[i][q][k]=np.exp(-1j*2*np.pi*f[k]*dist[i][q]/c0)/\
                    dist[i-1][q-1]

    return(M)

'''Signal transmission through a frequency domain propagation plant matrix
A wrapper function that applies FFT, multiply by plant matrix, compute IRFFT
Input parameters:
    sig: source signal
    plant: 3D ndarray, with dimension 2 (third dimension) the frequency vector
Output:
    rcvTD: received multichannel signal in time domain
    rcvFD: received multichannel signal in freq domain
When FFT/IFFT is applied, nfft = 2*(length of frequency vector-1)
'''
def fdTransmit(sig,plant):
    rcvFD = np.ndarray(shape = plant.shape,dtype=complex)
    nfft = (plant.shape[2]-1)*2
    rcvTD = np.ndarray(shape = (plant.shape[0],plant.shape[1],nfft),dtype=complex)
    sigFD = np.fft.fft(sig,nfft)[0:plant.shape[2]]
    for i in range(plant.shape[0]):
        for j in range(plant.shape[1]):
            rcvFD[i,j,:] = sigFD*plant[i,j,:]
            rcvTD[i,j,:] = np.fft.irfft(rcvFD[i,j,:])
    return(rcvTD,rcvFD)