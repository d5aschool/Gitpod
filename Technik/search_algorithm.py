# This is the list with all possible values
# put all your trash in here:
lst: list = [
    "simon",
    "niklas",
    "steven",
    "phi-anh"
]

def search(values: list, query: str) -> [bool, int]:
    # This is the string-sequence the algorithm should search for in the list. 
    # Should be in lower-case... MUST be in lower-case!
    query = query.lower()

    # Index of the query. This will be changed by the for-loop.
    # Better don't have or you will break everything like always!
    idx: int = 0

    # Iterate through every object in list
    for value in values:
        
        # is q in lower(entry) ?
        # we have to make the value lower, because we want to check for "A" in "A" AND "a":
            # entry = "sImOn"
            # entry         == "simon": false
            #  entry.lower() == "simon": true
        if query in value.lower():
            # return True and found index
            return True, idx
        else:
            # count index 1 up
            idx += 1

    # if value was not found in list, return False and -1.
    return False, -1
    
# search list "lst" for "phi-anhh"
found, index = search(lst, "phi-anh")

# if it was found, print "Gefunden an Index :index:"
if found:
    print(f"Gefunden an Index {index}")

# otherwise "Leider nicht gefunden. (res: :index:)"
else:
    print(f"Leider nicht gefunden. (res: {index})")