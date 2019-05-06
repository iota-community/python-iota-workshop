'''
This example fetches and prints transactions for a given address
'''

from iota import Iota
from iota import Transaction

import pprint

api = Iota('https://nodes.devnet.iota.org:443') 
address = 'TOKLOARHKXQCVPPVVIPIJGLUTLTKFHYGMBBLOXJFYGSARLOTYFFSDZNYCOBOCNPGRMJWZCQBNOROUCE9G'

transactions = api.find_transactions(addresses=[address,])

# We found all transactions on this address, now we need to put all hashes
# in a iterable to send it to the get_trytes function

hashes = []
for txhash in transactions['hashes']:
    hashes.append(txhash)

# Get Trytes accepts multiple Transaction Hashes
trytes = api.get_trytes(hashes)['trytes']

# get_trytes returns us a list fo raw trytes, so we need to convert them
# into transaction objects first
for trytestring in trytes:
    tx = Transaction.from_tryte_string(trytestring)
    print('\n\nTransaction %s (tag %s):' % (tx.hash, tx.tag))

    # To see what's avaialble in this object uncomment the next line
    # pprint.pprint(tx.as_json_compatible())
    
    # Get the embedded message from the Signature Mesage Fragment
    message = tx.signature_message_fragment
    print(message.decode())

