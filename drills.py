test_parents_children_list = [(1,4), (2,3), (5,3), (2,5), (10, 14), (8,17), (7,2)]

test_parens_bad = "((((()))))((())(())"
test_parens_good = "(((())))(((())))"

taco_cat = "tact coa"

def test_unique(test_string):
	return set(test_string) == test_string

def test_unique_pointers(test_string):
	for i in range(test_string):
		for j in range(i+1, test_string):
			if test_string[i] == test_string[j]:
				return False
	return True

def create_count_dict(string):
	string_map = {}
	for char in string:
		if not char in string_map:
			string_map[char] = 1
		else:
			string_map[char] += 1
	return string_map

def check_key(dict_a, dict_b, key):
	count_a = dict_a.get(key, None)
	count_b = dict_b.get(key, None)
	if not (count_a and count_b):
		return False
	return count_a == count_b

def check_permuatation(string_a, string_b):
	if len(string_a) != len(string_b):
		return False
	else:
		count_a = create_count_dict(string_a)
		count_b = create_count_dict(string_b)
		for key in count_a:
			if not check_key(count_a, count_b, key):
				return False
		return True			

def urlify(string, replacement = "%20"):
	for i in range(0, len(string)):
		if string[i] == " ":
			string[i] = replacement
	return string	

def one_away(string_a, string_b):
	if abs(len(string_a) - len(string_b)) > 1:
		return False
	else:
		edits = 0
		count_a = create_count_dict(string_a)
		count_b = create_count_dict(string_b)
		for key in count_a:
			if not check_key(count_a, count_b, key):
				edits += 1
	return edits == 1	

def string_compression(string):
	new_string = ""
	count_dict = create_count_dict(string_a)
	for key in count_dict:
		new_string = "".join([key,count_dict[key])
	if len(new_string) < len(string):
		return new_string
	else:
		return string

def find_parents_and_child(test_list):
	parents = []
	children = []
	for element in test_list:
		parents.append(element[0])
		children.append(element[1])
	return(
		list(set(parents) - set(children)),
		[ele for ele in children if children.count(ele) == 1]	
	)

def test_parens(paren_list):
	balance = 0
	for paren in paren_list:
		if paren == "(":
			balance += 1
		elif paren == ")":
			balance -= 1
		else:
			return False
	return balance == 0

def constrain_max_one_odd(count_dict):
	found = False
	for key in count_dict:
		if count_dict[key] > 1:
			if found:
				return False
			else:
				return True
	return True 

def test_palindrome_permutation(test_string):
	if test_string == test_string[::-1]:
		return True
	else:
		test_string = test_string.strip()
		count_dict = {}
		for char in test_string:
			if not char in count_dict:
				count_dict[char] = 1
			else:
				count_dict[char] += 1
		return constrain_max_one_odd(count_dict)

"""
Test 2d array
[
[1, 0, 0, 0],
[0, 1 ,0, 0],
[0, 0, 1, 0],
[0, 0, 0, 1],
]
[
[0, 0, 0, 1],
[0, 0, 1, 0],
[0, 1, 0, 0],
[1, 0, 0, 0]
] Rotated
"""
def rotate_matrix(list_of_lists):
	for i in range(0, len(list_of_lists)):
		for j in range(0, len(list_of_lists[0])):
			tmp = list_of_lists[i,j]
			lists_of_lists[i,j] = list_of_list[len(list_of_lists[0]) - i)][len(list_of_lists) - j]
			lists_of_lists[len(lists_of_lists[0]) - i][len(lists_of_lists) - j] = tmp
	return list_of_lists


"""
Test MxN Matrix
[
[1, 1, 1],
[0, 1, 0],
[0, 1, 1],
[1, 1, 1],
]

[
[0, 1, 0],
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
]
"""
def zero_matrix(test_matrix):
	for i in range(0, len(test_matrix)):
		for j in range(0, len(test_matrix[i])):
			if test_matrix[i][j] == 0:
				for k in range(0, len(test_matrix[i])):
					test_matrix[i][k] = 0
				for l in range(0, len(test_matrix)):
					test_matrix[l][j] = 0
	return test_matrix

def is_sub_string(string_a, string_b):
	return (string_a in string_b)

def string_rotation(string_a, string_b):
	if (string_a and string_b) and (len(string_a) == len(string_b)):
		string_a_test = string_a + string_a
		return is_sub_string(string_b, string_a_test)	
	return False
