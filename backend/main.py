from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["https://collaborative-whiteboard-frontend-production.up.railway.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

rooms = {}

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    print(f"Client connected to room {room_id}")

    if room_id not in rooms:
        rooms[room_id] = []

    rooms[room_id].append(websocket)

    # Send updated user count to all clients
    await broadcast_user_count(room_id)

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received data in room {room_id}: {data}")

            # Forward drawing or clear events to other clients
            for client in rooms[room_id]:
                if client != websocket:
                    await client.send_text(data)

    except WebSocketDisconnect:
        rooms[room_id].remove(websocket)
        print(f"Client disconnected from room {room_id}")

        if not rooms[room_id]:
            del rooms[room_id]
            print(f"Room {room_id} deleted because it is empty.")
        else:
            # Send updated user count when someone leaves
            await broadcast_user_count(room_id)

async def broadcast_user_count(room_id: str):
    user_count_message = {
        "type": "userCount",
        "count": len(rooms[room_id])
    }

    for client in rooms[room_id]:
        await client.send_json(user_count_message)
