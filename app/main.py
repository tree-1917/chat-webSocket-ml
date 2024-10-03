from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import json  # Import the json module
from pathlib import Path

app = FastAPI()

# Load the HTML content from the index.html file
html_file_path = Path(__file__).parent / "index.html"
html_content = html_file_path.read_text()

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
    return HTMLResponse(content=html_content)

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
