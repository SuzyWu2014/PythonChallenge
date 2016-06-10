import string

data = """g fmnc wms bgblr rpylqjyrc gr zw fylb. r
            fyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw f
            ylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr g
            q qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkk
            clbcb. lmu ynnjw ml rfc spj."""


# solution 1: without maketrans
def mapChar(char):
    if ord(char) >= ord("a") and ord(char) <= ord("z"):
        return chr((ord(char) + 2 - ord("a")) % 26 + ord("a"))
    else:
        return char

# data = "".join(map(lambda char: chr(ord(char)+2), data))
modified_data = "".join(map(lambda char: mapChar(char), data))

print(modified_data)

url = "map"
# trans = string.maketrans('abcdefghijklmnopqrstuvwxyz',
#                          'cdefghijklmnopqrstuvwxyzab')
trans = string.maketrans(string.ascii_lowercase,
                         string.ascii_lowercase[2:] +
                         string.ascii_lowercase[:2])
print (url.translate(trans))

# ocr

# Other solution:
print("".join(map(lambda x: x.isalpha() and chr((ord(x) + 2 - ord("a"))
                                                % 26 + ord("a")) or x, data)))

print("".join([(c.isalpha() and chr(ord('a') + (ord(c) - ord('a') + 2)
                                    % 26) or c) for c in "map"]))
