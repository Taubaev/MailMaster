import json

def save_reply_to_json(reply_data, archive_file_path):
    try:
        with open(archive_file_path, 'r') as archive_file:
            data = json.load(archive_file)
    except FileNotFoundError:
        data = []

    data.append(reply_data)

    with open(archive_file_path, 'w') as archive_file:
        json.dump(data, archive_file, indent=4)
