import json

__author__ = 'robot'

with open('topics-unsorted.json') as data_file:
    topics = json.load(data_file)
    sorted_topic = sorted(topics, key=lambda k: int(k['proof']), reverse=True)
    with open('topics-temp.json', 'w') as outfile:
        json.dump(sorted_topic, outfile)
