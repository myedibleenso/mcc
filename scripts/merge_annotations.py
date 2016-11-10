import json
import os
from collections import Counter

def get_annotations(d):
    data = []
    for f in os.listdir(d):
        somefile = os.path.join(d, f)
        if f.endswith("json"):
            print(somefile)
            data += json.load(open(somefile))
        else:
            print("{} does not end in json".format(f))
    return data

def filter_bugs(data):
    return [d for d in data if d["relation"] != "Bug"]

directory = "/Users/gus/repos/reach-resources/recovered-annotations/annotation-splits/verified/"
outfile = "/Users/gus/repos/reach-resources/wip/event-pairs.json"

data = get_annotations(data)

# dump annotations
json.dump(filter_bugs(data), open(outfile, "w"), indent=2, sort_keys=True)
