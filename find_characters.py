# pylint: disable=print-statement
word_list = ["hello", "world", "my", "name", "is", "Anna"]
char = "e"
newlist = []

for word in word_list:
    for string in word:
        if string == char:
            newlist.append(word)
print newlist