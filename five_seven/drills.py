import sys
import re


def hard_count(some_string):
	count = 0
	for char in some_string:
		count += 1
	return count

def one_two(some_string):
	am = re.compile(r"[a-m,A-M]")
	nz = re.compile(r"[n-z,A-Z]")

	print("Pratice, pratice, pratice.\n")

	if am.match(some_string):
		print("Hello %s -> %s" % (some_string, hard_count(some_string)))
	elif nz.match(some_string):
		print("Something strange is happening.. %s -> %s" % (some_string, hard_count(some_string)))
	else:
		print("Robits be strong here %s -> %s" % (some_string, hard_count(some_string)))

	print("The first 10,000 hours are the easiest.")
	
if __name__ == "__main__":
	one(sys.argv[1])
