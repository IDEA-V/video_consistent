from moviepy.editor import *
import matplotlib.pyplot as plt
import numpy as np
import os
import struct
from demodulator import Demod

fps = 24
name = "VID_20201127_171921_10_005.insv"
v = VideoFileClip(name)
a = v.audio.to_soundarray()

# a = AudioFileClip("0728test1.mp3").to_soundarray();
base = 0

a = a[:,1]
x = [i for i in range(len(a))]
y = []
for i in range(len(a)):
	# if a[i] - a[i-1] > 0.5:
	# 	base = 1
	# if a[i] - a[i-1] < -0.5:
	# 	base = -1
	# y.append(base)
	lo = i - 10
	hi = i + 11
	if lo < 0:
		lo = 0
	if hi > len(a):
		hi = len(a)

	avg = sum(a[lo:hi])/(hi- lo)

	if avg > 0.25:
		y.append(1)
	elif avg < -0.25:
		y.append(-1)
	else:
		y.append(0)
	# y.append(avg)

demod = Demod(y)
plt.plot(x, y)
plt.show()

index, time_stamps = demod.demodulate()

# time = [i/44100 for i in index]
# # imgs = [v.get_frame(i) for i in time]

# i = 0
# index = 0
# imgs = []
# times = []
# for frame in v.iter_frames(fps = fps):
# 	t = index/fps
# 	imgs.append(frame)
# 	if i < len(time)-1 and abs(t - time[i]) < abs(time[i+1] - t):
# 		print(time_stamps[i] + (t - time[i]))
# 		times.append(time_stamps[i] + (t - time[i]))
# 	else:
# 		i += 1
# 		print(time_stamps[i] + (t - time[i]))
# 		times.append(time_stamps[i] + (t - time[i]))

# 	index += 1

print("end")
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