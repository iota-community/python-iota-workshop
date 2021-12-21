# This example creates a simple message with a custom index/data.
import iota_client

INDEX = "Chrysalis Python Workshop"
DATA = "Hello World!".encode()
# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.h.chrysalis-devnet.iota.cafe/')

message_id_indexation = client.message(index=INDEX, data=DATA)

print(f"Message sent!\n https://explorer.iota.org/devnet/message/{message_id_indexation['message_id']}")
print("Copy the ID of your message. You'll need it in the next example.")
print(f"Message ID: {message_id_indexation['message_id']}")
