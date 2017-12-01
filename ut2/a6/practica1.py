import sys

sentence = sys.argv[1]

def count_words(sentence):
	summary = {}
	words = sentence.split()
	for word in words:
		if word in summary:
			summary[word] += 1
		else:
			summary[word] = 1
	return summary
for name, count in (count_words(sentence)).items():
	print(name, count)
