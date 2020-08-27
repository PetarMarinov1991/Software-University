import re

regex = r"\b_[0-9a-zA-Z]+\b"
ids = re.findall(regex, input())

print(','.join([i[1:] for i in ids]))
