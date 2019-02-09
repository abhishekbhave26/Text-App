import credentials
from twilio.rest import Client

class New():

	def send(self):
		acc,auth=credentials.account_sid,credentials.auth_token
		client=Client(acc,auth)

		num,tw=credentials.my_cell,credentials.my_twilio
		x=str(input("Please enter a message to be sent to {} :".format(num)))
		message=client.messages.create(to=num,from_=tw,body=x)

	
n=New()
n.send()