
clear c;
r=0.15;
lspan=20;
espan=20;
m=5;
n=4;
theta=-lspan/2:lspan/(n-1):lspan/2;
phi=90-(-espan/2:espan/(m-1):espan/2);
c = zeros (m*n,3);
% for i=1:m
%     for j=1:n
%         c(i,j,:) = [r  theta(1,j) phi(1,i)];
%     end
% end
[Theta,Phi]=meshgrid(theta,phi);

reshape(Theta,1,m*n);

c(:,1)=r;
c(:,2)=reshape(Theta,m*n,1);
c(:,3)=reshape(Phi,m*n,1);
c = sphrDeg2Cart(c);
figure;plot3(c(:,1),c(:,2),c(:,3),'b.');hold on;plot3(0,0,0,'rs');
%figure;plot3(a(:,1),a(:,2),a(:,3),'b.');
%==========================================================================
%Cartesian coords of rectangular HIFU concave array
%module in 3D for rectangular 32 Element HIFU array
%m Elements each row, n elements each column
%r as focal length, in meter
%eleSpan as total span of elevation angle
%latSpan as total span of lateral angle
%centreTheta as lateral centre angle of module
%centrePhi as elevation centre angle of module
%==========================================================================
function moduleCrd = recArray(r,m,n,eSpan,lSpan,centreTheta,centrePhi)
    theta = (centreTheta-lSpan/2:lSpan/n:centreTheta+...
        lSpan/2-lSpan/(2*n));
    phi = 90-(centrePhi-eSpan/2+eSpan/(2*m):eSpan/m:centrePhi+...
        eSpan/2-eSpan/(2*m));
    sphereCrd = zeros (m*n,3);
    sphereCrd(:,1) = r;
    for i = 1:m
        sphereCrd((i-1)*m+1:(i-1)*m+n,2) = theta(1,:);
    end
    sphereCrd(:,3) = repelem(phi,n);
    moduleCrd = sphrDeg2Cart(sphereCrd);
end

%==========================================================================
%Spherical to Cartesian Coordinate Conversion, with theta and phi in deg
%Input must be of size [x,3], elements in each row as r,theta,phi
%x = r cos(theta) sin(phi); y = r sin(theta) sin(phi); z = r cos(theta)
%==========================================================================
function cartesianCrd = sphrDeg2Cart(sphericalCrd)
    cartesianCrd = zeros(size(sphericalCrd));
    cartesianCrd(:,1) = sphericalCrd(:,1).*sind(sphericalCrd(:,3)).*cosd...
        (sphericalCrd(:,2));
    cartesianCrd(:,2) = sphericalCrd(:,1).*sind(sphericalCrd(:,3)).*sind...
        (sphericalCrd(:,2));
    cartesianCrd(:,3) = sphericalCrd(:,1).*cosd(sphericalCrd(:,3));
end