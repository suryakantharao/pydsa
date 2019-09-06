class node():
	def __init__(self,value, ref):
		self.value = value
		self.ref = ref
class SingleLinkedList():
	def __init__(self, *list):
		if not len(list):
			self.head=None
		else:
			self.head = node(list[0], None)
		prv_nd = self.head
		for value in list[1:]:
			nd = node(value,None)
			prv_nd.ref = nd
			prv_nd = nd

	def __setitem__(self, idx,  value):
		nd = self.head
		if idx >= len(self): raise IndexError("index {} out of range".format(idx))
		for _ in range(idx):
			nd = nd.ref
		nd.value = value
	def append(self, value):
		nd = self.head
		while(nd.ref is not None):
			nd = nd.ref
		newnd = node(value, None)
		nd.ref = newnd
	def __del__(self):
		pass
	def push(self):
		pass
	def pop(self):
		pass
	def get_slice(self, start, stop, step):
		rel_step = step
		print start, stop, step
		if step is None : step =1
		if step < 0:
			if start <= stop:
				return SingleLinkedList()
			else:
				step = -1 * step
				(start, stop) = (stop,start)
		if step > 0 and start >= stop:
			return SingleLinkedList()
		nd = self.head
		for _ in range(start):
			nd = nd.ref
		new_list = SingleLinkedList(nd.value)
		cur_pos = start

		while nd.ref is not None and cur_pos < stop:
			print "cur_pos= {}".format(cur_pos)
			for _ in range(step):
				nd = nd.ref
			cur_pos += step
			new_list.append(nd.value)
		return new_list
	def __getitem__(self, item):
		if isinstance(item, slice):
			return self.get_slice(item.start, item.stop, item.step)
		nd = self.head
		if item >= len(self): raise IndexError("index {} out of range".format(item))
		for _ in range(item):
			nd = nd.ref
		return nd.value
	def __len__(self):
		nd = self.head
		if nd is None:
			return 0
		i = 1
		while(nd.ref is not None):
			i +=1
			nd = nd.ref
		return  i
	def __str__(self, ):
		nd  = self.head
		if nd is None: return ''
		value = '['
		value += "{}, ".format(nd.value)
		while(nd.ref is not None):
			nd = nd.ref
			value += "{}, ".format(nd.value)
		value = value.strip(', ')
		value += "]"
		return value

