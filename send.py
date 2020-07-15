import numpy as np
import time
import os
import struct 

def send():
	f = open("data.tx","wb")
	# t3 = t - int(t)
	# t1 = int(t) >> 16
	# t2 = int(t) & 0xffff

	# t = np.array([t1,t2,t3]).astype('float16').tostring()
	t = time.time() + 0.25 + 0.54
	t1 = time.time()
	b = struct.pack('d', t)
	for i in range(5):
		f.write(b)
	f.close()

	os.system("amodem send -i data.tx -o a.pcm")
	print(time.time()-t1)
	os.system("ffplay -f s16le -ac 1 -ar 8000 -autoexit -i a.pcm")
	print("==========================================================")
	print("==========================================================")
	print("send at time", t)
	for i in b:
		print(hex(i))
	print("==========================================================")
	print("==========================================================")


send()