def find_index(data, index):
    while True:
        if 'title' not in data.entries[0].links[index].keys():
            index += 1
            continue
        if data.entries[0].links[index].title != 'pdf':
            index += 1
        else:
            return index
        return -1
