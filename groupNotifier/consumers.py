from channels.generic.websocket import WebsocketConsumer
import json

class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("connected")

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if (message == 'hello'):
            self.send(text_data=json.dumps({
                'message': "hi"
            }))
        else: 
            self.send("Fuck you")