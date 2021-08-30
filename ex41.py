import random
from urllib.request import urlopen
import sys

# 注意编写代码文档时，采取的缩进格式的差异

# 这个网址打开是一系列单词，每个单词占一行
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# 注意这是一个字典
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# 根据书中的运行条件，结果是True
#True表示先打印value，按下任意键后再打印key
# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True
else:
	PHRASES_FIRST = False

# 字面意思，将连接中的单词以utf8格式，以字符串形式保存在WORDS列表中
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
	# str()方法的作用是把括号里的对象变成字符串，返回值是string格式
	#word = word.decode()
	#WORDS.append(word.strip())

def convert(snippet, phrase):
	#  capitalize()将字符串的第一个字母变成大写,其他字母变小写,注意第一个字母不得是空格
	#  count() 方法用于统计字符串里某个字符出现的次数。
	#  random.sample方法用来在WORDS这个列表中，随机取snippet.count("***")这么多个数的元素，但不改变列表的排序
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]  #（10个字符）
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")): # （4）
        param_count = random.randint(1,3)	#在范围内随机生成一个整数类型
        param_names.append(', '.join(
            random.sample(WORDS, param_count))) #以, 分隔来把列表连接成一个字符串

    for sentence in snippet, phrase:	# 遍历这两个列表，并且是有顺序的，先遍历前一个再遍历后一个
        result = sentence[:]		# 就是复制列表或者字符串  只复制内容，而不是关联两个变量，相当于strcpy

			# fake class names
        for word in class_names:	# 做替换
            result = result.replace("%%%", word, 1)

			# fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

			# fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# try except是一种异常处理机制，这里的EOFError是指出现不期望的文件结尾，通常是ctrl-d
# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())  # list将元组转换成列表 keys方法返回一个字典的所有键值
        random.shuffle(snippets) # shuffle方法将序列的所有元素随机排序

        for snippet in snippets:
            phrase = PHRASES[snippet]	# phrase等于字典里的键值对应的值
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")
