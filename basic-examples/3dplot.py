'''

Author: Gabriel
        http://stackoverflow.com/users/1391441/gabriel

        Chinmay Kanchi
        http://stackoverflow.com/users/148765/chinmay-kanchi

Example from stackoverflow of matplotlib
        http://stackoverflow.com/a/1986020/3921457

'''

from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pylab.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = range(0,100)
sequence_containing_y_vals = range(0,100)
sequence_containing_z_vals = range(0,100)

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

#ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)

ax.scatter(2,3,3,'z', 100,'y')
ax.scatter(2,5,3,'z', 100, 'r')
ax.scatter(100,100,100,'z', 100, 'r')

pyplot.show()
