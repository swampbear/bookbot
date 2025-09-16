import string

def get_num_words(text):
    text_arr = text.split()
    length = len(text_arr)
    return length

def sort_on(items):
    return items["num"]


def get_sorted_dict_list(items):
    l = []
    for item in items:
        l.append({"char": item, "num": items[item]})
    l.sort(reverse=True, key=sort_on)
    return l
    


def get_letter_distribution(text):
    text = text.lower()
    alphabet= list(string.ascii_lowercase)
    dis = dict.fromkeys(alphabet, 0)
    txt_arr = text.split()
    for w in txt_arr:
        for c in w:
            if not c.isalpha() or c not in dis:
                continue
            dis[c] += 1
    return dis
    

