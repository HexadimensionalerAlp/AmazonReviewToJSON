import json
import os
import datetime


f = open('movies_json.json', 'w')
review = {}

for l in open('movies.txt', encoding="iso-8859-15", errors='ignore'):
    line = l.strip()
    if len(line) > 12:
        try:
            split = line.split(': ', 1)
            if len(split) == 2:
                review[split[0]] = split[1]
                if split[0] == 'review/text':
                    review['review/time'] = datetime.datetime.fromtimestamp(int(review['review/time'])).isoformat()
                    json.dump(review, f)
                    f.write(os.linesep)
                    review = {}
        except Exception as e:
            print(e)

f.flush()
