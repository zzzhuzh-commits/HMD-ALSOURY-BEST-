queues = {}

def add_to_queue(chat_id, item):
    if chat_id not in queues:
        queues[chat_id] = []

    queues[chat_id].append(item)

def get_queue(chat_id):
    return queues.get(chat_id, [])

def clear_queue(chat_id):
    if chat_id in queues:
        queues[chat_id] = []
