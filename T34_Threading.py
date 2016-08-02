import threading

class BuckysMessenger(threading.Thread):
	
	def run(self):
		for i in range(10):
			print(threading.currentThread().getName())

x = BuckysMessenger(name = 'Sent out messages')
y = BuckysMessenger(name = 'Receive messages')
x.start()
y.start()