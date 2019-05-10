from __future__ import division 
import csv 
import sys 
import socket
from collections import defaultdict 
import glob
from pyndn.name import Name
from pyndn.face import Face
from pyndn.util.blob import Blob
from manifest import Manifest
from data import Data
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from pyndn.sha256_with_rsa_signature import Sha256WithRsaSignature
import ast
import json

def main(filepath=None, maxSuccess=None):

       with open('attacker2.csv', 'rb') as f:
          dataArray = []
          readdata = f.read(8*1024)
          dataArray.append(readdata)
          manifestData = {}
          count = 0
          seq = 0
          while readdata:
             digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
             digest.update(readdata)
             manifestData[(seq+count)]=(str(digest.finalize()))

             #c = sys.getsizeof(manifestData)
             count = count + 1
             if count == 100:

                #print(manifestData)
                s=json.dumps(manifestData).encode('utf-8')
                manifest_packet = Manifest(Name("prefix/data/"+str(seq)))
                manifest_packet.setContent(s)
                k = json.loads(Blob(manifest_packet.getContent()).toBytes().decode('utf-8'))
                print(sys.getsizeof(Blob(s)))
                #print(seq)
                if seq == 15150:
                 print(manifestData[15150])
                 print(k["15150"])
                #print(Blob(s).toBytes().decode('utf-8'))
                #print(json.loads(s.decode('utf-8')))
                #print(manifest_packet.getName())
                while count > 0:
                   seq = seq + 1
                   datapacket = Data(Name("prefix/data/"+str(seq)))
                   datapacket.setContent(dataArray[10-count])
                   print(datapacket.getContent())
                   count = count - 1
                seq = seq + 1
                manifestData = {}
                dataArray = []
             readdata = f.read(8*1024)
             dataArray.append(readdata)

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
