class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def build_linked_list(self, values):
		for value in values:
			self.append(value)

	def append(self, value):
		if not self.head:
			self.head = Node(value)
		else:
			tmp = self.head
			while tmp.next != None:
				tmp = temp.next
			tmp.next = Node(value)

	def remove(self, value):
		if not self.head:
			return
		tmp = self.head
		if tmp.value == value:
			self.head = self.head.next
		else:
			while tmp.next != None:
				if tmp.next.value == value:		
					tmp.next = tmp.next.next
				else:
					tmp = temp.next	
		return

	def remove_duplicates(self):
		if not self.head:
			return
		else:
			tmp = self.head
			while tmp != None:
				next_tmp = tmp.next
				while next_temp.next != None:
					if next_temp.next.value == tmp.value:
						next_temp.next = next_temp.next.next
					next_temp = next_temp.next	
				tmp = tmp.next	


	def remove_middle(self, node):
		if not self.head:
			return
		else:
			tmp = self.head
			while tmp.next != None:
				if tmp.next.value == node.value:
					tmp.next = tmp.next.next
					return
				else:
					tmp = temp.next
		return		

	def size(self):
		count = 0
		tmp = self.head
		while tmp.next != None:
			count += 1
			tmp = tmp.next
		return size

	def reverse(self):
		new_head = None
		tmp = self.head
		while tmp != None:
			node = Node(tmp.data)
			node.next = new_head
			new_head = node
			tmp = tmp.next
		self.head = new_head

	def clone_and_reverse(self):
		new_list = LinkedList()
		tmp = self.head
		while tmp != None:
			node = Node(tmp.data)
			node.next = new_list.head 
			new_list.head = node
			tmp = tmp.next
		return new_list

	def is_equal(self, other_list):
		tmp_a = self.head
		tmp_b = other_list.head
		while (tmp_a != None and tmp_b != None):
			if tmp_a != tmp_b:
				return False
			tmp_a = tmp_a.next
			tmp_b = tmp_b.next
		return tmp_a == None and tmp_b == None
				
	def get_counts(self):
		counts = {}
		tmp = self.head
		while tmp != None:
			if not tmp.value in counts:
				counts[tmp.value] = 1
			else:
				counts[tmp.value] += 1
		return counts
			
	def kth_to_last(self, position):
		i = 0
		tmp = self.head
		while i!= (self.size() - position):
			tmp = tmp.next
			i += 1
		return tmp
	
	#So we have to make new list from the nodes
	def partition(self, partition):
		pass

	def is_palindrome(self):
		return self.is_equal(self.clone_and_reverse())
	
	def is_palindrome_permutation(self):
		counts = self.get_counts()
		count_flag = False
		for count in list(counts.values()):
			if count % 2 != 0:
				if count_flag:
					return False
				else:
					count_flag = True
		return True

	def intersection(self, other_linked_list):
		tmp_a = self.head
		tmp_b = other_linked_list.head
		while tmp_a is not None:
			if tmp_a.value == tmp.value:
				return True
			else;
				tmp_a = tmp_a.next
				tmp_b = tmp_b.next
		return False

	def loop_detection_address(self):
		tmp = self.head
		while tmp.next != None:
			runner = tmp.next
			while runner != None:
				if id(runner) == id(tmp):
					return True
			tmp = tmp.next

	def sum_list(self, other_list, forward = False, carry):
		tmp_a = self.head
		tmp_b = other_list.head


		pass

	#would need to check address for this, but assume values are unique
	def loop_detection_unique_values(self, node = self.head, possible_loop = False):
		if node is None:
			return False
		else:
			tmp = node.next
			while tmp != None:
				if tmp.value == node.value:
					if possible_loop == True:
						return True
					else:
						return self.loop_detection(node = tmp.next, possible_loop = True)
				tmp = tmp.next
			return self.loop_detection(node = node.next, possible_loop = False)
