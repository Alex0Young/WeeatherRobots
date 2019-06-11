from flask import  Flask ,request,render_template
from  geventwebsocket.websocket import WebSocket,WebSocketError
from  geventwebsocket.handler import WebSocketHandler
from  gevent.pywsgi import WSGIServer
import getUnit as gu
import json

app = Flask(__name__)

# def HandleSession(msg):
#     res,state, bot_session = gu.getRecv(msg)
#     if state == 0:      #failure
#         return res
#     if state == 1:      #success
#         return res
#     if state == 2:      #clarify time



@app.route('/index/')
def index():
    return render_template('one2one.html')

user_socket_list = []
user_socket_dict={}

@app.route('/webchat/<username>')
def ws(username):
    user_socket=request.environ.get("wsgi.websocket")
    if not user_socket:
        return "请以WEBSOCKET方式连接"

    user_socket_dict[username]=user_socket
    print(user_socket_dict)
    state = 1
    bots=''
    while True:
        try:        #接受前端信息发送给其他人
            user_msg = user_socket.receive()
            user_msg=json.loads(user_msg)
            print(type(user_msg))
            to_user_socket = user_socket_dict.get(user_msg.get("username"))
            uip = user_msg.get("uip")
            send_msg={
                "send_msg":user_msg.get("send_msg"),
                "send_user":username,
                "uip":user_msg.get("uip")
            }
            if state == 1:
                res, state, bots = gu.getRecv(json.dumps(send_msg),1,bots,uip)
            elif state == 2:
                res, state, bots = gu.getRecv(json.dumps(send_msg),2,bots,uip)
            elif state == 3:
                res, state, bots = gu.getRecv(json.dumps(send_msg),3,bots,uip)
            elif state == 0:
                res, state, bots = gu.getRecv(json.dumps(send_msg),0,bots,uip)
            print(type(res))
            sendmsg={
                "send_msg": res,
                "send_user":username
            }
            to_user_socket.send(json.dumps(sendmsg))
        except WebSocketError as e:
            user_socket_dict.pop(username)
            print(user_socket_dict)
            print(e)


if __name__ == '__main__':
    http_serve=WSGIServer(("0.0.0.0",5000),app,handler_class=WebSocketHandler)
    http_serve.serve_forever()
