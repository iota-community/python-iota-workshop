# This example retrieves the balance of the given address and total balance of the given seed.
import iota_client

# *** Replace with your testing seed (In case you decided to generate one, otherwise keep this one) ***
TEST_SEED = 'a201599ad3bc079378e1e3cba43ee976828c146ec95f296c7d3a4ddc7dee24f37edba7b2bf8055503babd992964e0cb3649af6f184626636741cd9d6813b8c57'
# *** Replace with your address from the previous example ***
TEST_ADDRESS = 'atoi1qzr2qca680txhplug4dkyhyvgu3w7g7jeuw2jale2ht60el3u9el2v375fe'
# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.testnet.chrysalis2.com')

address_balance = client.get_address_balances([TEST_ADDRESS])
seed_balance = client.get_balance(TEST_SEED)
print(f"Address balance: {str(address_balance[0]['balance'])} IOTA")
print(f"Total seed balance: {str(seed_balance)} IOTA")
