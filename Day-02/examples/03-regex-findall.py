import re

text = "The quick brown fox had a brown tail and brown fur"
pattern = r"brown"

findall = re.findall(pattern, text)

print(findall)
