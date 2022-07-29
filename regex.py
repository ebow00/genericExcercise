import re

text = 'Price: $455,009.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, text)

print(matches.group(0))
print(matches.group(1))
price = matches.group(1)
print(float(price.replace(',', '')))
