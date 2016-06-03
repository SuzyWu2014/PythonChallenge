from urllib.request import urlopen
import re


pageId = "12345"
pageIds = set()
pageIds.add(pageId)
for i in range(400): 
	data = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+pageId).read() 
	normal = "".join(re.findall('and the next nothing is [1-9]*',str(data)))
	if normal == "":
		print(data)
	new_pageId = "".join(re.findall('the next nothing is [0-9]*',str(data)))
	new_pageId = "".join(re.findall('[0-9]*',new_pageId))
	if new_pageId == "":
		new_pageId = str(int(pageId)//2)
	if new_pageId in pageIds:
		print(new_pageId)
		break
	else:
		pageId = new_pageId
		pageIds.add(pageId)

	print(pageId)
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
   url='http://www.pythonchallenge.com/pc/def/%s'
   u = url % 'linkedlist.php'
   nothing = '12345'
   while nothing.isdigit():
       s = urllib.urlopen(u + '?nothing=%s' % nothing).read()
       nothing = str(int(nothing)/2) if 'Divide' in s else s.split()[-1]
   print url % s