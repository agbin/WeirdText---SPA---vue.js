import random
import re


def shuffle_string(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)


def garble_word(word):
    # No operation needed on sufficiently small words
    # (Also, main algorithm requires word length >= 2)
    if len(word) <= 3:
        return word
    # Split word into first & last letter, and middle letters
    first, mid, last = word[0], word[1:-1], word[-1]
    return first + shuffle_string(mid) + last


def garble(sentence):
    SEPARATOR = "\n-weird-\n"
    tokenize_re = re.compile(r'(\w\w\w+)', re.U)
    words = tokenize_re.findall(sentence)
    words = [word for word in words if (word[1:-1])[1:] != (word[1:-1])[:-1]]
    words_sorted = sorted(words, key=str.lower)
    wodswym = [garble_word(word) for word in words if word]
    for i in range(0, len(words)):
        while words[i] == wodswym[i]:
            wodswym[i] = garble_word(words[i])
        sentence = re.sub(words[i], wodswym[i], sentence)
    words_sorted = ' '.join(words_sorted)
    encoded_text = SEPARATOR + sentence + SEPARATOR + words_sorted
    return encoded_text


text = "'This is a long looong test sentence,\n' 'with some big " \
       "(biiiiig) words!'"
print(garble(text))


def decode(encoded):
    t = encoded
    text_to_encoded = t[(t.find('-weird-')+9):(t.rfind('-weird-')-2)]
    tokenize_re = re.compile(r'(\w\w\w\w+)', re.U)
    text_to_encoded_list = tokenize_re.findall(text_to_encoded)
    original_words2 = t[(t.rfind('-weird-')+9)::]
    original_words2 = tokenize_re.findall(original_words2)
    for b in text_to_encoded_list:
        # print("b", b)
        for a in original_words2:
            # print("a", a)
            if a[0] == b[0] and a[-1] == b[-1] and len(a) == len(b):
                text_to_encoded = re.sub(b, a, text_to_encoded)
    return text_to_encoded


encoded = "'\n-weird-\n' 'Tihs is a lnog loonog tset sntceene,\n' " \
          "'wtih smoe big (biiiiig) wdros!' " \
          "'\n-weird-\n' 'long looong sentence some test This with words'"
print(decode(encoded))
