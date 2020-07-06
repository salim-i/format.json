import json
from collections import Counter

with open("newsafr.json") as f:
    json_data = json.load(f)

words = []
for value in json_data["rss"]["channel"]["items"]:
    description = value["description"]
    news = description.lower().split()
    for word in news:
        if len(word) > 6:
            words.append(word)
            words.sort()
            c = Counter(words)
print(c.most_common(10))
