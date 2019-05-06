'''
Retreive the balance in iota for all addresses with balances for a given seed
'''

from iota import Iota
import pprint

# This is a demonstration seed, always generate your own seed!
seed = 'EDFCUGAMUKFUTSNERKXBVFTMRPGQRLFMYOHHSVCYDTZRJWULKHKRTGCEUMPD9NPFGWFTRTKLQSQRWZDMY'

api = Iota('https://nodes.devnet.iota.org:443', seed)

print('\nThe balance for your seed:\n')
pprint.pprint(api.get_account_data())
