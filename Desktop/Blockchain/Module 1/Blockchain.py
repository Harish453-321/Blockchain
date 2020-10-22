# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:54:09 2020

@author: ASUS
"""
#Importing libraries
import datetime
import hashlib
import json
from flash import Flask, jsonify

#Creating a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain=[];
        self.create_blockchain=(proof = 1,previous_hash ='0');
    
    def create_blockchain(self,proof,previous_hash):
        block = ('index': len(self.chain)+1,
                 'timestamp':str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash':previous_hash,
                 'data':My content)
     
