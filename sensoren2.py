from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os

from flask import request

#variabele
CONNECTION_STR = "Endpoint=sb://service-bus-smartcity.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=SKJ78kDCvfR+6uGE7+V4fLvOL+VBAnTStd1dB9EfPAE="
QUEUE_NAME = "rpia2"

# create a Service Bus client using the connection string
servicebus_client = ServiceBusClient.from_connection_string(CONNECTION_STR, logging_enable=True)

# get a Queue Sender object to send messages to the queue
#sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)

print("receiving messages")
print("-----------------------")

with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(QUEUE_NAME)
    with receiver:
        for msg in receiver:
            print("Received: ")
            print(str(msg))
            receiver.complete_message(msg)