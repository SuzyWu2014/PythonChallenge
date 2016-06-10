from urllib.request import urlopen
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

data = pickle.load(urlopen(url))

for line in data:
	print("".join(elem[0] * elem[1] for elem in line))

# for line in data:
#    print "".join(map(lambda pair: pair[0]*pair[1], line))
# next level: channel
