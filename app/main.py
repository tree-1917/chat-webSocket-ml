from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import json  # Import the json module

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Private Chat with WebSocket</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    </head>
    <body>
        <div class="container mt-3">
            <h1>Private Chat with WebSocket</h1>
            <h2>Your ID: <span id="ws-id"></span></h2>
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" class="form-control" id="targetId" placeholder="Enter target ID" autocomplete="off"/>
                <input type="text" class="form-control mt-2" id="messageText" placeholder="Enter message" autocomplete="off"/>
                <button class="btn btn-outline-primary mt-2">Send</button>
            </form>
            <ul id="messages" class="mt-5"></ul>
        </div>
        <script>
            var client_id = Date.now();
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('li');
                var content = document.createTextNode(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            };
            
            function sendMessage(event) {
                var targetId = document.getElementById("targetId").value;
                var input = document.getElementById("messageText").value;
                var message = JSON.stringify({ "target_id": targetId, "message": input });
                ws.send(message);
                event.preventDefault();
            }
        </script>
    </body>
</html>
"""

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: int):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: int):
        self.active_connections.pop(client_id, None)

    async def send_personal_message(self, message: str, target_id: int):
        target_connection = self.active_connections.get(target_id)
        if target_connection:
            await target_connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            data_json = json.loads(data)  # Parse JSON data
            target_id = int(data_json["target_id"])
            message = data_json["message"]
            await manager.send_personal_message(f'Client #{client_id} says: {message}', target_id)
    except WebSocketDisconnect:
        manager.disconnect(client_id)
