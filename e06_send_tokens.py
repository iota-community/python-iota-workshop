# This example creates a transaction with a custom index/data.
# The amount of iota specified in the "amount" variable will be transferred to the given address.
import iota_client

# *** Replace with your testing seed (In case you decided to generate one, otherwise keep this one) ***
SENDER_SEED = 'a201599ad3bc079378e1e3cba43ee976828c146ec95f296c7d3a4ddc7dee24f37edba7b2bf8055503babd992964e0cb3649af6f184626636741cd9d6813b8c57'
RECIPIENT_ADDRESS = 'atoi1qz8wn7fj23g3qz8rpk9dk38zffs6u7wmdalvu7eak8a5r7me72pw2vspcl0'
INDEX = "Chrysalis Python Workshop"
DATA = "Here are your IOTAs!".encode()
# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.h.chrysalis-devnet.iota.cafe/')

output = {
    'address': RECIPIENT_ADDRESS,
    'amount': 2000000  # 2 MIOTA
}

message_id = client.message(seed=SENDER_SEED, index=INDEX, data=DATA, outputs=[output])
print(f"IOTAs sent!\n https://explorer.iota.org/devnet/message/{message_id['message_id']}")
