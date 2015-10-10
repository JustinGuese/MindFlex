import serial
import visualizeBar
import threading
import visual2
import concRelaxPlot

try:
	ser = serial.Serial('/dev/ttyACM0', 9600)
except serial.SerialException as e:
        print("could not open serial port: {}".format(e))

counter = 0
while True:
	try:
		list = (ser.readline()).split(",")
		# we didn't get the whole string, so it's useless
		if len(list) == 11:
			print "Recieved msg no: ",counter, "signal strength: ",list[0]
			counter = counter + 1
			#visual2.gotMessage(list) # use this to get a plot
			visualizeBar.update(list)
			concRelaxPlot.update(list)
			
	except Exception:
		pass #just ignore it, sometimes pyserial throws an exception


	
