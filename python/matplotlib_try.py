import numpy as np
import matplotlib.pyplot as plt
plt.plot([1, 12, 3, 9])
#plt.ylabel('some numbers')
#plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#plt.show()

#plt.axis([x_min, x_max, y_min, y_max])
#plt.axis([0, 6, 0, 20])
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
#plt.show()

t = np.arange(0, 5, 0.2)
plt.plot(t, t*t, 'g^')
plt.show()