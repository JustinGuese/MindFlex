import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

names = ["signal strength", "attention", "meditation", "delta", "theta", "low alpha", "high alpha", "low beta", "high beta", "low gamma", "high gamma"]
plt.ion()

signals = [[],[],[],[],[],[],[],[],[],[],[]]
nrs = numpy.arange(len(signals))

def gotMessage(array):
	for i in nrs:
		signals[i].append(array[i])
	plt.cla()
	plt.plot(array,'*')
	#plt.set_xticklabels(names)
	plt.draw()
