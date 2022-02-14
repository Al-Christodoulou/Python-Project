from urllib.request import Request, urlopen
import json
import math
from time import sleep

request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'}

print("Αρπάζω πληροφορίες από τον τελευταίο γύρο ...")
req = Request('https://drand.cloudflare.com/public/latest', headers=request_headers)
data = urlopen(req).read()

dictionary = json.loads(data)
curround = dictionary["round"]
hex_text = dictionary["randomness"]

for i in range(1,20):
	print("Αρπάζω πληροφορίες από τον γύρο", curround - i, "...")
	req = Request('https://drand.cloudflare.com/public/' + str(curround - i), headers=request_headers)
	data = urlopen(req).read()
	dictionary = json.loads(data)
	hex_text += dictionary["randomness"]

hex_text_unique = list(set(hex_text))
hex_text_length = len(hex_text)

hex_symbol_frequency = []
for symbol in hex_text_unique:
	hex_symbol_frequency += [hex_text.count(symbol)]

sum = 0
for i in range(len(hex_text_unique)):
	chance = hex_symbol_frequency[i] / hex_text_length
	sum += chance * math.log2(chance)
sum = sum * -1

print("Τελική εντροπία:", sum)