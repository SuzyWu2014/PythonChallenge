try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import collections
import string
import re, webbrowser as wb

# My solution
response = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
page_source = response.read()

# python2: string.letters
# python3: string.ascii_letter
chars = "".join(list(filter(lambda c: c in string.letters,str(page_source))))
print(chars)

# Next level: equality

# Other solutions:

#1. Rare characters = less frequence than average

s = "".join([line.rstrip() for line in open("ocr.txt")])
OCCURRENCES = {}
for c in s: OCCURRENCES[c] = OCCURRENCES.get(c,0) + 1
avgOC = len(s) // len(OCCURRENCES)
chars = "".join([c for c in s if OCCURRENCES[c]<avgOC])
print (chars)

#2. use OrderedDict
data = "".join([line.rstrip() for line in open("ocr.txt")])
OCCURRENCES = collections.OrderedDict()
for c in data: OCCURRENCES[c] =  OCCURRENCES.get(c,0) + 1
avgOC = len(data) // len(OCCURRENCES)
chars = "".join([c for c in OCCURRENCES if OCCURRENCES[c] < avgOC])
print (chars)

#3 

print("".join([x for x in s if x.isalpha()]))

# slowest one
print("".join([x for x in s if s.count(x)<5])) 




