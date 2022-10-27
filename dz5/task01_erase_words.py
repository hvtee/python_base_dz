text = 'asgnj! abcioeyj aokth! abcabc opejabcdrg'
text = text.split()


def find_index(list_):
    indexes = []
    for i in range(len(list_)):
        if 'abc' in text[i]:
            indexes.append(i)
    return indexes


for i in range(len(find_index(text))):
    text.pop(find_index(text)[0])
print(text)
