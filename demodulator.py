class Demod:
	def __init__(self, sample):
		self.s = sample
		self.state = 0
		self.index = 0

	def detect(self):
		count = 0
		state = 0
		current = 0
		head = []
		while True:
			if self.index == len(self.s):
				return False
			if state == 0:
				if self.s[self.index] != 0:
					count += 1
					current = self.s[self.index]
					state = 1
			elif state == 1:
				if self.s[self.index] == current:
					count += 1
				else:
					# print(self.index)
					if count >= 66:
						if count <= 110:
							head.append(current)
							if len(head) == 3:
								break
						else:
							if len(head) == 2:
								head.append(current)
								break
							print("Too long prefix!:", self.index, count)
							count = 0
							state = 0
							current = 0
							head = []
							continue
					else:
						print("Too short prefix!:", self.index, count)
						count = 0
						state = 0
						current = 0
						head = []
						continue
					count = 0
					if self.s[self.index] == 0:
						state = 0
						current = 0
					else:
						current = self.s[self.index]
			self.index += 1

		if head == [1,-1,1]:
			return True
		else:
			print("Wrong prefix!:", head)
			return False

	def read(self):
		count = 0
		state = 0
		current = 0
		payload = []
		while True:
			if self.index == len(self.s):
				return []
			if state == 0:
				if self.s[self.index] != 0:
					count += 1
					current = self.s[self.index]
					state = 1
			elif state == 1:
				if self.s[self.index] == current:
					count += 1
				else:
					# print(self.index)
					if count >= 165:
						if count <= 275:
							payload.append(current)
							if len(payload) >= 24:
								break
						elif count >= 330 and count <= 550:
							payload.append(current)
							payload.append(current)
							if len(payload) >= 24:
								break
						elif count > 550 and len(payload) == 23:
							payload.append(current)
							break
						else:
							print("Ood length of symbol:", len(payload), self.index, count)
					else:
						print("Too short symbol!:", self.index, count)
					count = 0
					if self.s[self.index] == 0:
						state = 0
						current = 0
					else:
						current = self.s[self.index]
			self.index += 1
		payload = payload[:24]
		out = "0b"
		for i in range(8):
			symbol = payload[3*i:3*i+3]
			if symbol == [-1,1,-1]:
				out += "0"
			elif symbol == [1,-1,1]:
				out += "1"
			else:
				print("Wrong symbol:", symbol)
		# print(out)
		return int(out,2)

	def demodulate(self):
		index = []
		payloads = []
		while True:
			if self.detect():
				payload = self.read()
				print(payload)
				payloads.append(payload)
				index.append(self.index)
				print("---------------------------------") 
			if self.index == len(self.s):
				break
		return index, payloads