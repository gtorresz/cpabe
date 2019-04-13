from __future__ import division 
import csv 
import sys 
from collections import defaultdict 
import glob

def main():
    avk = []
    ave = []
    avd = []
    count = 0
    for i in range(0,10):
        avk.append(0)
        ave.append(0)
        avd.append(0)


    filesToProcess  = glob.glob("keygen10.csv", )
    filesToProcess += glob.glob("keygen20.csv", )
    filesToProcess += glob.glob("keygen30.csv", )
    filesToProcess += glob.glob("keygen40.csv", )
    filesToProcess += glob.glob("keygen50.csv", )
    filesToProcess += glob.glob("keygen60.csv", )
    filesToProcess += glob.glob("keygen70.csv", )
    filesToProcess += glob.glob("keygen80.csv", )
    filesToProcess += glob.glob("keygen90.csv", )
    filesToProcess += glob.glob("keygen100.csv", )
    print (filesToProcess)
    for filename in filesToProcess:
        print("Trying :" + filename)
        with open(filename, 'r') as csvh:
            dialect = csv.Sniffer().has_header(csvh.read(1024))
            csvh.seek(0)
            reader = csv.DictReader(csvh, dialect=dialect)
            for row in reader: 
                avk[count] += float(row['time(sec)'])
        count += 1
    count = 0
    filesToProcess  = glob.glob("enc10.csv", )
    filesToProcess += glob.glob("enc20.csv", )
    filesToProcess += glob.glob("enc30.csv", )
    filesToProcess += glob.glob("enc40.csv", )
    filesToProcess += glob.glob("enc50.csv", )
    filesToProcess += glob.glob("enc60.csv", )
    filesToProcess += glob.glob("enc70.csv", )
    filesToProcess += glob.glob("enc80.csv", )
    filesToProcess += glob.glob("enc90.csv", )
    filesToProcess += glob.glob("enc100.csv", )
    print (filesToProcess)
    for filename in filesToProcess:
        print("Trying :" + filename)
        with open(filename, 'r') as csvh:
            dialect = csv.Sniffer().has_header(csvh.read(1024))
            csvh.seek(0)
            reader = csv.DictReader(csvh, dialect=dialect)
            for row in reader: 
                ave[count] += float(row['time(sec)'])
        count += 1

    count = 0
    filesToProcess  = glob.glob("dec10.csv", )
    filesToProcess += glob.glob("dec20.csv", )
    filesToProcess += glob.glob("dec30.csv", )
    filesToProcess += glob.glob("dec40.csv", )
    filesToProcess += glob.glob("dec50.csv", )
    filesToProcess += glob.glob("dec60.csv", )
    filesToProcess += glob.glob("dec70.csv", )
    filesToProcess += glob.glob("dec80.csv", )
    filesToProcess += glob.glob("dec90.csv", )
    filesToProcess += glob.glob("dec100.csv", )
    print (filesToProcess)
    for filename in filesToProcess:
        print("Trying :" + filename)
        with open(filename, 'r') as csvh:
            dialect = csv.Sniffer().has_header(csvh.read(1024))
            csvh.seek(0)
            reader = csv.DictReader(csvh, dialect=dialect)
            for row in reader: 
                avd[count] += float(row['time(sec)'])
        count += 1 


    f = open("averageKeygen.csv","w")
    counter = 1;
    for each in avk:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1
   
    f = open("averageEnc.csv","w")
    counter = 1;
    for each in ave:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1
    f = open("averageDec.csv","w")
    counter = 1;
    for each in avd:
        f.write(str(counter*10) + ":\t" + str(each/1000) + "\n")
        counter += 1

    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

