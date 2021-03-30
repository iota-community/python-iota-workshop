# This example creates a new instance of the IOTA Client object and prints out
# the node information of the node you are connected to.
import iota_client

# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.testnet.chrysalis2.com')
print(f'{client.get_info()}')
