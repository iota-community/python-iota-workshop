'''
In this example we generate 1 address with a security level of 2 (default)
for a given seed. This is the first available, unused address for this seed.
'''

from iota import Iota

# This is a demonstration seed, always generate your own seed!
seed = 'EDFCUGAMUKFUTSNERKXBVFTMRPGQRLFMYOHHSVCYDTZRJWULKHKRTGCEUMPD9NPFGWFTRTKLQSQRWZDMY'

api = Iota('https://nodes.devnet.iota.org:443', seed)

# We want the first address for this seed (index 0), make sure it hasn't been spent from before!
addresses = api.get_new_addresses(index=0, count=1, security_level=2, checksum=True)

address = addresses['addresses'][0]

print('\nThe first available address for your seed: %s' % address)
print('Go to https://faucet.devnet.iota.org and paste this address here to receive devnet tokens now\n\n')
