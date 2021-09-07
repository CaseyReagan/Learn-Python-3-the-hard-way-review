class ParserError(Exception):
	pass

class Sentence(object):

	def __init__(self, subject, verb, obj):
	## remember we take ('noun', 'princess') tuples and convert them.
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]

## 返回word_list里的第一个单词
## 我需要窥探列表中的单词来决定我正在处理的句子是什么类型
def peek(word_list):
	if word_list:
		word = word_list[0]
## peek这里实际返回的是下一个单词的类型，比如verb，noun
		return word[0]
	else:
		return None

# 检查word_list里是否是我们需要的内容
# ，然后我需要匹配这些单词来创建我的 Sentence。
def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)

## 判断当前单词的type是不是我们想要的类型，如果是的话，就将这对词组返回
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None
	pass

## skip 不只跳过一个单词，它会跳过所有它所找到的那个类型的单词。
def skip(word_list, word_type):
## 当单词的类型与我们想要跳过的单词一样的时候，就进行（跳过）到下一个单词，如果不一样就退出循环
	while peek(word_list) == word_type:
		match(word_list, word_type)

def parse_verb(word_list):
	skip(word_list,'stop')

## 查看下一个单词是不是verb
	if peek(word_list) == 'verb':
## 如果是“verb”，那就进行匹配，并把它从列表中拿出来
		return match(word_list, 'verb')
## 如果下一个单词不是verb的话，就返回一个错误信息
	else:
		raise ParserError("Expected a verb next.")

# 原理与上面相同，跳过所有的stop单词，先窥探，然后基于内容决定句子是否正确
# 有两个if条件的原因是，宾语里既可能是名词也可能是方向词

def parse_object(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("Expected a verb next.")

## 最终句子的解释器
def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)

## 测试举例x = parse_sentence([('verb', 'run'), ('direction', 'north')])