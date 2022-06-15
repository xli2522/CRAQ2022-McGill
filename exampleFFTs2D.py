"""Load an image, calc mags and phases, save mags and phase images.
"""

import numpy
from numpy import fft
import pylab
from scipy import ndimage
import matplotlib.image as image
import matplotlib.colors as colors
import IPython

#-------------------------------------------------------------------------------------------------------------
def makeRMap(x, y, data):
    """Returns an array that gives radial distance to given coords.
    """
    xPix=numpy.array([numpy.arange(0, data.shape[1], dtype=float)]*data.shape[0])-x
    yPix=(numpy.array([numpy.arange(0, data.shape[0], dtype=float)]*data.shape[1])-y).transpose()
    rPix=numpy.sqrt(xPix**2+yPix**2)

    return rPix

#-------------------------------------------------------------------------------------------------------------
def makeCircleArray(x, y, radius, arrWidth):
    """Returns an array with a circle of given radius drawn at coords x, y.
    """
    arr=numpy.zeros([arrWidth, arrWidth])
    rMap=makeRMap(x, y, arr)
    arr[numpy.less(rMap, radius)]=1.0
    
    return arr

#-------------------------------------------------------------------------------------------------------------
def makeBoxArray(x, y, boxWidth, boxHeight, arrWidth, rotationDeg = 0):
    """Returns an array with a box of given dimensions (boxWidth,
    boxHeight) drawn centered on coordinates x, y within a square
    array of size arrWidth.  Optionally specify a rotation angle for
    the box.
    """
    arr=numpy.zeros([arrWidth, arrWidth])
    halfWidth=boxWidth//2
    halfHeight=boxHeight//2
    arr[y-halfHeight:y+halfHeight, x-halfWidth:x+halfWidth]=1.0

    if rotationDeg != 0:
        arr=ndimage.rotate(arr, rotationDeg, reshape = False)
    
    return arr

#-------------------------------------------------------------------------------------------------------------
def saveImage(arr, fileName, logScaling = False, title = None):
    """Save image.
    """
    pylab.figure(figsize=(8, 8))
    if logScaling == False:
        pylab.imshow(arr, cmap=pylab.get_cmap('gray'))
    else:
        pylab.imshow(arr, cmap=pylab.get_cmap('gray'), norm=colors.LogNorm(vmin=1e-2, vmax=arr.max()))
    pylab.colorbar()
    if title is not None:
        pylab.title(title)
    pylab.savefig(fileName)
    print('Close the plot to continue')
    pylab.show()
    
#-------------------------------------------------------------------------------------------------------------
# Main

if __name__ == '__main__':

    # Make a 2D image that you'll FFT.  A few examples are included
    # below; uncomment the one that you want (by deleting the "#"
    # character at the beginning of the line).  Experiment with the
    # inputs by changing the numbers in the parentheses -- make sure
    # you know what they are.

    arr=makeCircleArray(128, 128, 32, 256)  # circle
    #arr=makeBoxArray(128, 128, 16, 32, 256)  # small filled box
    #arr=makeBoxArray(128, 128, 16, 32, 256, rotationDeg = 45)
    #arr=makeBoxArray(64, 128, 16, 32, 256, rotationDeg = 20)

    # Save input image we made
    saveImage(arr, "input.png", title='Input image')

    # Take the FFT
    farr=fft.fft2(arr)

    # Calculate magnitude and phase
    mags = abs(farr)
    phases = numpy.angle(farr)

    # Save FFT images - use log scaling for mags image
    saveImage(fft.fftshift(mags), "mags.png", logScaling = True, title='FFT magnitude')
    saveImage(fft.fftshift(phases), "phases.png", logScaling = False, title='FFT phase')
