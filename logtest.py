# main.py

from fastapi import FastAPI, WebSocket
import logging
import asyncio

app = FastAPI()

# 로그 설정
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# WebSocket 연결을 위한 세트
connected_clients = set()

# WebSocket 엔드포인트
class LogWebSocket(WebSocket):
    async def on_connect(self, websocket):
        await websocket.accept()
        connected_clients.add(websocket)

    async def on_disconnect(self, websocket, close_code):
        connected_clients.remove(websocket)

# 로그를 WebSocket 클라이언트에 전송하는 함수
async def send_logs_to_clients(log_message):
    for client in connected_clients:
        await client.send_text(log_message)

# 예시 API 엔드포인트
@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    await send_logs_to_clients("Root endpoint accessed")
    return {"message": "Hello, World!"}

# WebSocket 경로 등록
app.add_websocket_route("/ws", LogWebSocket)

# 5초에 한 번 로그를 생성하는 함수
async def generate_logs():
    while True:
        logger.info("Logging every 5 seconds")
        await asyncio.sleep(5)

# asyncio 이벤트 루프에서 로그 생성 함수 실행
async def start_log_generation():
    await generate_logs()

if __name__ == "__main__":
    asyncio.create_task(start_log_generation())
