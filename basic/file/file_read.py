from pathlib import Path

from operation import Operation
import os

file = open("words.txt", Operation.READ)
lines = file.readlines()
for line in lines[1:]:
    print(line.strip())
file.close()

# with open ... as ...这种写法可以省去file.close的步骤，程序会自动帮忙关闭资源
print('===with open ... as ...====')
with open("words.txt", Operation.READ) as f:
    for line in f.readlines():
        print(line.strip())


print('===word append===')
file1 = 'words_bak.txt'
if not os.path.exists(file1):
    Path(file1).touch()
file_append = open(file1, Operation.READ_WRITE)
word1 = "I'm Sorry!"+"\n"
word2 = "You're Welcome!"+"\n"
append_lines = file_append.readlines()
if word1 not in append_lines:
    file_append.write(word1)
if word2 not in append_lines:
    file_append.write(word2)
file_append.close()

# import linecache
# 
# filename = 'C:\\Users\\Administrator.PC-201904211321\\Desktop\\start (2).log'
#
#
# # 放入缓存防止内存过载
# def get_line_count(filename):
#     line_count = 0
#     file = open(filename, 'r+')
#     while True:
#         buffer = file.read(8192 * 1024)
#         if not buffer:
#             break
#         line_count += buffer.count('\n')
#     file.close()
#     return line_count
#
#
# if __name__ == '__main__':
#     file1 = 'acceptor.txt'
#     if not os.path.exists(file1):
#         Path(file1).touch()
#     file_append = open(file1, Operation.READ_WRITE)
#     # get the last 30 lines
#     n = 20000
#     linecache.clearcache()
#     line_count = get_line_count(filename)
#     print('line count total:', line_count)
#     line_count = line_count - n
#     print('line_count:[%s]' % line_count)
#
#     # the last 20000 lines
#     for i in range(n+1):
#         last_line = linecache.getline(filename, line_count)
#         file_append.write(last_line)
#         line_count += 1
