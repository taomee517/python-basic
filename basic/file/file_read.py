from operation import Operation

file = open("words.txt", Operation.READ)
lines = file.readlines()
for line in lines[1:]:
    print(line)
file.close()


file_append = open("words.txt", Operation.READ_WRITE)
word1 = "I'm Sorry!"+"\n"
word2 = "You're Welcome!"+"\n"
append_lines = file_append.readlines()
if word1 not in append_lines:
    file_append.write(word1)
if word2 not in append_lines:
    file_append.write(word2)
file_append.close()
