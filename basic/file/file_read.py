from pathlib import Path

from operation import Operation
import os

file = open("words.txt", Operation.READ)
lines = file.readlines()
for line in lines[1:]:
    print(line)
file.close()

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
