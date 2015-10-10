import numpy as np
import matplotlib.pyplot as plt

signals = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
counter = 1
names = ["signal strength", "attention", "meditation", "delta", "theta", "low alpha", "high alpha", "low beta", "high beta", "low gamma", "high gamma"]

plt.ion()

def gotMessage(array):
	global counter,signals
	newArray = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
	for i in range(len(array)):
		newArray[i]=float(array[i])
	counter = counter + 1
	for i in range(len(newArray)):
		signals[i]=float((signals[i]+newArray[i])/counter)
	print "average" , signals
	plt.clf()
	plt.plot(signals,'-',label="average")
	plt.plot(array,'o',label="current")
	plt.xlim([-1,12])
	plt.xticks(np.arange(11),names,rotation="vertical")
	plt.legend()
	plt.draw()



