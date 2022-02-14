userinput = input("Δώστε όνομα αρχείου: ")
file = open(userinput)
text = file.read()
text = text.lower()

# Γέμισμα της λίστας με τους χαρακτήρες ASCII από το 33 εώς το 65,
# από 91-97 και από 123 εώς 127
blacklist = []
for i in range(33, 65):
	blacklist += chr(i)
for i in range(91, 97): # [,\,],^,_,`
	blacklist += chr(i)
for i in range(123, 127): # {,|,},~
	blacklist += chr(i)

# Αντικατάσταση αυτών των χαρακτήρων με το κενό
for i in range(0, len(blacklist)):
	text = text.replace(blacklist[i], "")

# Χωρίζουμε το text σε λίστα από λέξεις
text = text.split()

# Λίστα με την κάθε ξεχωριστή λέξη χωρίς επαναλήψεις
unique_words = list(set(text))
unique_words_count = len(unique_words)

# ===================================
# Εύρεση δέκα δημοφιλέστερων λέξεων
# ===================================

def calcMostUsedWordsWithFrequency(unique_words, num_of_most_used):
	word_and_frequency_list = []
	# Αυτό το unique_words_count είναι διαφορετικό από το εξωτερικό
	unique_words_count = len(unique_words)

	for word in unique_words:
		word_count = text.count(word)
		word_and_frequency_list += [ [word, word_count] ]

	# Βρές την λέξη με την μεγαλύτερη συχνότητα, και τοποθέτησέ την σε
	# μια καινούργια λίστα, max frequency word list
	max_word = ""
	max_frequency_word_list = []

	# Έλεγχος με το num_of_most_used καθώς θέλουμε τις num_of_most_used πιο
	# δημοφιλέστερες λέξεις, εκτός αν είναι λιγότερες από αυτό
	wanted_word_count = num_of_most_used
	if unique_words_count < num_of_most_used:
		wanted_word_count = unique_words_count
	for i in range(wanted_word_count):
		max_frequency = -1
		max_index = -1
		for j in range(len(word_and_frequency_list)):
			# Έλεγχος αν η συγκεκριμένη λέξη εμφανίζεται πιο συχνά
			# από το max που έχουμε αυτήν την στιγμή
			if (word_and_frequency_list[j][1] > max_frequency):
				max_frequency = word_and_frequency_list[j][1]
				max_word = word_and_frequency_list[j][0]
				max_index = j

		max_frequency_word_list += [ [max_word, max_frequency] ]
		# Διαγραφή της λέξης από την λίστα ώστε να βρούμε το επόμενο max
		del word_and_frequency_list[max_index]
	return max_frequency_word_list


# Εμφάνιση των 10 πιο δημοφιλέστερων λέξεων:
tenMostPopularWords = calcMostUsedWordsWithFrequency(unique_words, 10)

print("Οι 10 πιο δημοφιλέστερες λέξεις είναι:")
for i in range(len(tenMostPopularWords)):
	print("'", tenMostPopularWords[i][0], "', εμφανίζεται", tenMostPopularWords[i][1], "φορές")


# ====================================================================================
# Οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις
# + για τρία γράμματα
# ====================================================================================
unique_words_2letters = []
unique_words_3letters = []
for i in range(unique_words_count):
	if (len(unique_words[i][:2]) == 2): # Θέλουμε λέξεις που είναι ακριβώς 2 γράμματα
		unique_words_2letters += [unique_words[i][:2]]
	if (len(unique_words[i][:3]) == 3): # Το ίδιο για τα τρία γράμματα
		unique_words_3letters += [unique_words[i][:3]]
# Ξανά μετατροπή σε σύνολο (set) και μετά πάλι σε λίστα ώστε να μην υπάρχουν επαναλήψεις
# (Υπάρχει η πιθανότητα 2 διαφορετικές λέξεις να έχουν τα ίδια πρώτα 2 ή 3 γράμματα)
unique_words_2letters = list(set(unique_words_2letters))
unique_words_3letters = list(set(unique_words_3letters))

threeMostUsedFirstLetters = calcMostUsedWordsWithFrequency(unique_words_2letters, 3)
twoMostUsedFirstLetters = calcMostUsedWordsWithFrequency(unique_words_3letters, 3)

print("Οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι:")
for i in range(len(threeMostUsedFirstLetters)):
	print("'", threeMostUsedFirstLetters[i][0], "', εμφανίζεται", threeMostUsedFirstLetters[i][1], "φορές")

print("Για τρία γράμματα:")
for i in range(len(twoMostUsedFirstLetters)):
	print("'", twoMostUsedFirstLetters[i][0], "', εμφανίζεται", twoMostUsedFirstLetters[i][1], "φορές")