import pylab
import numpy as np

# Set up the x-values for the function:
x=np.arange(-np.pi,np.pi,0.01) 

# Set maximum number of iterations
i_max = 10

# Initialise values
sqwave = 0.0
b = 1.0

# Now we sucessively add up a series of sine waves to make an
# ever-better approximation of a square wave:

for iplot in range(1, i_max):
    pylab.figure(figsize=[15,6])
    
    # On the left side, overplot all sine waves that we want to add
    # together
    pylab.subplot(121)
    sqwave = 0.0
    for i in range(iplot):
        # New component
        b = float(i*2 + 1)
        component = (1/b)*np.sin(b*x)
        # Add that component to our existing wave
        sqwave = sqwave+component
        # Plot the new component on the left, the sum on the right
        pylab.plot(x,component)
    pylab.xlabel('Time')
    pylab.ylabel('Amplitude (real)')
    pylab.title('Sinusoidal components ('+str(iplot)+' of '+str(i_max)+')')

    # On the right side, plot the total sum
    pylab.subplot(122)
    pylab.plot(x,sqwave)
    pylab.xlabel('Time')
    pylab.ylabel('Amplitude (real)')
    pylab.title('Sum of '+str(iplot)+' sines')

    # Save the plot for future reference
    outfile = 'sqwave_'+str(iplot).zfill(2)+'.png'
    pylab.savefig(outfile)
    print ('Wrote',outfile)

    # Show the plot, then get ready for the next plot
    print('Close the plot to continue')
    pylab.show()
    
    # Close this plot and move on to the next iteration
    pylab.close()
