import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np

names = ["signal strength", "attention", "meditation", "delta", "theta", "low alpha", "high alpha", "low beta", "high beta", "low gamma", "high gamma"]

signals = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
plt.ion()

def animated_barplot():
    plt.subplot(212)
    plt.cla()
    N = 11
    rects = plt.bar(range(N), signals,  align = 'center')
    plt.xticks(np.arange(N),names,rotation="vertical")
    maximum = max(signals)
    for rect, h in zip(rects, signals):
    	rect.set_height(h)
    plt.draw()

def update(array):
    print "got update"
    # array is a string array, so let's convert it to float
    for i in range(len(array)):
	signals[i]=float(array[i])
    animated_barplot()
	

#fig = plt.figure()
#win = fig.canvas.manager.window
#win.after(100, animated_barplot)
#figure1.draw()
