from typing import Optional

from fastapi import FastAPI

from analyzer.tool import load_json, chat_info, get_oldest_message, get_latest_message, get_senders, \
    get_forwarded_messages, get_forwarders, get_forward_sources, get_repliers, get_editors, get_most_common_words, \
    each_average_message_length, get_most_active_hours, get_most_active_weekdays, get_most_active_months, \
    get_user_activity

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


@app.get("/editors")
async def get_editor_ranking(file_path: Optional[str] = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    editor_ranking = get_editors(data)

    return editor_ranking


@app.get("/common-words")
async def get_most_common_words_endpoint(file_path: Optional[str] = 'result.json', top_n: Optional[int] = 10):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    most_common_words = get_most_common_words(data, top_n)

    return most_common_words


@app.get("/average-message-length")
async def calculate_average_message_length(file_path: Optional[str] = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    average_lengths = each_average_message_length(data)

    return average_lengths


@app.get("/most-active-hours")
async def calculate_most_active_hours(file_path: str = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    active_hours = get_most_active_hours(data)
    active_hours = [{'hour': hour, 'messages': count} for hour, count in active_hours]

    return active_hours


@app.get("/most-active-weekdays")
async def calculate_most_active_weekdays(file_path: str = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    active_weekdays_counter = get_most_active_weekdays(data)

    active_weekdays_dict = {weekday: count for weekday, count in active_weekdays_counter}

    return active_weekdays_dict


@app.get("/most-active-months")
async def calculate_most_active_months(file_path: str = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    active_months_counter = get_most_active_months(data)

    active_months_dict = {month: count for month, count in active_months_counter}

    return active_months_dict


@app.get("/user-activity")
async def analyze_user_activity(file_path: str = 'result.json'):
    data = load_json(file_path)
    if data is None:
        return {"message": "Failed to load JSON data"}

    user_activity = get_user_activity(data)

    for user, activity_info in user_activity.items():
        activity_info.pop('Overall', None)

    return user_activity
