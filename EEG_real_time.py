"""
Mind Monitor - Minimal EEG OSC Receiver
Coded: James Clutterbuck (2021)
Requires: pip install python-osc
"""
from datetime import datetime
from pythonosc import dispatcher
from pythonosc import osc_server
import numpy as np
import argparse

ip = "0.0.0.0"
port = 5000


fs = 256

n_channels = 1

# Length of the EEG data buffer (in seconds)
# This buffer will hold last n seconds of data and be used for calculations
buffer_length = 30

eeg_buffer = []
#eeg_buffer = np.zeros((int(fs * buffer_length), n_channels))
counter = 0


def update_buffer(data):
    if(len(eeg_buffer) < int(fs * buffer_length)):
        eeg_buffer.append(data)
        print(len(eeg_buffer))
        return False
    else:
        print(len(eeg_buffer))
        print("clear!")
        eeg_buffer.clear()
        while len(eeg_buffer) != 0: {}
        print(len(eeg_buffer))
        return True
    



def eeg_handler(address: str, tp9, af7, af8,tp10, fpz, aux):
    # update buffers
    bool ready = update_buffer(tp9)

    # pre-process data
    if (ready == True):

        


    
    
    
    


if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/eeg", eeg_handler)

    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print("Listening on UDP port "+str(port))
    server.serve_forever()