from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

origins = ["http://localhost:3000"]  # Frontend URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

rooms = {}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    print(f"Client connected to room {room_id}")

    if room_id not in rooms:
        rooms[room_id] = []

    rooms[room_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received data in room {room_id}: {data}")
            for client in rooms[room_id]:
                if client != websocket:
                    await client.send_text(data)
    except WebSocketDisconnect:
        rooms[room_id].remove(websocket)
        print(f"Client disconnected from room {room_id}")
        if not rooms[room_id]:
            del rooms[room_id]
            print(f"Room {room_id} deleted because it is empty.")
