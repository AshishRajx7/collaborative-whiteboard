# Collaborative Whiteboard

A real-time collaborative whiteboard that allows multiple users to draw together in shared rooms. Built with FastAPI WebSockets, React, Docker, and Railway. Each room is uniquely generated and fully isolated for seamless multi-user sessions.

---



## Tech Stack

- **Frontend:** React, React Router, WebSockets, React Color
- **Backend:** FastAPI, WebSockets
- **Deployment:** Docker, Railway
- **Version Control:** Git, GitHub

---

## Key Features

- Real-time Collaborative Drawing
- Dynamic Room Generation and Joining
- Fast WebSocket Communication
- Multi-User Sessions per Room
- Dockerized Backend
- Deployed on Railway (Frontend & Backend)

---

## Project Structure

```text
collaborative-whiteboard/
├── backend/           # FastAPI WebSocket backend
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/          # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
└── docker-compose.yml
Getting Started (Local Setup)
Prerequisites
Docker installed

Node.js and npm installed

Backend Setup
bash
Copy
Edit
cd backend
docker build -t collaborative-whiteboard-backend .
docker run -d -p 5000:5000 collaborative-whiteboard-backend
Frontend Setup
bash
Copy
Edit
cd frontend
npm install
npm start
Open http://localhost:3000 to use the app locally.

Deployment
Backend and Frontend are deployed on Railway.

Automated builds and redeployments are triggered via GitHub push using the Dockerfile.

Future Enhancements
Real-time user count (partially integrated)

In-room chat feature

"User is drawing..." indicators

Undo/Redo functionality

UI polish with animations

Responsive design
