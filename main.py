from typing import Optional

from fastapi import FastAPI

from analyzer.tool import load_json, chat_info, get_oldest_message, get_latest_message, get_senders

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
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    oldest_message = get_oldest_message(data)

    return oldest_message


@app.get("/message/latest")
async def get_latest_message_endpoint(file_path: Optional[str] = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    latest_message = get_latest_message(data)

    return latest_message


@app.get("/senders")
async def get_senders_endpoint(file_path: Optional[str] = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    senders_ranked = get_senders(data)

    return senders_ranked
