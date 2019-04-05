import sys
import itertools

def parse_cnf(path, mode):
	file = open(path, 'r')
	line = file.readline()
	cnf_list = set()
	alpha_list = []
	while line:
		chars_list = line.split(' ')
		temp = []
		for i in chars_list:
			if i[0] == '-':
				if mode:
					temp.append(-1*(ord(i[1])-64))
				else:
					temp.append(ord(i[1]) - 64)
			else:
				if mode:
					temp.append(ord(i[0]) - 64)
				else:
					temp.append(-1*(ord(i[0])-64))
		line = file.readline()
		if mode:
			cnf_list.add(frozenset(temp))
		else:
			alpha_list.append(temp)

	file.close()
	if mode:
		return cnf_list
	else:
		return alpha_list

def PL_resolve(ci, cj):
	if len(ci) is 1 and len(cj) is 1:
		for i in ci:
			if -i in cj:
				return frozenset()
	resolved = None
	for i in ci:
		if -i in cj:
			ci = ci.difference(frozenset([i]))
			cj = cj.difference(frozenset([-i]))
			resolved = ci.union(cj)
	return resolved

def PL_resolution(KB, alpha):
	clauses = KB.union(alpha)
	new = set()
	resolved_count = 0
	while True:
		for i in clauses:
			for j in clauses:
				resolvant = PL_resolve(i, j)
				if resolvant is not None and len(resolvant) == 0:
					return True, resolved_count
				if resolvant is not None:
					resolved_count += 2
					new.add(resolvant)
		print(new)
		if new.issubset(clauses):
			return False, resolved_count
		clauses = clauses.union(new)

def dnf_to_cnf(alpha_list):
	final_alpha = set()
	for i in alpha_list:
		final_alpha.add(frozenset(i))
	return final_alpha
		
def recursive_add(elem, alpha_list):
	if len(alpha_list) == 0:
		return elem
	if len(elem) is 0:
		for i in alpha_list[0]:
			elem.append([i])
		return recursive_add(elem, alpha_list[1:len(alpha_list)])
	else:
		temp = []
		for i in elem:
			for j in alpha_list[0]:
				if -j not in i:
					temp.append(i + [j])

		return recursive_add(temp, alpha_list[1:len(alpha_list)])
main():
	KB = parse_cnf(sys.argv[1], True)
	Alpha = dnf_to_cnf(recursive_add([], parse_cnf(sys.argv[2], False)))
	solution = PL_resolve(KB, Alpha)
	print(solution[0]+ ' ' + solution[1])