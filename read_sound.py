from moviepy.editor import *
import matplotlib.pyplot as plt
import numpy as np
import os
import struct

f = open("out.pcm",'wb')

name = "VID_20200714_164018_00_050.insv"
v = VideoFileClip(name)
a = v.audio.to_soundarray()

# a = AudioFileClip("shouji2.mp3").to_soundarray();

a = a[:,1]
b = []
r = 44100/8000
t = len(a)/44100
for i in range(int(8000*t)):
	b.append(a[int(i*r)])
b = np.array(b) * 32000
print(max(b))
f.write(b.astype('int16').tostring())
f.close()

# os.system("amodem recv -i out.pcm -o data.rx")
# f = open("data.rx", "rb")
# for i in range(5):
# 	b = f.read(8)
# 	t = struct.unpack('d', b)
# 	print(t)
# f.close()
# times = np.arange(len(a))/float(44100)
# plt.fill_between(times, a[:,0])
# plt.show()