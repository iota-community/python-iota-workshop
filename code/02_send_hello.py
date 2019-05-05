'''
This example creates a simple transaction with a custom message/tag
There is no value attached to this transaction.
'''

from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

# Note that we don't need a seed to send 0 value transactions since these
# transactions are not signed, we can publish to any address
api = Iota('https://nodes.devnet.iota.org:443') 

address = 'TOKLOARHKXQCVPPVVIPIJGLUTLTKFHYGMBBLOXJFYGSARLOTYFFSDZNYCOBOCNPGRMJWZCQBNOROUCE9G'

tx = ProposedTransaction(
    address=Address(address),
    message=TryteString.from_unicode('You did it!'),
    tag=Tag('HELLOWORLD'),
    value=0
)

tx = api.prepare_transfer(transfers=[tx])

result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)

print('Transaction sent to the tangle!')
print('https://devnet.thetangle.org/address/%s' % address)
