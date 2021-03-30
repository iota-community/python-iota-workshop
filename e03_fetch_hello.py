# This example fetches and prints a message with the given ID.
import iota_client

# *** Replace with the ID you got from the previous example ***
MESSAGE_ID = 'fc464e422f5dcb612c4e303172d7077281aada6cfe61e3d786d34ff97dc99a64'
# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.testnet.chrysalis2.com')

message = client.get_message_data(MESSAGE_ID)
message_index = message['payload']['indexation'][0]['index']
message_content = message['payload']['indexation'][0]['data']
print(f'Message data: {message}')
print(f'Message index: {bytes.fromhex(message_index).decode("utf-8")}')
print(f'Message content: {bytes(message_content).decode()}')
