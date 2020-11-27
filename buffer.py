class Buffer:
	def __init__(self):
		self.l = []
		self.start = 0
		self.len= 0

	def push(self, x):
		if self.len < 20:
			self.l.append(x)
			self.len += 1
		else:
			self.l = self.l[1:]
			self.l.append(x)

	def diff(self):
		hi = self.l.index(max(self.l))
		loi = self.l.index(min(self.l))
		if hi > loi:
			return max(self.l) - min(self.l)
		else:
			return min(self.l) - max(self.l)  