import bitsv
import qrcode
import time


import sys
from multiprocessing import Event, Process, Queue, Value, cpu_count

from coincurve import Context

from bitsv.base58 import BASE58_ALPHABET, b58encode_check
from bitsv.crypto import ECPrivateKey, ripemd160_sha256
from bitsv.format import bytes_to_wif, public_key_to_address
from bitsv import Key, PrivateKey
from bitsv import wif_to_key




lst=[]

def get_number_of_op_return():
    i=input("how many op_returns do you need?")
    return i



def op_return_construct(i,c,lst):
    if i<=int(c):
        d="s"+str(i)
        lst.append(d)
        i=i+1
        op_return_construct(i,c,lst)

def make_tx(c):
    i= len(lst)
    
    if c<i:
        a=lst[c]+"="
        e=input(a)
        d=e.encode('utf-8')
        print(d)
        lst[c]=d
        c=c+1
        
        make_tx(c)
def empty_list(lst):
    lst[:]=[]
def send_tx(a):
    my_key=bitsv.Key(a) #priv key needed
    list_of_pushdata=lst
    bob=my_key.send_op_return(list_of_pushdata)
    print(bob)
    

    main()

def check_balance(a):
    my_key=bitsv.Key(a)  #priv key needed
    key=Key(a)
    addy=key.address
    print(addy)




def main():
    empty_list(lst)
    op_return_construct(1,get_number_of_op_return(),lst)
    print(lst)

    make_tx(0)
    print(lst)
    send_tx('key')
    





main()


