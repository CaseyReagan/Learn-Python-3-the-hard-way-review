from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv			# 在windows命令行里给这个代码赋予系统参数就可以运行，例如代码python ex13.py a b c

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)