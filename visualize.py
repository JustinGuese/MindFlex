import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#signal strength, attention, meditation, delta, theta, low alpha, high alpha, low beta, high beta, low gamma, high gamma
plt.ion()
fig = plt.figure()

signals = [[],[],[],[],[],[],[],[],[],[],[]]
nrs = numpy.arange(len(signals))


def gotMessage(array):
	for i in nrs:
		print i
		signals[i].append(array[i])
		ax = fig.add_subplot(4,4,i)
		ax.plot(signals[i])
		plt.draw()
