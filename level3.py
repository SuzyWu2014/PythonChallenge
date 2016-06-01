import re

data =  open("equality.txt").read()
pattern = re.compile(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')

matches = pattern.findall(data)
matches = "".join([string[4] for string in matches])

print(matches)


# "".join(re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',data))

# matches = "".join([data[i] for i in range(len(data)) if data[i].islower() and \
#                                                   data[i-3:i].isupper() and data[i+1:i+4].isupper() and \
#                                                   data[i-4].islower() and data[i+4].islower()])
