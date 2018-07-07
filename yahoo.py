import itertools

database ={"Name":"Arnold", "Age":"52", "Height":"160"}

def search(s):
    s = s.lower() # it is a nice feature to ignore case
    #f#or item in database:
    if any(s in v.lower() for v in database): # if any value contains s
            yield v # spit out the item — this is a generator function

# iterate over at most 5 first results
for result in itertools.islice(search("52"), 5):
    print(result)
print(search("nol"));