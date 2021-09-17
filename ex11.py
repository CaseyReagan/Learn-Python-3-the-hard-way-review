print("How old are you?", end=' ')			#为末尾end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串，其实这也是一个语法要求，表示这个语句没结束。
age = input()
print("How tall are you?", end=' ')			#print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


## my code for practise

name = input("enter your name:> ")
print("your name is",name)