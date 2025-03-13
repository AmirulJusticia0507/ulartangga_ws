import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "WebSocket connected!"
        }))

    async def disconnect(self, close_code):
        print("Disconnected:", close_code)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")

        # Kirim kembali pesan ke client
        await self.send(text_data=json.dumps({
            "message": message
        }))
