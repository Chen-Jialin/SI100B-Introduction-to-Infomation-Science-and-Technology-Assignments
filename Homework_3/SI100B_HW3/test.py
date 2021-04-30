import matplotlib.pyplot as plt
import numpy as np
x = 100
y = x
plt.scatter(x,y,c = 'r')
plt.axis([0,320,0,240])
frame=plt.gca()
frame.axes.get_yaxis().set_visible(False)
frame.axes.get_xaxis().set_visible(False)
plt.show()