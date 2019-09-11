import collections.abc
class Node():

	def __init__(self,value):
		self.data = value
		self.link = None


class SingleLinkedList(collections.abc.MutableSequence):
	"""
	This Module Implements List using single linked list
	===================================================
	list creation -  						sllist(1, 2, 3)
	print the list (string overloading)	-	print(slist)
	"""
	start = None
	_len = 0
	def __init__(self, *list):
		prev_node = None
		for idx, value in enumerate(list):
			node = self._create_node(value)
			if prev_node is not None:
				prev_node.link = node
			else:
				self.start = node
			prev_node =  node

	def _create_node(self, value):
		nd = Node(value)
		self._len +=1
		return nd

	def __setitem__(self, idx,  value):
		nd = self.head
		if idx >= len(self): raise IndexError("index {} out of range".format(idx))
		for _ in range(idx):
			nd = nd.ref
		nd.value = value
	def append(self, value):
		nodes = self._nodes_traversal()
		for node in nodes:
			nd = node
		newnd = Node(value)
		nd.link = newnd
	def __del__(self):
		pass
	def push(self):
		pass
	def pop(self):
		pass
	def get_slice(self, start, stop, step):
		rel_step = step
		print( start, stop, step)
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
			print("cur_pos= {}".format(cur_pos))
			for _ in range(step):
				nd = nd.ref
			cur_pos += step
			new_list.append(nd.value)
		return new_list
	def __getitem__(self, item):
		"""
		Repleacates index accessing of list
		:param item: list index
		:return: return the item in the list
		"""
		if isinstance(item, slice):
			return self.get_slice(item.start, item.stop, item.step)
		nodes = self._nodes_traversal()
		for _ in range(item+1):
			try:
				nd = next(nodes)
			except StopIteration:
				raise IndexError("Index out of range")
		return nd.data
	def __len__(self):
		"""
		Replecates list len mentod
		Usage len(sll)
		:return: length of single linked list
		"""
		return self._len

	def __str__(self, ):
		"""
		replecates str of list
		:return: string value of list
		"""
		value = '['
		nodes = self._nodes_traversal()
		for nd  in nodes:
			value += "{}, ".format(nd.data)
		value = value.strip(', ')
		value += "]"
		return value

	def _nodes_traversal(self):

		nd = self.start
		while (nd):
			yield nd
			nd = nd.link
	def __delitem__(self, key):
		pass
	def insert(self):
		pass
if __name__ == '__main__':
	sll = SingleLinkedList('a','b','c')
	print(list(sll))

	# TypeError: Can't instantiate abstract class  with abstract methods __delitem__, insert
