import bitsv
import sys
import time
from multiprocessing import Event, Process, Queue, Value, cpu_count

from coincurve import Context

from bitsv.base58 import BASE58_ALPHABET, b58encode_check
from bitsv.crypto import ECPrivateKey, ripemd160_sha256
from bitsv.format import bytes_to_wif, public_key_to_address
from bitsv import Key, PrivateKey
from bitsv import wif_to_key



def generate_key_address_pair():  #pragma: no cover
    
   
    key=Key()
    priv=key.to_wif()
    print (priv)
    print(key)
    
    
    return priv




    
              
def main():
    generate_key_address_pair()
    
   
main()
