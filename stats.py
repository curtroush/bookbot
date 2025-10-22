def get_word_count(text):
    count = 0
    for word in text.split():
        count = count + 1
    return count

def get_char_count(text):
    char_counts = {
    }

    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    results = []

    for key in char_dict:
        result = {}
        result["char"] = key
        result["num"] = char_dict[key]
        results.append(result)

    results.sort(reverse=True, key=sort_on)
    return results
