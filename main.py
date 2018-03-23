import pandas
from autocorrect import spell
import csv

# rows = csv.reader(open('data.csv'))

# f = open('clean.csv', 'w+')
# writer = csv.writer(f)

# for row in rows:
#     row = [x.strip().lower() for x in row]
#     writer.writerow(row)
# f.close()

df = pandas.read_csv('clean.csv')

def histogram_values(columns):
    where = df.groupby([c.lower() for c in columns])
    return where[[c.lower() for c in columns]].count()

print(histogram_values(['How did you first hear about Surprise Ride?']))