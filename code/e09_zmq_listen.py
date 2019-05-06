'''
Listen to the ZeroMQ data stream provided by IRI to monitor the tangle
in real time. We use the pyzmq library in this example to listen to 
new and confirmed transactions.
'''

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

# Subscribe to new transaction and confirmed transaction events
# For a list of available topics to sbuscribe to see the documentation
# https://docs.iota.org/docs/iri/0.1/references/zmq-events

socket.setsockopt(zmq.SUBSCRIBE, b'tx') # Subscribe to all new transactions, including trytes
socket.setsockopt(zmq.SUBSCRIBE, b'sn') # Subscribe to all confirmed transactions

socket.connect('tcp://zmq.devnet.iota.org:5556')

while True:
    topic, data = socket.recv().decode().split(' ', 1)
    
    if topic == 'tx':
        tx_hash, address, value, obs_tag, ts, index, lastindex, \
        bundle_hash, trunk_hash, branch_hash, received_ts, tag = data.split(' ')

        print('NEW TRANSACTION:\n\nAddress: %s\nTransaction hash: %s\nValue: %di \nTag: %s\n' % (address, tx_hash, int(value), tag))

    if topic == 'sn':
        milestone, tx_hash, address, trunk_hash, branch_hash, bundle_hash = data.split(' ')
        
        print('CONFIRMED: %s\nAddress: %s\n' % (tx_hash, address))
