# This example fetches and prints a multi-transaction message.
import iota_client

# *** Replace with IDs from the previous example ***
MESSAGE_IDS = ['3f0ad429395d2990a32f1bd31e5787931dea2ab4ad2035c1d554bb4dbf3dd34d',
               '26894efc6fe60cd1660e52780c5f3e167cd23d3a1f64175a1c226181e8e803e7',
               'b48ca2a18303010b8f9736b5b8bb85eb959e2ac87561e15c88fc57a76a9de48f']
# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.h.chrysalis-devnet.iota.cafe/')
full_message = ""
for x in range(len(MESSAGE_IDS)):
    message = client.get_message_data(MESSAGE_IDS[x])
    message_index = message['payload']['indexation'][0]['index']
    message_content = message['payload']['indexation'][0]['data']
    full_message += bytes(message_content).decode()
    # Additional message information, feel free to uncomment following lines
    # print(f'Message {x + 1} data: {message}')
    # print(f'Message {x + 1} index: {bytes.fromhex(message_index).decode("utf-8")}')
    print(f'Message {x + 1} content: {bytes(message_content).decode()}')
    print(f'Message {x + 1} length: {len(bytes(message_content).decode())} bytes')

print(f'\nResulting message: {full_message}')
print(f'Resulting message length: {len(full_message)} bytes')
