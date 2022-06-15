"""Fourier transforms of some common functions
"""

# These import commands load various python modules that contain
# functions that we'll need later on:
# - "numpy" stands for numerical python, and this module contains the
#   FFT routines that we'll be using
# - "scipy" stands for scientific python, and this module contains a
#   stats package that we'll use for calculating a Gaussian
# - "pylab" is a plotting module
import numpy
import numpy.fft as fft
from scipy import stats
import pylab


# The following section of code contains custom-built functions, and
# detailed information is in the comments.  For example, "makeFFTPlot"
# is a function that calculates and plots the FFT of an array of data
# (specified by the input variable "arr").

#-------------------------------------------------------------------------------------------------------------
def deltaFunction(N, x):
    """Returns an array of length N containing a delta function at location x.
    """
    arr=numpy.zeros(N, dtype = float)
    arr[x]=1.0
    return arr

#-------------------------------------------------------------------------------------------------------------
def gaussian(N, x0, sigma):
    """Returns an array of length N containing a Gaussian function, centred at x0 and with specified sigma
    """
    x=numpy.linspace(-x0, N-x0, N)
    y=stats.norm.pdf(x, 0, sigma)
    x=x+N/2
    return y
    
#-------------------------------------------------------------------------------------------------------------
def boxcar(N, x0, x1):
    """Returns an array of length N containing a boxcar between x0 and x1
    """
    arr=numpy.zeros(N, dtype = float)
    arr[x0:x1]=1.0
    return arr

#-------------------------------------------------------------------------------------------------------------
def makeFFTPlot(arr, label):
    """Makes a 3-panel figure containing plot of a function, it's FFT, and the inverse FFT of the FFT'ed
    function (to show we get back what we put in). Use label to set part of title (e.g., gaussian), and
    the output file name.
    """
    
    # Create a new figure
    pylab.figure(figsize=(15, 6))

    # In the first subplot, show the original data to be transformed
    pylab.subplot(1, 3, 1)
    pylab.plot(arr)
    pylab.xlim(0, len(arr))
    pylab.title(label)

    # Calculate the Fourier transform of the input data, which is
    # stored in variable "arr".  The input is assumed to be complex,
    # and the output is also an array of complex numbers.
    farr=fft.fft(arr)

    # In the second subplot, show the magnitude of the FFT
    pylab.subplot(1, 3, 2)
    pylab.plot(numpy.abs(farr))
    pylab.xlim(0, len(farr))
    pylab.title("FFT magnitude of %s" % (label))

    # In the second subplot, show the phase of the FFT (and unwrap the angle)
    pylab.subplot(1, 3, 3)
    pylab.plot(numpy.unwrap(numpy.angle(farr)))
    pylab.xlim(0, len(farr))
    pylab.title("FFT phase of %s" % (label))

    # Save the plot to a png file, and show the results to the human.
    outfile = "%s.png" % (label.replace(" ", "_"))
    pylab.savefig(outfile)
    print('Saved plot as',outfile)
    print( "Close plot to continue")
    pylab.show()
    
    # Close the plot and move on...
    pylab.close()
    
#-------------------------------------------------------------------------------------------------------------
# The main part of the program starts here.  The following lines are
# what actually executes when you run the code.  You can try
# commenting out various lines with the "#" symbol to see how that
# affects the running of the code.

if __name__ == '__main__':

    # Delta function
    print('Generating and plotting delta function')
    delta=deltaFunction(128, 0)
    makeFFTPlot(delta, "Delta Function")
    
    # Boxcar
    print('Generating and plotting boxcar')
    box=boxcar(128, 0, 16)
    makeFFTPlot(box, "Box Car")
    
    # Gaussian
    print('Generating and plotting Gaussian')
    gauss=gaussian(128, 0, 16)
    makeFFTPlot(gauss, "Gaussian")

