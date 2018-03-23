import pandas
from autocorrect import spell
import csv
import os.path
import matplotlib.pyplot as plt

if not os.path.isfile('clean.csv'):
    rows = csv.reader(open('data.csv'))

    f = open('clean.csv', 'w+')
    writer = csv.writer(f)

    for row in rows:
        row = [x.strip().lower() for x in row]
        writer.writerow(row)
    f.close()

df = pandas.read_csv('clean.csv')

def histogram_values(columns):
    where = df.groupby([c.lower() for c in columns])
    return where[sorted([c.lower() for c in columns])].count()

def graph(columns, filename):
    histogram_values(columns).plot(kind='barh', legend=False, title=filename, stacked=True).get_figure().savefig('images/' + filename, bbox_inches='tight')

def multivalue_map(column_name):
    attractionMap = {}

    for attraction in df[column_name.lower()]:
        try:
            attractionSplit = [a.strip() for a in attraction.split(',') if a.strip()]
            for a in attractionSplit:
                attractionMap[a] = attractionMap.get(a, 0) + 1 
        except Exception as e:
            pass

    for k, v in sorted(attractionMap.items(), key=lambda value: value[1], reverse=True)[:5]:
        print(k, v)

graph(histogram_values(['How did you first hear about Surprise Ride?']), 'how-did-you-hear.png')
graph(histogram_values(['what is the purchaser\'s primary relationship to the surprise ride recipient?']), 'primary-relationship.png')
graph(histogram_values(['what was the purchaser\'s age? (at the time of sign up)']), 'purchaser-age.png')
graph(histogram_values(['what was the surprise ride recipient\'s age? (at the time of sign up)']), 'recipient-age.png')
graph(histogram_values(['what is the surprise rider recipient\'s gender?']), 'recipient-gender.png')
graph(histogram_values(['household income']), 'household-income.png')
graph(histogram_values(['Level of screen limits']), 'screen-limits.png')
graph(histogram_values(['Have you referred Surprise Ride to a friend?']), 'referral.png')
graph(histogram_values(['Where do you typically buy children’s product?']), 'where-product.png')

graph(histogram_values(['Other sub']), 'have-other-subscriptions.png')
graph(histogram_values(['What other subscriptions services do you have and what would you change about them?']), 'other-subscriptions.png')

graph(histogram_values(['household income', 'Where do you typically buy children’s product?']), 'income-to-where.png')
graph(histogram_values(['household income', 'Other sub']), 'income-to-other-subscriptions.png')

# print(histogram_values(['How did you first hear about Surprise Ride?']))
# multivalue_map('attracted')
# print(histogram_values(['what is the purchaser\'s primary relationship to the surprise ride recipient?']))
# print(histogram_values(['what was the purchaser\'s age? (at the time of sign up)']))
# print(histogram_values(['what was the surprise ride recipient\'s age? (at the time of sign up)']))
# print(histogram_values(['what is the surprise rider recipient\'s gender?']))
# print(histogram_values(['household income']))
# print(histogram_values(['Level of screen limits']))
# print(histogram_values(['Have you referred Surprise Ride to a friend?']))
# print(histogram_values(['Where do you typically buy children’s product?']))

# print(histogram_values(['Other sub']))
# print(histogram_values(['What other subscriptions services do you have and what would you change about them?']))

# print(histogram_values(['household income', 'Where do you typically buy children’s product?']))
# print(histogram_values(['household income', 'Other sub']))

# print(dir(histogram_values(['Would you be interested in buying single Surprise Ride kits if you saw them for sale in a store or on Amazon?']).plot))

graph(histogram_values(['Would you be interested in buying single Surprise Ride kits if you saw them for sale in a store or on Amazon?']), 'sale-in-store.png')
graph(histogram_values(['household income']), 'household-income.png')

# cancellations
graph(histogram_values(['Why did you cancel your subscription?']), 'why-cancel.png')
graph(histogram_values(['What would have prevented you from canceling?']), 'prevent-cancel.png')
graph(histogram_values(['What do you think the right price is for Surprise Ride activity kits?']), 'right-price.png')

# evaluating solutions
graph(histogram_values(['content']), 'interesting-content.png')
graph(histogram_values(['Interested in digital content']), 'interested-digital-content.png')
graph(histogram_values(['How much would you pay for the above concept?']), 'how-much-would-you-pay.png')
graph(histogram_values(['interested in pikcing bundles']), 'interested-picking-bundles.png')