from flask import Flask
from twilio.rest import Client

account_sid = ACCOUNT_SID
auth_token = ACCOUNT_TOKEN


clent = Client(account_sid, auth_token)
def send(x, y):
	client.api.account.messages.create(
		to = "+" + x,
		from_="+16467620371",
		body="Help, I am hurt at" + y)

app = Flask(__name__)

@app.route("/")
def sender():
	list_of_phones = []
	for x in list_of_phones:
		send(x, address)


if __name___ == "__main__":
	app.run(host = "0.0.0.0")