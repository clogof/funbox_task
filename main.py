import sys
import re

def status_count(filepath, find_status):
    data = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        while (row := f.readline().rstrip()):
            reg = r'\[(\d{4}-\d{2}-\d{2}\s\d{2}\:\d{2}):\d{2}\]\s(\w+)'
            r = re.match(reg, row)
            if r is None:
                continue
            
            ts = r.group(1)
            status = r.group(2)

            if status != find_status:
                continue

            if ts not in data:
                data[ts] = 0
            data[ts] += 1
    
    return data


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("\nmain.py need: <filepath>\n")
        exit(1)

    filepath = args[1]
    res = status_count(filepath, 'NOK')

    for k, v in res.items():
        print(k, "-", v)
