def count_words(text):
    text=text.split()
    return len(text)

def count_characters(text):
    text = text.lower()
    count_stats = {}
    for i in text:
        if i in count_stats:
            count_stats[i] = count_stats[i] + 1
        else:
            count_stats[i] = 1
    return count_stats

testdict = {"a":1}
testdict["b"] = 2
print (testdict)
