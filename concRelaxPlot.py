import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
import time

names = ["Relaxation","Concentration"]

signals = [[],[]]
plt.ion()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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
    #decide what state we are in
    if signals[0][-2]<relax_Value and signals[1][-2]>concentrate_Value:
	#if current relax_Val over average & current conc_Val below average
	# means definitely chill
	print (bcolors.GREEN + "Definitely Chill!" + bcolors.ENDC)
    if signals[0][-2]>relax_Value and signals[1][-2]<concentrate_Value:
	#other way around, definitely concentration
	print (bcolors.FAIL + "Definitely Concentration!" + bcolors.ENDC)
    if (signals[0][-2]<relax_Value and signals[1][-2]<concentrate_Value) or (signals[0][-2]>relax_Value and signals[1][-2]>concentrate_Value):
	# both below or above average
	if relax_Value < concentrate_Value:
		print "Maybe Concentration"
	if concentrate_Value < relax_Value:
		print "Maybe Relaxation"
    animated_barplot()

	

#fig = plt.figure()
#win = fig.canvas.manager.window
#win.after(100, animated_barplot)
#plt.draw()
