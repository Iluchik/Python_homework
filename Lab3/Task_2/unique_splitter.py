from collections import Counter
import re

def number_of_words(string: str):
	count = Counter(filter(None, re.split(r"[., \-!?:]+", string)))
	print(count)

number_of_words(input())