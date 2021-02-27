class TreeNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

class Graph(object):
	def __init__(self):
		self.nodes = []
	

def in_order_traversal(node):
	if(node != None):
		in_order_traversal(node)
		print(node.value)
		in_order_traversal(node)

def pre_order_traversal(node):
	if(node != None):
		print(node.value)
		pre_order_traversal(node)
		pre_order_traversal(node)

def post_order_traversal(node):
	if (node != None):
		post_order_traversal(node)
		post_order_traversal(node)
		print(node.value)

def has_route(src, target):
	#directed graph,
	#look ahead to see if theyre in any of the adj adjs
	#if so, return true
	#else recursivly search all of them until there are no adj nodes left.
	adj = src.adjacent
	while adj:
		pass

class Node(object):
	def __init__(self, value, children = []):
		self.value = value
		self.adjacent = []
		self.visited = False
		self.marked = True
		self.f = 0
		self.g = 0
		self.h = 0
'''
check if node.value is None
if so return empty path

'''
def build_a_star_path(root,node):
	#for each adjacent use the one with the smallest f to score
	#from node to root
	min_node = None
	path = []
	n = node
	while n != root:
		if root in n.adjacent:
			path.append(root)
			return path[::-1]
		else:
			for a in n.adjacent:
				if not min_node or a.f < n.f:
					min_node = a
			path.append(min_node)
			n = min_node
			min_node = None		

def a_star_search(root, node, search_value, successors = []):
	if node.value == None:
		return []
	if node.f < min([n.f for n in successors]) and node.value == search_value:
		return build_path(root, node)
	else:
		successors.extend(self.adjacent)
		for s in successors:
			s.f = max([(s.g + s.h), node.f])
		successors = sorted(successors, key = lambda x: x.f)
		while sucessors:
			lowest = sucessors.pop()
			return a_star_search(root, lowest, search_value, successors = successors)

def dfs(node):
	if node.value == None:
		return None
	print(node)
	node.visited = True
	for adjacent in root.adjacent:
		if not adjacent.visited:
			print(dfs(adjacent))

def bfs(node):
	queue = []
	node.marked = True
	queue.append(node)

	while(queue != []):
		some_node = queue[0]
		queue = [1:]
		print(some_node)
		for adjacent in some_node.adjacent:
			if not child.marked:
				child.marked = True
				queue.append(adjacent)
