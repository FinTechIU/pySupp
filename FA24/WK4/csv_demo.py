import csv, time

def basic_reader():
	old_school = True
	if old_school:
		l = list(reader)
		for i in range(len(l)):
			row = l[i]
			print(row)
	else:
		for row in reader: # explain this type of for loop
			print(row)

def print_banks_from_state():
	wanted_state = input('Enter a state abbreviation: ')
	for row in reader:
		if row['State'] == wanted_state:
			print(row['Bank Name'], row['Closing Date'])


'''
	time library is used here; you never just use 1 library, you use several in combination
	strptime takes a string according to the format you pass and returns a datetime object
	for format details, see: https://man7.org/linux/man-pages/man1/date.1.html
'''
def print_banks_ascending_date():
	list_banks = list(reader)
	list_banks.sort(key=lambda x: time.strptime(x['Closing Date'], '%d-%b-%y'))
	for b in list_banks:
		print(b['Bank Name'], b['Closing Date'])

# try removing the encoding= argument and show what happens
with open('banklist.csv', newline='', encoding='ISO-8859-1') as csvfile:
	global reader
	# can read a file with a non-comma delimiter with csv.reader(delimiter='|')
	reader = csv.DictReader(csvfile)
	#basic_reader()
	#print_banks_from_state()
	#print_banks_ascending_date()