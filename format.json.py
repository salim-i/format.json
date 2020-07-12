import json

with open("newsafr.json") as f:
    json_data = json.load(f)

words = []

for value in json_data["rss"]["channel"]["items"]:
    description = value["description"]
    news = description.lower().split()
    for word in news:
        if len(word) > 6:
            words.append(word)

word_count = {}
for item in words:
  if item not in word_count:
    word_count[item] = 1
  else: 
    word_count[item] += 1

my_words = []

for keys, values in word_count.items():
    my_words.append((values,keys))
    my_words.sort(reverse = True)

for key, val in my_words[:10]:
  print (key, val)
