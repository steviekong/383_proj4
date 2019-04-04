import sys

def convert 

class cnf_or_vals:
	def __init__(self, negated_variables, non_neg_varaibles):
		self.negated_variables = negated_variables
		self.non_neg_variables = non_neg_varaibles
#def process_line(chars_list):


def parse_cnf(path):
	file = open(path, 'r')
	line = file.readline()
	cnf_list = []
	while line:
		chars_list = line.split(' ')
		temp = cnf_or_vals([],[])
		for i in chars_list:
			if i[0] == '-':
				temp.negated_variables.append(-1*(ord(i[1])-96))
			else:
				temp.non_neg_variables.append(ord(i[0]) - 96)
		line = file.readline()
		cnf_list.append(temp)
	file.close()
	return cnf_list

def negate_alpha(alpha_list):


