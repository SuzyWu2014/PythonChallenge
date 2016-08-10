def solution(S):
    # write your code in Python 2.7
    lines = S.split("\n")
    path_sum = 0
    spaces = 0
    for line in lines:
        print path_sum
        print spaces
        if ".gif" in line or ".jpeg" in line:
            spaces = len(line) - len(line.lstrip())
        if spaces > len(line) - len(line.strip()):
            path_sum = path_sum + len(line.lstrip()) + 1
            spaces = spaces - 1
            print path_sum
    return path_sum
# 'dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif'

print solution("dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif")