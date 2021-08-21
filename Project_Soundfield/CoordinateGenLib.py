#============================================================================#
#Numpy-based Spatial (R3 Space) Geometry Generation Lib                    #
#Specialised in generating coordinate arrays that can be visualised w/ plot3d#
#============================================================================#
import numpy as np

'''Define a point in R3 space
(Euclidean space / cartesian coordinate, however you call it)
Wrap around a regular 1D list to 2D numpy array
I wrote it like this just because I got addicted to Matlab
'''
def pt(x,y,z):
    return (np.asarray([[x,y,z]]))

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

'''Find intersection coordinate for two vectors known to have a crossing point
https://blog.csdn.net/Mr_HCW/article/details/82856056
'''
def intersectPt(vec1,vec2):
    dir1 = vec1[-1,:]-vec1[0,:]
    dir2 = vec2[-1,:]-vec2[0,:]
    d1 = vec1[1,:]-vec1[0,:]
    d2 = vec2[1,:]-vec2[0,:]
    A1B1 = vec2[0,:]-vec1[0,:]
    A1B2 = vec2[-1,:]-vec1[0,:]
    d1 = np.linalg.norm(np.cross(A1B1,dir1))/np.linalg.norm(dir1)
    d2 = np.linalg.norm(np.cross(A1B2,dir1))/np.linalg.norm(dir1)
    x = dir2*d1/(d1+d2)+vec2[0,:]   #crossing point
    return (x)

'''Coordinate of a meshgrid plane from two linspance vectors
At the moment the two segments need to intersect with each other
TB-Updated in the future (?)
Algorithm:
1. Find intersection point coordinate 
Find orthogonal distance from the two ends of vector2 to vector1
2. Find mid-point of the starting point of two vectors
3. Construct plane using meshgrid & directional vectors,
start from mirror point of intersection point to mid point of initial vectors
'''
def planeGrid(vec1,vec2):
    m = vec1.shape[0]
    n = vec2.shape[0]
    pln = np.ndarray(shape=(m*n,3))
    x = intersectPt(vec1,vec2)
    s = vec1[0,:] + vec2[0,:] -x #starting point of the plane
    d1 = vec1[1,:]-vec1[0,:]
    d2 = vec2[1,:]-vec2[0,:]
    for i in range(m):
        for j in range(n):
            pln[(i-1)*n+j,:]=s+i*d1+j*d2
    return (pln)

'''Coordinate of points on a concave curve on x-y plane
'''
def concave(r,numPts,l):
    crdTemp = np.zeros((numPts,3))
    crdTemp[:,0] = r
    crdTemp[:,1] = np.linspace(-np.arcsin(l/2/r),np.arcsin(l/2/r),num=numPts)
    crdTemp[:,2] = np.deg2rad(90)
    crd = sphr2Cart(crdTemp,'rad')
    crd[:,0] = crd[:,0]-np.max(crd[:,0])
    return (crd)
#a =sphrRect(0.15,5,4,20,20,0,0)

#ax = plt.axes(projection="3d")
#ax.scatter3D(a[:,0],a[:,1],a[:,2],color = 'green')
#io.savemat('test.mat',{'a':a})


