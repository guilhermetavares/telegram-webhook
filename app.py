from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

@app.route("/")
def test(request):
    return text('Hello world!')

# app.run(host="localhost", port=8000, debug=True)
