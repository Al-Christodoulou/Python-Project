import json

userinput = input("Δώστε όνομα αρχείου: ")
file = open(userinput)

# Ανάγνωση αρχείου
dict_list = []
while True:
	text = file.readline()
	if (text == ''): # Τέλος αρχείου
		break
	dictionary = json.loads(text)
	dict_list += [dictionary]

print("Τα διαθέσιμα κλειδιά είναι: x, y, name.")
keychoice = input("Επιλέξτε ένα από αυτά τα κλειδιά: ")
while keychoice not in ['x', 'y', 'name']:
	print("Δεν υπάρχει αυτή η επιλογή. Προσπαθήστε ξανά.")
	print("Τα διαθέσιμα κλειδιά είναι: x, y, name.")
	keychoice = input("Επιλέξτε ένα από αυτά τα κλειδιά: ")

# Στην αρχή θεωρούμε το πρώτο στοιχείο ως min και max, και μετά
# το συγκρίνουμε με τα υπόλοιπα
min = dict_list[0][keychoice]
max = min
for i in range(len(dict_list)):
	if (dict_list[i][keychoice] > max):
		max = dict_list[i][keychoice]
	if (dict_list[i][keychoice] < min):
		min = dict_list[i][keychoice]

print("Το min και max είναι:", min, ",", max)