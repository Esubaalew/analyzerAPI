from typing import Optional

from fastapi import FastAPI

from analyzer.tool import load_json, chat_info, get_oldest_message

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/chat/info")
async def get_chat_info(file_path: Optional[str] = 'result.json'):

    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    chat_information = chat_info(data)

    return chat_information


@app.get("/message/oldest")
async def get_oldest_message_endpoint(file_path: Optional[str] = 'result.json'):
    # Load JSON data
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    # Get the oldest message
    oldest_message = get_oldest_message(data)

    return oldest_message
