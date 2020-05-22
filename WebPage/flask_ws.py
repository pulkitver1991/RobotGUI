from flaskws import WsMiddleware
from flaskws import ws_server, WsError, OP_TEXT
from flaskws import ws_server_view
from flaskws import ws_connect
from flask import Flask, flash, redirect, render_template, request, session
	

app = Flask(__name__, template_folder='templates')
app.wsgi_app = WsMiddleware(app.wsgi_app)
# app.run()


@app.route('/ws/<int:oops>')
@ws_server
class WebsocketServer(object):

	def __init__(self, ws_sock, **req_args):
		self.ws_sock = ws_sock
		print req_args['oops']

	def on_open(self, ws_sock): pass

	def on_message(self, ws_sock, frame):
		fin, op, payload = frame

	def on_close(self, ws_sock): pass


@app.route('/ws/<int:oops>')
@ws_server_view
def my_ws_echo_server(ws_sock, oops=None):
	while True:
		frame = ws_sock.recv(timeout=5.0)
		if frame:
			fin, op, msg = frame
			if msg:
				ws_sock.send(msg)
				if msg == 'close':
					break


with ws_connect('ws://0.0.0.0/8080') as c:
	if c.handshake():
		c.send('hello!')
		for frame in c:
			print frame					