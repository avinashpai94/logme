from google.cloud import pubsub_v1

def send_message(project_id, topic_name, data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    data = data.encode("utf-8")
    print(data)
    future = publisher.publish(topic_path, data = data)
    print(future.result())

    print("Published messages.")
# .\venv\Scripts\activate & set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\anj24\Downloads\errorlogger-d5dc9028e1af.json
