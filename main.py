from typing import Optional

from fastapi import FastAPI

from analyzer.tool import load_json, chat_info, get_oldest_message, get_latest_message, get_senders, \
    get_forwarded_messages, get_forwarders, get_forward_sources, get_repliers

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


@app.get("/forwarders")
async def get_forwarder_ranking(file_path: Optional[str] = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    forwarder_ranking = get_forwarders(data)

    return forwarder_ranking


@app.get("/forward-sources")
async def get_forward_sources_count(file_path: Optional[str] = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    forward_sources_count = get_forward_sources(data)

    return forward_sources_count


@app.get("/repliers")
async def get_replier_ranking(file_path: Optional[str] = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    replier_ranking = get_repliers(data)

    return replier_ranking
