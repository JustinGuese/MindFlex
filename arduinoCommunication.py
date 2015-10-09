import serial
import visualize
import threading

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
			print "Recieved msg no: ",counter
			counter = counter + 1
			visualize.gotMessage(list)
	except Exception:
		pass #just ignore it, sometimes pyserial throws an exception


	
