from urllib.request import Request, urlopen
import json
from time import sleep

request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'}

print("Αρπάζω πληροφορίες από τον τελευταίο γύρο ...")
req = Request('https://drand.cloudflare.com/public/latest', headers=request_headers)
data = urlopen(req).read()

dictionary = json.loads(data)
curround = dictionary["round"]
hex_text = dictionary["randomness"]

for i in range(1,100):
	print("Αρπάζω πληροφορίες από τον γύρο", curround - i, "...")
	req = Request('https://drand.cloudflare.com/public/' + str(curround - i), headers=request_headers)
	data = urlopen(req).read()
	dictionary = json.loads(data)
	hex_text += dictionary["randomness"]

hex_text = int(hex_text, 16)
bin_text = bin(hex_text)
# Αγνοούμε τους δυο πρώτους '0b' χαρακτήρες
bin_text = bin_text[2:]

max0 = -1
max1 = -1
cur0s = 0
cur1s = 0
for letter in bin_text:
	if letter == '0':
		if cur1s > max1:
			max1 = cur1s
		cur0s += 1
		cur1s = 0
		if cur0s > max0:
			max0 = cur0s
	elif letter == '1':
		if cur0s > max0:
			max0 = cur0s
		cur1s += 1
		cur0s = 0
		if cur1s > max1:
			max1 = cur1s

print("Η μεγαλύτερη ακολουθία με συνεχόμενα μηδενικά έχει μήκος", max0)
print("Η μεγαλύτερη ακολουθία με συνεχόμενες μονάδες έχει μήκος", max1)