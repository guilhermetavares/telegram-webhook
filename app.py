import os
import requests

from sanic import Sanic
from sanic.response import text

app = Sanic('app')

@app.route("/", methods=["POST",])
async def test(request):
	BASEURL = "https://api.telegram.org/bot"
	TOKEN = "309262202:AAH2Is4bmUSOqDRzFZFvwEAokUS3iilJ8uA"
	url = BASEURL + TOKEN + "/sendMessage"
	print(url)
	response = requests.post(
		url,
		data={ "chat_id": 15343812, "text": 'my message' }).content
	return text(response)

# app.run(host="localhost", port=8000, debug=True)
app.run(host='0.0.0.0', port=int(os.environ['PORT']))