'''
This example creates a simple transaction with a custom message/tag
1 iota will be transfered to the given address
'''

from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

# This is a demonstration seed, always generate your own seed!
seed = 'EDFCUGAMUKFUTSNERKXBVFTMRPGQRLFMYOHHSVCYDTZRJWULKHKRTGCEUMPD9NPFGWFTRTKLQSQRWZDMY'

# The address to send 1i
address = 'FEEDTHESHEEP999999999999999999999999999999999999999999999999999999999999999999999'

# Since we are sending value we need a seed to sign the transaction
api = Iota('https://nodes.devnet.iota.org:443', seed)

tx = ProposedTransaction(
    address=Address(address),
    message=TryteString.from_unicode('This transaction should include 1i!'),
    tag=Tag('VALUETX'),
    value=1
)

tx = api.prepare_transfer(transfers=[tx])

result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)

print('Transaction sent to the tangle!')
print('https://devnet.thetangle.org/address/%s' % address)
