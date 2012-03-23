import numpy as N
import pylab as P

def _blob(x,y,area,colour):
    """
    Draws a square-shaped blob with the given area (< 1) at
    the given coordinates.
    """
    hs = N.sqrt(area) / 2
    xcorners = N.array([x - hs, x + hs, x + hs, x - hs])
    ycorners = N.array([y - hs, y - hs, y + hs, y + hs])
    P.fill(xcorners, ycorners, colour, edgecolor=colour)

def hinton(W, maxWeight=None):
    """
    Draws a Hinton diagram for visualizing a weight matrix. 
    Temporarily disables matplotlib interactive mode if it is on, 
    otherwise this takes forever.
    """
    reenable = False
    if P.isinteractive():
        P.ioff()
    P.clf()
    height, width = W.shape
    if not maxWeight:
        maxWeight = 2**N.ceil(N.log(N.max(N.abs(W)))/N.log(2))

    P.fill(N.array([0,width,width,0]),N.array([0,0,height,height]),'gray')
    P.axis('off')
    P.axis('equal')
    for x in xrange(width):
        for y in xrange(height):
            _x = x+1
            _y = y+1
            w = W[y,x]
            if w > 0:
                _blob(_x - 0.5, height - _y + 0.5, min(1,w/maxWeight),'white')
            elif w < 0:
                _blob(_x - 0.5, height - _y + 0.5, min(1,-w/maxWeight),'black')
    if reenable:
        P.ion()
    P.show()

l = [[1.0 for i in range(10)] for j in range(10)]
l = N.array(l)
maxW = 1.4 

l[:,1] = 5.0/6 - maxW*0.02
l[:,8] = 5.0/6 - maxW*0.02
l[1,:] = 5.0/6 - maxW*0.02
l[8,:] = 5.0/6 - maxW*0.02

l[:,0] = 4.0/6 - maxW*0.02
l[:,9] = 4.0/6 - maxW*0.02
l[0,:] = 4.0/6 - maxW*0.02
l[9,:] = 4.0/6 - maxW*0.02

l[1,0] = 3.0/6 - maxW*0.02
l[8,0] = 3.0/6 - maxW*0.02
l[0,8] = 3.0/6 - maxW*0.02
l[9,8] = 3.0/6 - maxW*0.02

l[0,0] = 2.0/6 - maxW*0.02
l[9,0] = 2.0/6 - maxW*0.02
l[0,9] = 2.0/6 - maxW*0.02
l[9,9] = 2.0/6 - maxW*0.02

# first miss in 4,4
l[4,4] = 0

l[2,4] = 5.0/6 - maxW*0.05
l[6,4] = 5.0/6 - maxW*0.05
l[4,2] = 5.0/6 - maxW*0.05
l[4,6] = 5.0/6 - maxW*0.05

l[3,4] = 4.0/6 - maxW*0.05
l[5,4] = 4.0/6 - maxW*0.05
l[4,3] = 4.0/6 - maxW*0.05
l[4,5] = 4.0/6 - maxW*0.05

hinton(N.array(l), maxW)
