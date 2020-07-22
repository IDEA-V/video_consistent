import numpy as np
import time
import os
import struct 

def send(f):
	# t = time.time() + 0.25 + 0.54
	# t1 = time.time()
	# b = struct.pack('d', t)
	# for i in range(5):
	# 	f.write(b)
	# f.close()
	os.system("amodem send -i data.tx -o a.pcm")
	ff = open("data.tx",'rb')
	f.write(ff.read(8))
	f.write(b'\n')
	os.system("ffplay -f s16le -ac 1 -ar 8000 -autoexit -i a.pcm")
	ff.close()
	# print("==========================================================")
	# print("==========================================================")
	# print("send at time", t)
	# for i in b:
	# 	print(hex(i))
	# print("==========================================================")
	# print("==========================================================")

f = open("time_send","wb")
for i in range(10):
	send(f)
	time.sleep(2)
f.close()