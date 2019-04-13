# cpabe
Must install cpabe libray from  http://hms.isi.jhu.edu/acsc/cpabe/#papers

Follow these steps http://hms.isi.jhu.edu/acsc/cpabe/cpabe-setup.html for setup in order to generate public key and master key files.

Then copy my keygen.c, enc.c, and dec.c files into your cpabe folder and run the makefile.

Sample comand to run keygen, enc, and dec, must be run from cpabe folder.

Keygen: ./cpabe-keygen -o priv10key pub_key master_key a1 a2 a3 a4 a5 a6 a7 a8 a9 a10

Enc: ./cpabe-enc -k pub_key test.txt 'a1 and a2 and a3 and a4 and a5 and a6 and a7 and a8 and a9 and a10'

Dec: ./cpabe-dec -k pub_key priv10key test.txt10.cpabe

Keygen will automatically create unique csv files based on attribute size, enc & dec require user to go into code and change the variable size to reflect number of attriubtes and generate unique file name, makefile must be run after each change.  
