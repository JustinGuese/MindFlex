import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
import time

names = ["Relaxation","Concentration"]

signals = [[],[]]
plt.ion()

def animated_barplot():
    plt.subplot(211)
    plt.cla()
    N = 2
    plt.plot(range(len(signals[0])), signals[0],label="Relaxation")
    plt.plot(range(len(signals[1])), signals[1],label="Concentration")
    plt.legend()
    plt.draw()

def update(array):
    # array is a string array, so let's convert it to float
    relax_Value=(float(array[5])+float(array[6]))
    concentrate_Value=(float(array[7])+float(array[8]))
    signals[0].append(relax_Value)
    signals[1].append(concentrate_Value)
    animated_barplot()

	

#fig = plt.figure()
#win = fig.canvas.manager.window
#win.after(100, animated_barplot)
#plt.draw()
