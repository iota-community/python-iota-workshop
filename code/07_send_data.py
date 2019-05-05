'''
This example creates a data transaction split over multiple messages
There is no value attached to this transaction.
'''

from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

import json

# Note that we don't need a seed to send 0 value transactions since these
# transactions are not signed, we can publish to any address
api = Iota('https://nodes.devnet.iota.org:443') 
address = 'TEMPERAHKXQCVPPVVIPIJGLUTLTKFHYGMBBLOXJFYGSARLOTYFFSDZNYCOBOCNPGRMJWZCQBNOROUCE9G'

# We generate a dataset that has to be split over multiple transactions,
# It's too much to fit into a single transaction. The library will split it for 
# us.
data = [{'temperature': '20.1', 'humidity': '72'}] * 50

tx = ProposedTransaction(
    address=Address(address),
    message=TryteString.from_unicode(json.dumps(data)),
    tag=Tag('TEMPERATURE'),
    value=0
)

tx = api.prepare_transfer(transfers=[tx])

result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)

print('Transaction sent to the tangle!')
print('https://devnet.thetangle.org/address/%s' % address)
