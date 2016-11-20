import json
import os
from collections import Counter
import argparse

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


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Merge json splits.')
    parser.add_argument('--input', dest="input", type=str, required=True, help='a directory containing json files to be merged')
    parser.add_argument('--output', dest='output', type=str, required=True, help='the destination directory for "event-pairs.json"')

    args = parser.parse_args()
    data = get_annotations(args.input)
    outfile = "{}/event-pairs.json".format(args.output)

    # dump annotations
    json.dump(filter_bugs(data), open(outfile, "w"), indent=2, sort_keys=True)
