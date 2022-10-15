import time
from  pyler import notification


if __name__=="__main__":

		notification.notify(
			title = "****Take rest**********",
			message=" DESCRIPTION HERE" ,
		
			# displaying time
			timeout=2
)
		# waiting time
		time.sleep(7)
