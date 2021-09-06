WORD_TYPE = {
	"north" : "direction",
	"south" : "direction",
	"east" : "direction",
	"west" : "direction",
	"go" : "verb",
	"eat" : "verb",
	"kill" : "verb",
	"the" : "stop",
	"in" : "stop",
	"of" : "stop",
	"bear" : "noun",
	"princess" : "noun",
}

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(sentence):
	words = sentence.split()
	result = []

	for word in words:
		word_type = WORD_TYPE.get(word)

		if word_type == None:
			# it might be a number, so try converting
			number = convert_number(word)

			if number != None:
				result.append(('number',number))
			else:
				result.append(('error',word))

		else:
			result.append((word_type,word))

	return result