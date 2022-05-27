from datetime import datetime
import random

# 1653570000 2022-05-26 13:00:00
# 1653577200 2022-05-26 15:00:00

rows_count = 1000
ts = []

for _ in range(rows_count):
    x = random.randint(1653570000, 1653577200)
    ts.append(x)

ts.sort()

with open('events.log', 'w', encoding='utf-8') as f:
    for t in ts:
        t_str = datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        status = "OK" if random.choice([0, 1]) == 1 else "NOK"

        row = f'[{t_str}] {status}\n'
        f.write(row)
