# This example generates an unused address for the provided seed.
import iota_client

# *** Replace with your testing seed (In case you decided to generate one, otherwise keep this one) ***
TEST_SEED = 'a201599ad3bc079378e1e3cba43ee976828c146ec95f296c7d3a4ddc7dee24f37edba7b2bf8055503babd992964e0cb3649af6f184626636741cd9d6813b8c57'
# Chrysalis testnet node
client = iota_client.Client(node='https://api.lb-0.h.chrysalis-devnet.iota.cafe/')

address = client.get_unspent_address(TEST_SEED)
print(f"Generated address: {address[0]}")
print("Copy your address. You'll need it in the next example.")
print("Go to https://faucet.chrysalis-devnet.iota.cafe/ and paste your address to receive devnet tokens. "
      "You'll need them in the following examples.")

