import os

from sanic import Sanic
from sanic.response import text

app = Sanic('app')

@app.route("/")
def test(request):
    return text('Hello world!')

# app.run(host="localhost", port=8000, debug=True)
app.run(host='0.0.0.0', port=int(os.environ['PORT']))