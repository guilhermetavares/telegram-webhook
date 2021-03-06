import os
import requests
import json

from sanic import Sanic
from sanic.response import text


app = Sanic('app')


def send_balance(token):
    HEADERS = {
        'Access-Token': token,
        'content-type': 'application/json',
    }
    url = 'https://api.totalvoice.com.br/composto'
    return json.loads(requests.post(url, json=data, headers=HEADERS).content.decode())


def send(from_, to, token):
    HEADERS = {
        'Access-Token': token,
        'content-type': 'application/json',
    }
    url = 'https://api.totalvoice.com.br/composto'
    data = {
        'numero_destino': to,
        'dados': [
            {
                'acao': 'audio',
                'acao_dados': {
                    'url_audio': 'https://github.com/haskellcamargo/gemidao-do-zap/raw/master/resources/gemidao.mp3'
                }
            }
        ],
        'bina': from_
    }
    return json.loads(requests.post(url, json=data, headers=HEADERS).content.decode())


@app.route("/", methods=["POST", "GET"])
async def test(request):
    
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    BASEURL = "https://api.telegram.org/bot{0}/sendMessage".format(TELEGRAM_TOKEN)

    token = None
    try:
        data = json.loads(request.body.decode())
    except:
        return text('PING')

    message = data.get('message', {}).get('text')
    chat_id = data.get('message', {}).get('chat', {}).get('id')
    post_message = 'Please uses /start, /help or /call!'
    
    if '/start' in message or '/help' in message:
        post_message = '''Make a register in http://www.totalvoice.com.br/, and send:
/call TOKEN NUMBER_FROM NUMBER_TO'''
    elif '/balance' in message:
        action, token = message.split()
        data = send(from_n, to_n, token)
        post_message = '{0}'.format(data.get('dados').get('saldo'))
    elif '/call' in message:
        try:
            action, token, from_n, to_n = message.split()
            post_message = 'calling to {0}, wait for the OOOWH AHHHWN WOOOO AAAAHN WAAAAA AAAAAAHN ANN WAAA!'.format(to_n)
        except:
            post_message = '''You must use "/call TOKEN NUMBER_FROM NUMBER_TO"'''

        if token:
            data = send(from_n, to_n, token)

            if data.get('status') in [405, 403, 400, 401, 500]:
                post_message = data.get('mensagem')

    response = requests.post(
        BASEURL,
        data={ "chat_id": chat_id, "text": post_message}).content
    return text(response)

app.run(host='0.0.0.0', port=int(os.environ['PORT']))
