from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):		#倒带，指光标回到原点
	f.seek(0)		#用seek（0）回到文件第一个字符

def print_a_line(line_count,f):
	print(line_count, f.readline())		#按行读取文件内容

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
#current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
#current_line += 1
print_a_line(current_line, current_file)