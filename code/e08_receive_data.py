'''
This example fetches and prints a multi-transaction JSON message for us
'''

from iota import Iota
from iota import Transaction
from iota import TryteString
import json

import pprint

api = Iota('https://nodes.devnet.iota.org:443') 
address = 'TEMPERAHKXQCVPPVVIPIJGLUTLTKFHYGMBBLOXJFYGSARLOTYFFSDZNYCOBOCNPGRMJWZCQBNOROUCE9G'

transactions = api.find_transactions(addresses=[address,])

# We found all transactions on this address, now we need to put all hashes
# in a iterable to send it to the get_trytes function

hashes = []
for txhash in transactions['hashes']:
    hashes.append(txhash)

# Get Trytes accepts multiple Transaction Hashes
trytes = api.get_trytes(hashes)['trytes']


# We need to get all trytes from all messages and put them in the right order
# We do this by looking at the index of the transaction

parts = []

for trytestring in trytes:
    tx = Transaction.from_tryte_string(trytestring)
    parts.append((tx.current_index, tx.signature_message_fragment))

parts.sort(key=lambda x: x[0])

# All that's left is to concatenate and wrap the parts in a TryteString object
full_message = TryteString.from_unicode('')

for index, part in parts:
    full_message += part

pprint.pprint(json.loads(full_message.decode()))
