import re
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
    
def entry_metadata (data, entry_data):
    base = data.entries[0]

    doi = base[entry_data[0]]
    title = base[entry_data[1]].lower()
    published = base[entry_data[2]]
    updated = base[entry_data[3]]
    summary = base[entry_data[4]].lower()
    summary = re.sub("\n"," ", summary)
    
    authors = base[entry_data[5]] #to normalize later
    authors = [nam.name.lower() for nam in authors]

    affiliation = base[entry_data[6]].lower()

    mong = {
        "doi" : doi,
        "title" : title,
        "published" : published,
        "updated" : updated,
        "summary" : summary,
        "authors" : authors,
        "affiliation" : affiliation
    }
    return mong