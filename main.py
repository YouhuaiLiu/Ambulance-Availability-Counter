from gpio import * 
from time import *
from ioeclient import *

def setup ():
    global state
    IoEClient.setup ({
        "type": "Ambulance available",
        "states": [{
            "name": "Number Available",
            "type": "number",
            "maxValue":2
        }]
    })
    garage_counter = 0
    IoEClient.reportStates(2)

def Loop():
	garage1 = customRead(0)
	garage2 = customRead(1)
	if(garage1 == "1" and garage2 =="0"):
		IoEClient.reportStates(1)
	if(garage1 == "1" and garage2 =="1"):
		IoEClient.reportStates(0)
	if(garage1 == "0" and garage2 =="0"):
		IoEClient.reportStates(2)
	if(garage1 == "0" and garage2 =="1"):
		IoEClient.reportStates(1)
	sleep(1)

if __name__ == "__main__":
    setup()
    while True:
    	Loop()



from gpio import * 
from time import *
from ioeclient import *

def setup ():
    global state
    IoEClient.setup ({
        "type": "Ambulance available",
        "states": [{
            "name": "Number Available",
            "type": "number",
            "maxValue":2
        }]
    })
    garage_counter = 0
    IoEClient.reportStates(2)

def Loop():
	garage1 = customRead(0)
	garage2 = customRead(1)
	if(garage1 == "1" and garage2 =="0"):
		IoEClient.reportStates(1)
	if(garage1 == "1" and garage2 =="1"):
		IoEClient.reportStates(0)
	if(garage1 == "0" and garage2 =="0"):
		IoEClient.reportStates(2)
	if(garage1 == "0" and garage2 =="1"):
		IoEClient.reportStates(1)
	sleep(1)

if __name__ == "__main__":
    setup()
    while True:
    	Loop()



