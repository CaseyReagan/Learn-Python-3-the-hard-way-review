from sys import argv

script, filename = argv

txt = open(filename)			#python的文件读取方法，这里filename要是系统参数输入，但是一定要名字完整包括后缀

print(f"Here's your file {filename}:")
print(txt.read())				# read方法读取文件指针指向的内容
txt.close()						# 用完之后要close文件（类似释放指针）

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()