from typing import Optional

from fastapi import FastAPI

from analyzer.tool import load_json, chat_info

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/chat/info")
async def get_chat_info(file_path: Optional[str] = 'result.json'):
    # Load JSON data
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    # Extract chat information
    chat_information = chat_info(data)

    return chat_information
