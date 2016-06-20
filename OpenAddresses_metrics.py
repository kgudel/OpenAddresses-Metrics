
import os
import argparse

#command line parsing
parser = argparse.ArgumentParser(description='Produce metrics on OpenAddresses data.')
parser.add_argument('input', help= 'The OpenAddresses Folder')
parser.add_argument('output', help= 'The file that data will be written into.')
parser.add_argument('-s', '--summary', type =str, help = 'define a file to output state by state summary')
args = parser.parse_args()


def check_validity(l_split):
	#checks if a row is good i.e. that it contains a valid lat, lon, number, and street. Also 
    #checks if there are quotation marks as a proxy for parsing issues and whether the number has
    #any digits as a proxy for parsing an bad data issues
	if len(l_split) >= 8 and l_split[0] and l_split[1] and l_split[2] and l_split[3] and 'plot' not in l_split[2] and 'plot' not in l_split[3] \
	and '"' not in l_split[2] and '"' not in l_split[3] and l_split[0].lower() != 'lon' and any(i.isdigit() for i in l_split[2]):
		if l_split[2].isdigit() == True: #if num is a digit check that it is greater than 0
			if int(l_split[2]) > 0: return True
			else: return False
		else: return True
	else: return False

def mylistdir(directory):
    #A specialized version of os.listdir() that ignores files that start with a leading period."""
    filelist = os.listdir(directory)
    return [x for x in filelist if not (x.startswith('.'))]

def is_number(string):
    #Returns whether a string can be converted into a number, intended only for address strings
	if string == '': return False
	else: return all(val.isdigit() or val == '-' and inx == 0 for inx, val in enumerate(string))

def has_city(list):
	if list[4] and '"' not in line[4]: return True
	else: return False

def has_zip(list):
	if len(list[7]) >= 5 and '"' not in list[7]: return True
	else: return False

def has_both(list):
	if has_zip(list) and has_city(list): return True
	else: return False

def has_quotes(list):
	if '"' in list: return True
	else: return False

def missing_rows(list):
	if len(list) < 9: return True
	else: return False

def no_digit_in_number(list):
	if len(list) >= 4 and list[2] and list[2] != 'NUMBER' and any(i.isdigit() for i in list[2]) != True: return True
	else: return False

def has_negative_number(list):
	if len(list) >= 4 and line[2] and is_number(line[2]) and int(line[2]) < 0: return True
	else: return False

def incomplete_zip(list):
	if len(list) >= 8 and list[7] and len(list[7]) < 5: return True
	else: return False

if args.summary: f_summary = open(args.summary, 'a')
output = open(args.output, 'a') 
for state in mylistdir(args.input): #loop through states folders
	print(state) #just to record progress in the terminal
	if args.input.endswith('//'): state_dir = args.input + state #make the state file path
	else: state_dir = args.input + '//' + state #make the state file path
	if args.summary: st_statewide = st_st_city = st_st_zip = st_st_both = st_other = st_o_city = st_o_zip = st_o_both = 0
	output.write(state +  '\n')
    	for region in mylistdir(state_dir): #loop through the files in state folders
		if region.endswith('.csv'):
			region_dir = state_dir + '//' + region #make the region file path
			with open(region_dir, 'r') as file:
				all_lines = [line.split(',') for line in file]
			lines = len(all_lines) - 1#count total lines
			good_lines = filter(check_validity, all_lines)
			good = len(good_lines) #counting good lines
			city = len(filter(has_city, good_lines))
			zip = len(filter(has_zip, good_lines))
			both = len(filter(has_both, good_lines))
			parsing = len(filter(has_quotes, all_lines))
			full = len(filter(missing_rows, all_lines))
			po = len(filter(no_digit_in_number, all_lines))
			nine = len(filter(has_negative_number, all_lines))
			bad_zip = len(filter(incomplete_zip, all_lines))
			output.write(','.join([region, str(lines), str(good), str(city), str(zip), str(both), str(parsing), str(po), str(nine), str(full), str(bad_zip)]) + '\n')
			if args.summary:
				#recording data about statewide files
				if region.lower() == 'statewide.csv' or region.lower() == '_loveland.csv':
					st_statewide += good
					st_st_city += city
					st_st_zip += zip
					st_st_both += both
				#recording data about non-statewide files
				else:
					st_other += good
					st_o_city += city
					st_o_zip += zip
					st_o_both += both
	if args.summary:
		#create list to join and write into summary file, fill it with data from other files
		summary = [state, str(st_statewide), str(st_other),str(st_o_city),'other',str(st_o_zip),'other',str(st_o_both),'other']
		#replace with statewide if larger than other for city
		if st_st_city > st_o_city: summary[3] = str(st_st_city); summary[4] = 'statewide'
		#replace with statewide if larger than other for zip
		if st_st_zip > st_o_zip: summary[5] = str(st_st_zip); summary[6] = 'statewide'
		#replace with statewide if larger than other for both
		if st_st_both > st_o_both: summary[7] = str(st_st_both); summary[8] = 'statewide'
		f_summary.write(','.join(summary) + '\n')

output.close
if args.summary: f_summary.close
