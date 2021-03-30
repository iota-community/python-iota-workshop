# This example creates a data transaction split over multiple messages.
# May come in handy with big messages exceeding 32768 byte limit
import iota_client

INDEX = "Chrysalis Python Workshop"
DATA = ("Chrysalis Python Workshop|" * 10).encode()     # 260 characters
CHUNK_SIZE = 128                                        # Split into multiple 128 character messages
# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.testnet.chrysalis2.com')

counter = 1
message_ids = []
while len(DATA):
    message_id_indexation = client.message(index=INDEX, data=DATA[:128])
    print('Message ' + str(counter) + " sent!")
    print("https://explorer.iota.org/chrysalis/message/" + message_id_indexation['message_id'])
    message_ids.append(message_id_indexation['message_id'])
    DATA = DATA[128:]
    counter += 1

print("\nCopy IDs of your messages. You'll need them in the next example.")
print(f'Message IDs: {str(message_ids)}')
