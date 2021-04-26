#============================================================================#
#Numpy-based Spatial (R3 Space) Geometry Generation Lib                    #
#Specialised in generating coordinate arrays that can be visualised w/ plot3d#
#============================================================================#
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from scipy import io

#%matplotlib qt

'''Spherical coordinate (in degs) to cartesian coordinate translation
'''
def sphr2Cart(crdInput,mode):
    crd = np.ndarray(np.shape(crdInput))
    if mode == 'deg':
        crd[:,0] = crdInput[:,0]*np.sin(np.pi*crdInput[:,2]/180)\
        *np.cos(np.pi*crdInput[:,1]/180)
        crd[:,1] = crdInput[:,0]*np.sin(np.pi*crdInput[:,2]/180)\
        *np.sin(np.pi*crdInput[:,1]/180)
        crd[:,2] = crdInput[:,0]*np.cos(np.pi*crdInput[:,2]/180)
        return (crd)
    elif mode == 'rad':
        crd = np.ndarray(np.shape(crdInput))
        crd[:,0] = crdInput[:,0]*np.sin(crdInput[:,2])*np.cos(crdInput[:,1])
        crd[:,1] = crdInput[:,0]*np.sin(crdInput[:,2])*np.sin(crdInput[:,1])
        crd[:,2] = crdInput[:,0]*np.cos(crdInput[:,2])
        return(crd)
    else:
        print("select 'deg' or 'rad' mode")

'''Points on a spherical rectangle
'''
def sphrRect(r,m,n,lSpan,eSpan,centreTheta,centrePhi):
    crdTemp = np.ndarray((m*n,3))
    crdTemp[:,0] = r
    theta = np.linspace(centreTheta-lSpan/2,centreTheta+lSpan/2,num=n)
    phi = 90-np.linspace(centrePhi-eSpan/2,centrePhi+eSpan/2,num=m)
    Theta,Phi = np.meshgrid(theta,phi)
    crdTemp[:,1] = np.reshape(Theta,m*n)
    crdTemp[:,2] = np.reshape(Phi,m*n)
    crd = sphr2Cart(crdTemp,'deg')
    return(crd)

'''A line of points centred at [0,0,0] along x/y/z axis
'''
def lineOnAxis(length,numPts,axis):
    crd = np.zeros((numPts,3))
    if axis == 'x':
        crd[:,0] = np.linspace(-length/2,length/2,num=numPts)
        return (crd)
    elif axis == 'y':
        crd[:,1] = np.linspace(-length/2,length/2,num=numPts)
        return (crd)
    elif axis == 'z':
        crd[:,2] = np.linspace(-length/2,length/2,num=numPts)
        return (crd)
    else:
        print("select axis 'x', 'y', or 'z'")

'''A line with equally distributed segments in vector form
'''
def lineVector(x0,y0,z0,i,j,k,pts):
    crd = np.ndarray((pts,3))
    for m in range (pts):
        crd[i,:] = [x0+i*m,y0+j*m,z0+k+m]
    return (crd)

'''Coordinate of a meshgrid plane from two linspance line segments
At the moment the two segments need to intersect with each other
TB-Updated in the future (?)
'''
def plane(line1,line2):

a =sphrRect(0.15,5,4,20,20,0,0)

ax = plt.axes(projection="3d")
ax.scatter3D(a[:,0],a[:,1],a[:,2],color = 'green')
io.savemat('test.mat',{'a':a})