import zipfile
# import re
import urllib

o, number, file = [], "90052", "%s.txt"
content = "Next nothing is (\d+)"

zip_url = "http://www.pythonchallenge.com/pc/def/channel.zip"
urllib.urlretrieve(zip_url, "channel.zip")

zip_archive = zipfile.ZipFile("channel.zip")
zipdict = {}

for info in zip_archive.infolist():
    zipdict[info.filename] = info.comment

current_nothing = '90052'
while True:
    print zipdict[current_nothing + '.txt'],
    page = zip_archive.read(current_nothing + '.txt')
    try:
        current_nothing = page.split('Next nothing is ')[1]
    except IndexError:
        break

# zobj = StringIO()
# zobj.write(urllib.urlopen("http://pythonchallenge.com/pc/def/channel.zip").read())
# z = zipfile.ZipFile(zobj)

# filenum = "90052"
# lcomment = []

# while True:
#     if filenum.isdigit():
#         filename = filenum + '.txt'
#         lcomment.append(z.getinfo(filename).comment)
#         info = z.read(filename)
#         filenum = info.split(' ')[-1]
#     else:
#         break
# z.close()
# print ''.join(lcomment)
