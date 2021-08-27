import sys
script, input_encoding, error = sys.argv	#	ex23.py utf-8 strict

def main(language_file, encoding, errors):
	line = language_file.readline()

	# 这段代码的用处是当line存在（文件按行读取不为空），就按print_line函数执行输出
	# 当执行了一次输出之后，return执行另一个main函数，这一点可能是python特有，C里没
	# 见过这种用法，很精妙，这样不用循环也能实现函数不断调用，直至if判断不满足（即文件读完了）
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
	# strip方法作用，在默认参数下是去除字符串两边的空格和换行符
	next_lang = line.strip()
	# encode方法是把字符串按照encoding模式编码
	# errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。
	raw_bytes = next_lang.encode(encoding, errors=errors)
	# decode与encode相对，是把编码按encoding模式解码成字符串
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


# 额外内容
# def func_a():
# 	print("AAAA.")

# def func_b():
# 	if True:
# 		func_a()
# 	else:
# 		#一些代码

# def fun_c():
# 	if True:
# 		func_c()
# 	else:
# 		#一些代码