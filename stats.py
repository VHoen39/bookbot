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

def sort_on(items):
    return items["num"]

def sorted_count_characters(character_stats):
    sorted_list = []
    for i in character_stats:
        sorted_list.append({"char": i, "num": character_stats[i]})
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list